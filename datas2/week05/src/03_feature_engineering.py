# 03_feature_engineering.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
df = sns.load_dataset('titanic')

# 1. 구간화 (Binning) - 나이대
# 0~10세, 10~20세 ... 
# labels를 지정하면 숫자가 아닌 문자로 반환됨
df['age_bin'] = pd.cut(df['age'], bins=[0, 10, 20, 40, 60, 100], labels=['Child', 'Teen', 'Adult', 'Middle', 'Senior'])
print("=== Age Binning 결과 ===")
print(df[['age', 'age_bin']].head(10))

# 2. 교호작용 (Family Size)
df['family_size'] = df['sibsp'] + df['parch'] + 1
print("\n=== Family Size ===")
print(df[['sibsp', 'parch', 'family_size']].head())

# 3. 문자열 처리 (Title 추출)
# 정규표현식을 이용한 호칭 추출
# ([A-Za-z]+)\. : 알파벳으로 시작해서 점(.)으로 끝나는 단어 추출
df['title'] = df['name'].str.extract(' ([A-Za-z]+)\.', expand=False)
print("\n=== 호칭 추출 결과 ===")
print(df['title'].value_counts())

# 4. 희소 범주 묶기 (Rare Label)
# Title 간소화 (Mr, Miss, Mrs, Master 제외하고 모두 'Others'로)
major_titles = ['Mr', 'Miss', 'Mrs', 'Master']
df['title_clean'] = df['title'].apply(lambda x: x if x in major_titles else 'Others')
print("\n=== 호칭 간소화 후 ===")
print(df['title_clean'].value_counts())

# 5. 시각화: 새로운 변수와 생존율
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 나이 구간별 생존율
sns.barplot(data=df, x='age_bin', y='survived', ax=axes[0], palette='pastel')
axes[0].set_title('Survival by Age Bin')

# 호칭별 생존율
sns.barplot(data=df, x='title_clean', y='survived', ax=axes[1], palette='deep')
axes[1].set_title('Survival by Title')

plt.tight_layout()
plt.show()

# 6. 다항 피처 (Polynomial) - Scikit-Learn 활용
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# 예시: 나이와 요금의 상호작용
poly = PolynomialFeatures(degree=2, include_bias=False)
features = df[['age', 'fare']].dropna() # 결측치 있으면 안됨
poly_features = poly.fit_transform(features)

print("\n=== 다항 피처 생성 (Age, Fare) ===")
print("Features: Age, Fare")
print("Poly Features: Age, Fare, Age^2, Age*Fare, Fare^2")
print(poly_features[:2])
# 이렇게 늘어난 변수는 회귀 분석의 설명력을 높여줄 수 있습니다.
