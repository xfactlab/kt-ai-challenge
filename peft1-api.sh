#!/bin/bash

python peft1-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api-peft1.json \
--input_file /userhomes/philhoon/kt-ai-challenge/result/kor-gsm8k-peft1-test.jsonl \
--output_path /userhomes/philhoon/kt-ai-challenge/result \
--output_file_name peft1-result-ko-gsm8k-test.jsonl

