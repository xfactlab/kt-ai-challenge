#!/bin/bash

#python peft3-math5-os-cot-api.py \
#--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
#--method zs \
#--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
#--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-zs-kor-D_addsub-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method zs-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-zs-cot-kor-D_addsub-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method os-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-1shot-cot-kor-D_addsub-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method three-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_addsub-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-3shot-cot-kor-D_addsub-test.json


#python peft3-math5-os-cot-api.py \
#--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
#--method zs \
#--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
#--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-zs-kor-D_multiarith-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method zs-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-zs-cot-kor-D_multiarith-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method os-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-1shot-cot-kor-D_multiarith-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method three-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_multiarith-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-3shot-cot-kor-D_multiarith-test.json

#python peft3-math5-os-cot-api.py \
#--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
#--method zs \
#--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
#--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-zs-kor-D_single_eq-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method zs-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-zs-cot-kor-D_single_eq-test.json

python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method os-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-1shot-cot-kor-D_single_eq-test.json


python peft3-math5-os-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft4.json \
--method three-cot \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/kor-D_single_eq-test.json \
--output_path /userhomes/philhoon/kt-ai-challenge/result/peft4-3shot-cot-kor-D_single_eq-test.json


