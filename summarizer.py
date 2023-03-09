# summarizer.py

import re
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from konlpy.tag import Okt

# BERT 모델 및 토크나이저 로딩
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=2)
model.load_state_dict(torch.load('saved_model.pth', map_location=torch.device('cpu')))
model.eval()

# 텍스트 전처리 및 BERT 모델을 이용한 텍스트 요약
def summarize_texts(article_titles):
    okt = Okt()
    preprocessed_texts = []
    for title in article_titles:
        # 한글과 공백을 제외한 문자 모두 제거
        title = re.sub('[^ㄱ-ㅣ가-힣 ]', '', title)
        # 명사 추출 및 토큰화
        nouns = okt.nouns(title)
        tokens = [noun for noun in nouns if len(noun) > 1]
        preprocessed_texts.append(' '.join(tokens))

    summarized_texts = []
    for text in preprocessed_texts:
        # 토크나이즈
        inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
        # 모델 예측
        outputs = model(**inputs)
        logits = outputs[0]
        # 문장 분류
        if logits[0] > logits[1]:
            summarized_texts.append(text)
        else:
            summarized_texts.append('')
    return summarized_texts
