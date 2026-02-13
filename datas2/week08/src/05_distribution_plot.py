import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# 1. Boxplot
# 요일(day)별로 팁(tip)의 가격 분포 보기
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x='day', y='tip')
plt.title("Tip Distribution by Day (Box)")
plt.show()

# 2. Violinplot
# 모양이 바이올린을 닮아서 이름이 이렇게 붙었습니다.
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x='day', y='tip', palette='muted')
plt.title("Tip Distribution by Day (Violin)")
plt.show()

# 3. [응용] 흡연자 vs 비흡연자 팁 분포
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x='day', y='tip', hue='smoker')
plt.title("Tip Distribution by Smoker")
plt.show()
