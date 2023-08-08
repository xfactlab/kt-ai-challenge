#!/bin/bash

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method zs-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-zs-cot-post-kor-D_addsub-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method os-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-1shot-cot-post-kor-D_addsub-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method three-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-3shot-cot-post-kor-D_addsub-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method zs-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-zs-cot-post-kor-D_multiarith-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method os-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-1shot-cot-post-kor-D_multiarith-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method three-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-3shot-cot-post-kor-D_multiarith-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method zs-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-zs-cot-post-kor-D_single_eq-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method os-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-1shot-cot-post-kor-D_single_eq-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-zs.json \
--method three-cot-post \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/no-peft-3shot-cot-post-kor-D_single_eq-test.json


