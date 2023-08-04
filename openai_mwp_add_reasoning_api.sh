#!/bin/bash

python openai_mwp_add_reasoning_api.py \
--api_key_file /userhomes/philhoon/kt-ai-challenge/api-openai.yaml \
--model_name gpt-3.5-turbo-0613 \
--max_token 2048 \
--temperature 0 \
--input_file /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_preprocess.jsonl \
--output_path /userhomes/philhoon/kt-ai-challenge/data/public_mwp_data_v2_reasoning.jsonl

