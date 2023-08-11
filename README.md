# kt-ai-challenge
## 개요
https://aifactory.space/task/2528/overview  
[결선] 2023 AI(인공지능) 대학원 챌린지 with kt 믿:음 / xfact팀
### 주제
* 설명가능 하고, 개인 맞춤 가능한 멀티 홉 질의응답 (Explainable and Customizable Multi-hop Question Answering)
![image](https://github.com/xfactlab/kt-ai-challenge/assets/18394356/2f123062-e550-4fbc-a418-d5099da9d92a)
### Demo
![image](https://github.com/xfactlab/kt-ai-challenge/assets/18394356/847f8f58-0570-4771-aa94-2da02454ef8e)
### Video
https://youtu.be/K9_glUcdj1E 
### Folder Descriptions
#### data 
- `data` directory contains datasets used for training/inference on KT'S 믿:음 
- For further details and descriptions, check out README.md in `data` directory
#### frontend 
- `frontend` directory contains scripts and codes used for Demo.
- For further details and descriptions, check out README.md in `frontend` directory
#### src
- `src` directory contains utility functions for calling apis/files.
### Script Descriptions
- kt-evaluate-api.py : evaluation script for default/trained KT믿:음 models on reasoning dataset 
- reasoning_api.py : reasoning script for adding rationales behind the answer using LLM apis
- translate_api.py : translation script from English to Korean using LLM apis
## License
Apache 2.0 license
