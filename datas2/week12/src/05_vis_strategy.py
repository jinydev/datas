import seaborn as sns
import matplotlib.pyplot as plt

# 데이터: 요일별 팁 금액
tips = sns.load_dataset('tips')

plt.figure(figsize=(15, 5))

# 1. Line Plot (추세?) - 요일은 순서가 있어서 나쁘지 않음
plt.subplot(1, 3, 1)
sns.lineplot(data=tips, x='day', y='total_bill', ci=None)
plt.title("Line Plot (Trend)")

# 2. Bar Plot (비교) - 평균 금액 비교할 때 좋음
plt.subplot(1, 3, 2)
sns.barplot(data=tips, x='day', y='total_bill', ci=None, palette='Pastel1')
plt.title("Bar Plot (Comparison)")

# 3. Box Plot (분포) - 데이터가 퍼진 정도까지 볼 때 최고
plt.subplot(1, 3, 3)
sns.boxplot(data=tips, x='day', y='total_bill', palette='Set3')
plt.title("Box Plot (Distribution)")

plt.tight_layout()
plt.show()

print("결론: 요일별 금액 분포를 보려면 Box Plot이 가장 정보량이 많습니다.")
