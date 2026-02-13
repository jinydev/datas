# 04_missing_values.py
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
df = sns.load_dataset('titanic')

# 1. 결측치 현황 시각화 (Simple Heatmap)
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# 4. 결측치가 너무 많은 컬럼 삭제 ('deck')
print(f"Deck 컬럼 결측 비율: {df['deck'].isnull().mean():.2f}")
df = df.drop('deck', axis=1)

# 12. 최빈값 대치 (Embarked)
# 2개 밖에 없으므로 가장 많이 나온 값으로 채움
most_freq_port = df['embarked'].mode()[0]
df['embarked'] = df['embarked'].fillna(most_freq_port)
print(f"임박 항구 결측치를 '{most_freq_port}'로 채웠습니다.")

# 7. 그룹별 대치법 (나이)
# 평균 대치 전 나이 분포 저장
age_before = df['age'].dropna()

# 호칭은 없지만 성별/등급별로 나이를 추정해봅시다.
# pclass와 sex 그룹별 평균 나이 확인
print("\n=== 그룹별 평균 나이 ===")
print(df.groupby(['pclass', 'sex'])['age'].mean())

# transform을 이용해 채우기
df['age'] = df['age'].fillna(df.groupby(['pclass', 'sex'])['age'].transform('mean'))

# 15. 대치 전후 분포 비교
plt.figure(figsize=(10, 5))
sns.kdeplot(age_before, label='Before Imputation', shade=True, color='blue')
sns.kdeplot(df['age'], label='After Imputation', shade=True, color='red')
plt.title("Age Distribution Comparison")
plt.legend()
plt.show()

# 최종 확인
print("\n=== 최종 결측치 확인 ===")
print(df.isnull().sum())
