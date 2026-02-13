# 01_text_mining_intro.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud

# 1. 간단한 문서 데이터
documents = [
    "I love deep learning and python",
    "Python is a great language for data science",
    "I dislike rainy days but I love python",
    "Deep learning is amazing"
]

# 2. Count Vectorizer (BoW)
print("=== Count Vectorizer (빈도수) ===")
vectorizer = CountVectorizer(stop_words='english')
dtm = vectorizer.fit_transform(documents)
# 단어 사전
print("단어 사전:", vectorizer.get_feature_names_out())
# 문서-단어 행렬
print(dtm.toarray())

# 3. TF-IDF Vectorizer (가중치)
print("\n=== TF-IDF Vectorizer ===")
tfidf_vec = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vec.fit_transform(documents)
# DataFrame으로 보기 좋게 출력
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vec.get_feature_names_out())
print(df_tfidf.round(2))

# 4. 코사인 유사도
print("\n=== 문서 간 유사도 (Cosine Similarity) ===")
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
print("문서1과 문서2의 유사도:", similarity[0, 1])
print("문서1과 문서3의 유사도:", similarity[0, 2]) # 둘 다 love python이 있어서 높게 나옴

# 5. 워드 클라우드 시각화
print("\n=== 워드 클라우드 생성 ===")
text_all = " ".join(documents)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_all)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Simple WordCloud')
plt.show()

# 6. 한국어 형태소 분석 (KoNLPy) 예제
# 실행하려면 KoNLPy와 JDK가 설치되어 있어야 합니다.
# 설치 안 된 환경을 대비해 try-except 처리
try:
    from konlpy.tag import Okt
    okt = Okt()
    korean_text = "아버지가 방에 들어가신다."
    print("\n=== 한국어 형태소 분석 ===")
    print("원문:", korean_text)
    print("형태소:", okt.morphs(korean_text))
    print("명사:", okt.nouns(korean_text))
except ImportError:
    print("\n[알림] KoNLPy가 설치되지 않아 한국어 실습은 생략합니다.")
