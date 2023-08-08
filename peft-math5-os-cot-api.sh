#!/bin/bash

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-kor-D_addsub-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-kor-D_addsub-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-kor-D_multiarith-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-kor-D_multiarith-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-kor-D_single_eq-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-kor-D_single_eq-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs \
--input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning-test.jsonl \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-public_mwp_data_v2_reasoning-test.jsonl

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft3.json \
--method zs-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning-test.jsonl \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft3-zs-cot-public_mwp_data_v2_reasoning-test.jsonl

