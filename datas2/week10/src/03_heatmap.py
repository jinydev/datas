import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 가상의 성적 데이터
data = {
    'Korean': [90, 80, 70, 60, 95],
    'English': [85, 90, 75, 50, 90],
    'Math': [100, 60, 50, 40, 95],
    'Music': [70, 70, 80, 90, 60],
    'Art': [60, 50, 90, 80, 50]
}
df = pd.DataFrame(data)

# 1. 히트맵 그리기
plt.figure(figsize=(8, 6))
# vmin=-1, vmax=1 : 색상 범위를 -1 ~ 1로 고정 (중요!)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

# 2. Clustermap (끼리끼리 묶어주기)
# 비슷한 패턴을 가진 변수끼리 옆으로 모아주는 기능입니다.
sns.clustermap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()
