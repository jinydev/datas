import seaborn as sns
import matplotlib.pyplot as plt

# 1. 예제 데이터 불러오기 (Tips)
tips = sns.load_dataset('tips')
print(tips.head())

# 2. 산점도 그리기
plt.figure(figsize=(6, 4))
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title("Total Bill vs Tip")
plt.show()

# 3. 그룹별 색상 나누기 (hue)
# 성별(sex)에 따라 색깔을 다르게
plt.figure(figsize=(6, 4))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.title("Bill vs Tip by Sex")
plt.show()

# 4. 점 크기(size)와 스타일(style)로도 정보 표현 가능
plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='time', size='size')
plt.title("Complex Scatter Plot")
plt.show()
