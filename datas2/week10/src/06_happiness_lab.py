import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 가상의 행복 데이터 생성
data = {
    'Country': ['Finland', 'Denmark', 'Norway', 'USA', 'Korea', 'China', 'Japan', 'Afghanistan'],
    'Continent': ['Europe', 'Europe', 'Europe', 'America', 'Asia', 'Asia', 'Asia', 'Asia'],
    'Score': [7.8, 7.6, 7.5, 6.9, 5.9, 5.1, 5.8, 2.5],
    'GDP': [1.3, 1.2, 1.4, 1.5, 1.0, 0.9, 1.1, 0.3]
}
df = pd.DataFrame(data)

# 미션 1: Top 5
print("=== Top 5 Happy Countries ===")
print(df.sort_values(by='Score', ascending=False).head(5))

# 미션 2: 상관관계
corr = df['GDP'].corr(df['Score'])
print(f"\nGDP vs Score Correlation: {corr:.2f}")

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='GDP', y='Score', hue='Continent', s=200)
for i in range(len(df)): # 나라 이름 써주기
    plt.text(df['GDP'][i]+0.02, df['Score'][i], df['Country'][i])
plt.title("Money vs Happiness")
plt.show()

# 미션 3: 대륙별 비교
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='Continent', y='Score')
plt.title("Happiness by Continent")
plt.show()
