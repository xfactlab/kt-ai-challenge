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


BODY_TEMP = {
    "serviceInstanceId" : "ddm3kz9g",
    "nluType" : "009",
    "apiType" : "002",
    "utterance" : None
}


PROMPT1 = "질문: 나탈리아는 4월에 친구 48명에게 클립을 팔았고, 그리고 5월에는 그 절반만큼을 팔았습니다. 나탈리아는 4월과 5월에 모두 몇 개의 클립을 팔았을까요? \
풀이: 나탈리아는 5월에 48/2 = 24개의 클립을 판매했습니다. 나탈리아는 4월과 5월에 모두 48+24 = 72개의 클립을 판매했습니다. \
정답: 72 \\n"


def get_gsm8k_zs(que):
    prompt = f'질문 : {que} \n정답 : '
    return prompt


def get_gsm8k_one_shot_cot(pre_prompt, que):
    suf_prompt = f'질문: {que} 풀이 : '
    prompt = pre_prompt + suf_prompt
    return prompt


def get_gsm8k_zs_cot(que):
    prompt = f"질문: {que} 정답: 질문을 단계적으로 풀어보면, "
    return prompt


def get_body(prompt, body_temp):
    body_temp["utterance"] = prompt
    return json.dumps(body_temp)


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

    # Reading input_file
    data = utils.read_jsonlines(input_file)


    for ins in tqdm(data):
        kor_que = ins['kor_question']

        # checking whether there is an answer
        test = kor_que.split('\n')

        if len(test[0]) != len(kor_que):
            continue

        prompt = get_gsm8k_zs_cot(kor_que)

        body = get_body(prompt, BODY_TEMP)
        response = model.generate(body)
        res_context = response.json()['data'][0]['result'][0]

        ins['kor_infer'] = res_context
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

# python zero-shot-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api.json \
# --input_file /userhomes/philhoon/kt-ai-challenge/data/openai-gpt-3.5-turbo-0301-2048-0.0-KOR-gsm8k-test.jsonl \
# --output_path /userhomes/philhoon/kt-ai-challenge/result \
# --output_file_name zero-shot-cot-result-ko-gsm8k-test.jsonl
