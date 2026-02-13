# 02_categorical_eda.py
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
df = sns.load_dataset('titanic')

# 스타일 설정
sns.set_theme(style="whitegrid")

# 1. 화면 분할 (Subplots)
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 4. 성별과 생존 (첫 번째 그래프)
sns.countplot(ax=axes[0], x='sex', hue='survived', data=df)
axes[0].set_title('Survival by Sex')

# 6. 등급과 생존 (두 번째 그래프)
sns.countplot(ax=axes[1], x='pclass', hue='survived', data=df, palette='viridis')
axes[1].set_title('Survival by Pclass')

# 9. 항구와 생존 (세 번째 그래프)
sns.countplot(ax=axes[2], x='embarked', hue='survived', data=df, palette='pastel')
axes[2].set_title('Survival by Embarked')

plt.show()

# 7. 교차표 (정확한 수치 확인)
print("\n=== 성별 생존 교차표 ===")
print(pd.crosstab(df['sex'], df['survived'], margins=True))

print("\n=== 등급별 생존 비율 (Normalize) ===")
# 행(index) 기준으로 비율 계산 (합이 1)
print(pd.crosstab(df['pclass'], df['survived'], normalize='index'))
