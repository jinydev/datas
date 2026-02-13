import numpy as np
import matplotlib.pyplot as plt

# 1. 상관관계가 다른 데이터 생성
np.random.seed(0)

# 양의 상관관계 (r = 0.9)
x1 = np.random.rand(50)
y1 = x1 * 2 + np.random.normal(0, 0.1, 50)

# 음의 상관관계 (r = -0.9)
x2 = np.random.rand(50)
y2 = -x2 * 2 + np.random.normal(0, 0.1, 50)

# 무상관 (r = 0)
x3 = np.random.rand(50)
y3 = np.random.rand(50)

# 2. 시각화
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.scatter(x1, y1, color='blue')
plt.title("Positive Correlation (r ≈ 0.9)")

plt.subplot(1, 3, 2)
plt.scatter(x2, y2, color='red')
plt.title("Negative Correlation (r ≈ -0.9)")

plt.subplot(1, 3, 3)
plt.scatter(x3, y3, color='green')
plt.title("No Correlation (r ≈ 0)")

plt.tight_layout()
plt.show()
