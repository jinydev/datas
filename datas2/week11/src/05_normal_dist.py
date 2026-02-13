import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 생성 (평균 170, 표준편차 5, 1000명)
heights = np.random.normal(loc=170, scale=5, size=1000)

print("=== 기초 통계 ===")
print(f"평균 키: {np.mean(heights):.2f}cm")
print(f"최소 키: {np.min(heights):.2f}cm")
print(f"최대 키: {np.max(heights):.2f}cm")

# 2. 시각화 (히스토그램 + 밀도 그래프)
plt.figure(figsize=(8, 5))
# kde=True: 부드러운 곡선도 같이 그려줌
sns.histplot(heights, kde=True, color='skyblue', bins=30)
plt.title("Height Distribution (Normal)")
plt.xlabel("Height (cm)")
plt.axvline(170, color='red', linestyle='--', label='Mean (170)')
plt.legend()
plt.show()
