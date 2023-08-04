import json
import requests
from src import utils
import time
import os
import argparse
import csv
import re
from tqdm import tqdm

PROMPT2 = "질문: 항아리 안에 몇 개의 젤리빈이 있습니다. 젤리빈의 3/4은 빨간색이며, 빨간색 젤리빈의 1/4은 코코넛 맛입니다. 코코넛 맛 젤리빈이 750개이면, 항아리 안에는 몇 개의 젤리빈이 있나요? \
풀이: 젤리콩이 750*4=3000개가 있습니다. 그리고 병 안에는 3000/3*4=4000개의 젤리콩이 있습니다. \
정답: 4000 \\n"

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


def get_body(prompt, body_temp):
    body_temp["utterance"] = prompt
    return json.dumps(body_temp)


def get_gsm8k_build_data_with_one_shot_cot_finetuning(kor_que, kor_ans, ans_s, PROMPT1):
    PROMPT1
    prompt = f"질문: {kor_que} 풀이: "
    output = f"{kor_ans} 정답: {ans_s}"

    prompt = PROMPT1 + prompt
    return prompt, output


def main(args):

    input_file = args.input_file
    output_path = args.output_path


    # Create output_file & initializing file writer
    os.makedirs(output_path, exist_ok=True)
    output_file = output_path + '/' + args.output_file_name
    print(f'output_file : {output_file}')
    jsonl_writer = utils.JSONLWriter(output_file)

    # Initialzing api
    api = utils.read_json_file(args.api_path)
    model = model_api(api['url'], api['headers'])
    BODY_TEMP = api['body']

    # Reading input_file
    data = utils.read_jsonlines(input_file)


    for ins in tqdm(data):
        kor_que = ins['kor_question']
        ans_s = ins['answer_s']
        kor_ans = ins['kor_answer']

        prompt, _ = get_gsm8k_build_data_with_one_shot_cot_finetuning(kor_que, kor_ans, ans_s, PROMPT2)

        body = get_body(prompt, BODY_TEMP)
        response = model.generate(body)
        res_context = response.json()['data'][0]['result'][0]

        ins['peft2_infer'] = res_context
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
    parser.add_argument("--output_file_name", type=str, default='zero-shot-cot-result-ko-gsm8k-test.jsonl', help="Path to the output directory")

    args = parser.parse_args()
    main(args)

# python peft2-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft2.json \
# --input_file /userhomes/philhoon/kt-ai-challenge/result/kor-gsm8k-peft2-test.jsonl \
# --output_path /userhomes/philhoon/kt-ai-challenge/result \
# --output_file_name peft2-result-ko-gsm8k-test.jsonl
