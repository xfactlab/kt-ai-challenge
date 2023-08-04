import json
import requests
from src import utils
import time
import os
import argparse
from tqdm import tqdm

class model_api():
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def generate(self, body):

        try:
            response = requests.post(self.url, data=body, headers=self.headers, verify=False)

        except:
            print("retrying due to an error......")
            time.sleep(20)
            return self.generate(body)

        return response


def get_mwp_zs_cot(que):
    prompt = f"질문: {que} 정답: 질문을 단계적으로 풀어보면, "
    return prompt


def get_body(prompt, body_temp):
    body_temp["utterance"] = prompt
    return json.dumps(body_temp)


def main(args):

    input_file = args.input_file
    output_file = args.output_path


    # Create output_file & initializing file writer
    print(f'output_file : {output_file}')
    jsonl_writer = utils.JSONLWriter(output_file)

    # Initialzing api
    api = utils.read_json_file(args.api_path)
    model = model_api(api['url'], api['headers'])
    BODY_TEMP = api['body']

    # Reading input_file
    data = utils.read_jsonlines(input_file)


    for ins in tqdm(data):
        kor_que = ins['question']

        prompt = get_mwp_zs_cot(kor_que)

        body = get_body(prompt, BODY_TEMP)
        response = model.generate(body)
        res_context = response.json()['data'][0]['result'][0]

        ins['zs_cot_infer'] = res_context
        jsonl_writer.write_json_line(ins)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Eval script for GSM8K")

    # API information
    parser.add_argument("--api_path", type=str, default='/userhomes/philhoon/kt-ai-challenge/api.json',
                        help="Path to the API key file")

    # Input information
    parser.add_argument("--input_file", type=str, default='/userhomes/philhoon/kt-ai-challenge/data/openai-gpt-3.5-turbo-0301-2048-0.0-KOR-gsm8k-test.jsonl', help="Path to the input file")

    # Output location
    parser.add_argument("--output_path", type=str, default='/userhomes/philhoon/kt-ai-challenge/result', help="Path to the output directory")

    args = parser.parse_args()
    main(args)

# python mwp-zs-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api.json \
# --input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_preprocess.jsonl \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/zero-shot-cot-public_mwp_data_v2_preprocess
