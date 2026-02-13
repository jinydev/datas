# 03_numerical_eda.py
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
df = sns.load_dataset('titanic')

# 2. 히스토그램 (나이 분포)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
# hue='survived'를 추가하여 생존자/사망자 분포 비교
sns.histplot(x='age', hue='survived', data=df, kde=True, element="step")
plt.title("Age Distribution by Survival")

# 9. 히스토그램 (요금 분포)
plt.subplot(1, 2, 2)
sns.histplot(x='fare', data=df, color='green', bins=40)
plt.title("Fare Distribution")
plt.xlim(0, 300) # 너무 큰 이상치는 화면에서 잘라냄

plt.tight_layout()
plt.show()

# 6. 박스플롯 (등급별 나이 분포)
plt.figure(figsize=(8, 5))
sns.boxplot(x='pclass', y='age', data=df)
plt.title("Age Distribution by Pclass")
plt.show()

# 8. 바이올린 플롯 (성별 나이 분포)
plt.figure(figsize=(8, 5))
sns.violinplot(x='sex', y='age', hue='survived', data=df, split=True)
plt.title("Age Distribution by Sex (Violin Plot)")
plt.show()

# 11. 상관관계 히트맵
plt.figure(figsize=(6, 5))
# 수치형 컬럼만 선택하여 상관계수 계산
numeric_cols = df.select_dtypes(include=['float64', 'int64'])
corr = numeric_cols.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
