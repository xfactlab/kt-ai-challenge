#!/bin/bash

 python peft2-api.py \
 --api_path /userhomes/philhoon/kt-ai-challenge/api-peft2.json \
 --input_file /userhomes/philhoon/kt-ai-challenge/result/kor-gsm8k-peft2-test.jsonl \
 --output_path /userhomes/philhoon/kt-ai-challenge/result \
 --output_file_name peft2-result-ko-gsm8k-test.jsonl

