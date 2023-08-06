#!/bin/bash

python openai_translate_reasoning_api.py \
--api openai \
--api_key_file /userhomes/philhoon/kt-ai-challenge/api-openai.yaml \
--model_name gpt-3.5-turbo-0613 \
--max_token 2048 \
--temperature 0 \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/D_multiarith.json \
--output_path /userhomes/philhoon/kt-ai-challenge/eng_data

python openai_translate_reasoning_api.py \
--api openai \
--api_key_file /userhomes/philhoon/kt-ai-challenge/api-openai.yaml \
--model_name gpt-3.5-turbo-0613 \
--max_token 2048 \
--temperature 0 \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/D_addsub.json \
--output_path /userhomes/philhoon/kt-ai-challenge/eng_data

python openai_translate_reasoning_api.py \
--api openai \
--api_key_file /userhomes/philhoon/kt-ai-challenge/api-openai.yaml \
--model_name gpt-3.5-turbo-0613 \
--max_token 2048 \
--temperature 0 \
--input_file /userhomes/philhoon/kt-ai-challenge/eng_data/D_single_eq.json \
--output_path /userhomes/philhoon/kt-ai-challenge/eng_data

