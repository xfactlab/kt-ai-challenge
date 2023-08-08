#!/bin/bash

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method os-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-1shot-cot-kor-D_addsub-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method three-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-3shot-cot-kor-D_addsub-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method os-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-1shot-cot-kor-D_multiarith-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method three-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-3shot-cot-kor-D_multiarith-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method os-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-1shot-kor-D_single_eq-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method three-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-3shot-cot-kor-D_single_eq-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method os-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning-test.jsonl \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-1shot-public_mwp_data_v2_reasoning-test.jsonl

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method three-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning-test.jsonl \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-3shot-cot-public_mwp_data_v2_reasoning-test.jsonl

