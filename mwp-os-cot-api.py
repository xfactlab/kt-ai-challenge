import json
import requests
from src import utils
import time
import os
import argparse
from tqdm import tqdm


PROMPT1 = "질문: 반짇고리 안에는 여러 가지 모양의 단추가 있습니다. 동그란 단추는 6개가 들어있고, 네모난 단추와 세모난 단추는 각각 3개씩 들어 있습니다. 동그란 단추는 네모난 단추보다 몇 개가 더 많습니까? \
풀이: 동그란 단추는 6개, 네모난 단추는 3개, 세모난 단추는 3개가 있습니다. 동그란 단추는 네모난 단추보다 3개가 더 많습니다. 이를 수식으로 나타내면, 동그란 단추의 개수(6개) - 네모난 단추의 개수(3개) = 3개입니다. 따라서 동그란 단추는 네모난 단추보다 3개가 더 많습니다. \
정답: 3 \\n"


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


def get_mwp_one_shot_cot(pre_prompt, que):
    suf_prompt = f'질문: {que} 풀이 : '
    prompt = pre_prompt + suf_prompt
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

        prompt = get_mwp_one_shot_cot(PROMPT1, kor_que)

        body = get_body(prompt, BODY_TEMP)
        response = model.generate(body)
        res_context = response.json()['data'][0]['result'][0]

        ins['os_cot_infer'] = res_context
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

# python mwp-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api.json \
# --input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning.jsonl \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/one-shot-cot-public_mwp_data_v2_test.jsonl
