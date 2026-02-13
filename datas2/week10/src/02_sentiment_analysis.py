# 02_sentiment_analysis.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# 1. 데이터 준비 (네이버 영화 리뷰 데이터셋 URL)
# 실제로는 다운로드 받아서 로드해야 함. 여기서는 데모용 간단 데이터 리스트 생성
train_data = [
    ("이 영화 진짜 재밌다 인생 영화임", 1),
    ("너무 지루하고 잠만 잤음", 0),
    ("배우들 연기가 대박이다 꼭 봐라", 1),
    ("돈 아깝다 시간이 멈루는 줄", 0),
    ("스토리가 엉망진창 개연성 없음", 0),
    ("감동적이고 눈물 콧물 다 뺐다 ㅠㅠ", 1),
    ("그냥 그래요 쏘쏘", 0),
    ("연출이 미쳤다 영상미 최고", 1),
    ("핵노잼 비추", 0),
    ("올해 최고의 영화", 1)
] 
# 실제 데이터라면 pd.read_table('ratings_train.txt') 사용

df = pd.DataFrame(train_data, columns=['document', 'label'])
print("=== 데이터 확인 ===")
print(df.head())

X = df['document']
y = df['label']

# 2. 한국어 형태소 분석 함수 (KoNLPy)
# 데모 환경에선 KoNLPy가 없을 수 있으므로, 
# 간단히 공백 기준으로 자르는 토크나이저를 정의해서 사용 (실제론 Okt 추천)
def simple_tokenizer(text):
    return text.split()

# 3. 파이프라인 (TF-IDF -> 로지스틱 회귀)
# tokenizer에 Okt.morphs 를 넣으면 됨
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(tokenizer=simple_tokenizer, token_pattern=None)), 
    ('clf', LogisticRegression(random_state=42))
])

# 4. 학습
pipeline.fit(X, y)

# 5. 예측 테스트
test_reviews = [
    "정말 재미있는 영화였습니다 추천해요",
    "최악의 영화... 돈 버림"
]
pred = pipeline.predict(test_reviews)
pred_proba = pipeline.predict_proba(test_reviews)

print("\n=== 예측 결과 ===")
for i, review in enumerate(test_reviews):
    label = "긍정" if pred[i] == 1 else "부정"
    score = pred_proba[i][1] if pred[i] == 1 else pred_proba[i][0]
    print(f"리뷰: {review} -> {label} ({score*100:.1f}%)")

# 6. 모델이 학습한 단어 가중치 확인
# 실제 데이터가 많을 때 의미가 있음
vectorizer = pipeline.named_steps['tfidf']
model = pipeline.named_steps['clf']

coefs = pd.Series(model.coef_[0], index=vectorizer.get_feature_names_out())
print("\n=== 긍정 키워드 Top 3 ===")
print(coefs.sort_values(ascending=False).head(3))
print("\n=== 부정 키워드 Top 3 ===")
print(coefs.sort_values(ascending=True).head(3))
