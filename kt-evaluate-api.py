import json
import requests
from src import utils
import time
import os
from pprint import pprint
import random
from tqdm import tqdm
import argparse

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


PROMPT1 = "다음 질문에 차근차근 답하시오. 질문: 나탈리아는 4월에 친구 48명에게 클립을 팔았고, 그리고 5월에는 그 절반만큼을 팔았습니다. 나탈리아는 4월과 5월에 모두 몇 개의 클립을 팔았을까요? \
풀이: 나탈리아는 5월에 48/2 = 24개의 클립을 판매했습니다. 나탈리아는 4월과 5월에 모두 48+24 = 72개의 클립을 판매했습니다. \
정답: 72 "

PROMPT2 = "다음 질문에 차근차근 답하시오. 질문: 데이비드는 장난감 강아지가 들어있는 상자를 7개 가지고 있습니다. 각 상자에는 강아지가 4마리씩 들어있습니다. 모두 몇 마리의 강아지가 있을까요? \
풀이: 7개의 상자가 있습니다. 각 상자에는 4마리의 개가 있습니다. 그러므로, 모두 몇 마리의 개가 있는지 알기 위해 곱셈을 할 수 있습니다. 7개의 상자 x 1상자당 4마리의 개 = 28마리의 개입니다. \
정답: 28 "

PROMPT3 = "다음 질문에 차근차근 답하시오. 질문: 카렌은 639개의 크레용을 가지고 있습니다. 신디는 504개의 크레용을 가지고 있습니다. 카렌은 신디보다 얼마나 더 많은 크레용을 가지고 있나요? \
풀이: 카렌은 639개의 크레용을 가지고 있습니다. 신디는 504개의 크레용을 가지고 있습니다. 카렌이 신디보다 얼마나 더 많은 크레용을 가지고 있는지 알기 위해서는 카렌의 크레용 개수에서 신디의 크레용 개수를 빼야 합니다. 639 - 504 = 135 카렌은 신디보다 135개의 크레용을 더 가지고 있습니다. \
정답: 135 "

PROMPT1_P = "질문: 나탈리아는 4월에 친구 48명에게 클립을 팔았고, 그리고 5월에는 그 절반만큼을 팔았습니다. 나탈리아는 4월과 5월에 모두 몇 개의 클립을 팔았을까요? \
풀이: 단계별로 풀어보면, 나탈리아는 5월에 48/2 = 24개의 클립을 판매했습니다. 나탈리아는 4월과 5월에 모두 48+24 = 72개의 클립을 판매했습니다. \
정답: 72 "

PROMPT2_P = "질문: 데이비드는 장난감 강아지가 들어있는 상자를 7개 가지고 있습니다. 각 상자에는 강아지가 4마리씩 들어있습니다. 모두 몇 마리의 강아지가 있을까요? \
풀이: 단계별로 풀어보면, 7개의 상자가 있습니다. 각 상자에는 4마리의 개가 있습니다. 그러므로, 모두 몇 마리의 개가 있는지 알기 위해 곱셈을 할 수 있습니다. 7개의 상자 x 1상자당 4마리의 개 = 28마리의 개입니다. \
정답: 28 "

PROMPT3_P = "질문: 카렌은 639개의 크레용을 가지고 있습니다. 신디는 504개의 크레용을 가지고 있습니다. 카렌은 신디보다 얼마나 더 많은 크레용을 가지고 있나요? \
풀이: 단계별로 풀어보면, 카렌은 639개의 크레용을 가지고 있습니다. 신디는 504개의 크레용을 가지고 있습니다. 카렌이 신디보다 얼마나 더 많은 크레용을 가지고 있는지 알기 위해서는 카렌의 크레용 개수에서 신디의 크레용 개수를 빼야 합니다. 639 - 504 = 135 카렌은 신디보다 135개의 크레용을 더 가지고 있습니다. \
정답: 135 "


def get_3s_cot_post(que):
    prompt = PROMPT1_P + PROMPT2_P + PROMPT3_P + f"질문: {que} 풀이: 단계별로 풀어보면,"
    return prompt

def get_os_cot_post(que):
    prompt = PROMPT1_P + f"질문: {que} 풀이: 단계별로 풀어보면,"
    return prompt

def get_zs_cot_post(que):
    prompt = f"질문: {que} 풀이: 단계별로 풀어보면,"
    return prompt


def get_gsm8k_3s_cot(que):
    prompt = PROMPT1 + PROMPT2 + PROMPT3 + f"다음 질문에 차근차근 답하시오. 질문: {que} 풀이: "
    return prompt

def get_gsm8k_os_cot(que):
    prompt = PROMPT1 + f"다음 질문에 차근차근 답하시오. 질문: {que} 풀이: "
    return prompt

def get_gsm8k_zs3(que):
    prompt = f"다음 질문에 차근차근 답하시오. 질문: {que} 풀이: "
    return prompt


def get_body(prompt, body_temp):
    body_temp["utterance"] = prompt
    return json.dumps(body_temp)


def main(args):

    input_file = args.input_file
    output_file = args.output_path
    method = args.method


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

        if 'kor_question' in ins:
            kor_que = ins['kor_question']
        else:
            kor_que = ins['question']

        if method == 'zs':
            prompt = kor_que
        elif method == 'zs-cot':
            prompt = get_gsm8k_zs3(kor_que)
        elif method == 'os-cot':
            prompt = get_gsm8k_os_cot(kor_que)
        elif method == 'three-cot':
            prompt = get_gsm8k_3s_cot(kor_que)
        elif method == 'zs-cot-post':
            prompt = get_zs_cot_post(kor_que)
        elif method == 'os-cot-post':
            prompt = get_os_cot_post(kor_que)
        elif method == 'three-cot-post':
            prompt = get_3s_cot_post(kor_que)

        body = get_body(prompt, BODY_TEMP)

        response = model.generate(body)
        res_context = response.json()['data'][0]['result'][0]

        ins['peft3_infer'] = res_context
        jsonl_writer.write_json_line(ins)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Eval script for GSM8K")

    # API information
    parser.add_argument("--api_path", type=str, default='/userhomes/philhoon/kt-ai-challenge/api-peft3.json',
                        help="Path to the API key file")

    # Input information
    parser.add_argument("--method", type=str, default='/userhomes/philhoon/kt-ai-challenge/api-peft3.json',
                        help="Path to the API key file")
    parser.add_argument("--input_file", type=str, default='/userhomes/philhoon/kt-ai-challenge/data/openai-gpt-3.5-turbo-0301-2048-0.0-KOR-gsm8k-test.jsonl', help="Path to the input file")

    # Output location
    parser.add_argument("--output_path", type=str, default='/userhomes/philhoon/kt-ai-challenge/result', help="Path to the output directory")

    args = parser.parse_args()
    main(args)

# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs \
# --input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-kor-D_addsub-test.json
#
# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs-cot \
# --input_file /userhomes/philhoon/kt-ai-challenge/data/kor-D_addsub-test.json \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-kor-D_addsub-test.json
#
#
# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs \
# --input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-kor-D_multiarith-test.json
#
# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs-cot \
# --input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-kor-D_multiarith-test.json
#
#
# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs \
# --input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-kor-D_single_eq-test.json
#
#
# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs-cot \
# --input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-kor-D_single_eq-test.json
#
#
# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs \
# --input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning-test.jsonl \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-public_mwp_data_v2_reasoning-test.jsonl
#
# python peft3-math5-os-cot-api.py \
# --api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
# --method zs-cot \
# --input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning-test.jsonl \
# --output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-public_mwp_data_v2_reasoning-test.jsonl


