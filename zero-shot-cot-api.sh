#!/bin/bash

python zero-shot-cot-api.py \
--api_path /userhomes/philhoon/kt-ai-challenge/api.json \
--input_file /userhomes/philhoon/kt-ai-challenge/data/openai-gpt-3.5-turbo-0301-2048-0.0-KOR-gsm8k-test.jsonl \
--output_path /userhomes/philhoon/kt-ai-challenge/result \
--output_file_name zero-shot-cot-result-ko-gsm8k-test.jsonl

