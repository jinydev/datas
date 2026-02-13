# 01_titanic_intro.py
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 4. 분석 환경 준비 (내장 데이터 로드)
print("타이타닉 데이터를 로드합니다...")
df = sns.load_dataset('titanic')

# 5. 데이터 첫인상 확인
print("\n=== 상위 5개 데이터 ===")
print(df.head())

print("\n=== 데이터 정보 (Info) ===")
# 결측치 현황 파악 (age, deck 등)
df.info()

print("\n=== 통계적 요약 ===")
print(df.describe())

# 9. 범주형 데이터 기초 분석 (성별 생존자 수)
print("\n=== 성별 생존자 수 ===")
print(df.groupby('sex')['survived'].sum())

# 10. 수치형 데이터 기초 분포 (나이)
plt.figure(figsize=(8, 5))
sns.histplot(df['age'].dropna(), bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.show()

print("\n준비 완료. 본격적인 EDA를 시작합니다.")
