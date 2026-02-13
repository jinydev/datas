# 05_correlation.py
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
df = sns.load_dataset('titanic')

# 9. 범주형 변수 수치화 (상관분석을 위해)
# 남성: 0, 여성: 1로 변환
df['sex_code'] = df['sex'].map({'male': 0, 'female': 1})

# Embarked도 수치화 (C:0, Q:1, S:2) 임시 변환
df['embarked_code'] = df['embarked'].astype('category').cat.codes

# 4. 상관계수 행렬 계산
# 수치형 데이터만 선택
numeric_df = df.select_dtypes(include=['number']) # float, int 모두 포함
corr_matrix = numeric_df.corr()

# 5. 상관관계 히트맵
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title("Titanic Correlation Matrix")
plt.show()

# 17. 실습: 생존과의 상관계수 순위 시각화
plt.figure(figsize=(8, 6))
# 생존 열과의 상관계수만 추출, 절댓값 기준으로 정렬
corr_target = corr_matrix['survived'].drop('survived') # 자기 자신 제외
corr_target.sort_values(ascending=False).plot(kind='barh', color='teal')
plt.title("Correlation with 'Survived'")
plt.xlabel("Correlation Coefficient (Pearson r)")
plt.axvline(0, color='gray', linestyle='--')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()

# 10. Pairplot (주요 변수만)
# 시간이 오래 걸릴 수 있으므로 샘플링하거나 변수를 줄임
cols = ['survived', 'pclass', 'age', 'fare', 'family_size']
# 파생변수 생성 (가족 수)
df['family_size'] = df['sibsp'] + df['parch']
sns.pairplot(df[['survived', 'pclass', 'age', 'fare', 'family_size']], hue='survived', palette='husl')
plt.show()
