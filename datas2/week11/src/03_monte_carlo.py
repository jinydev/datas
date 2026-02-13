import numpy as np
import matplotlib.pyplot as plt

# 점 개수
n = 10000

# 1. 정사각형 안에 랜덤 점 찍기 (-1 ~ 1 사이)
x = np.random.uniform(-1, 1, n)
y = np.random.uniform(-1, 1, n)

# 2. 원점에서의 거리 계산 (피타고라스 정리)
dist = np.sqrt(x**2 + y**2)

# 3. 원 안에 들어온 점 (거리가 1 이하)
inside = dist <= 1
n_inside = np.sum(inside)

# 4. 파이 추정 (사각형 넓이 4 * 비율)
pi_estimate = 4 * n_inside / n
print(f"Estimated Pi: {pi_estimate}")

# 5. 시각화
plt.figure(figsize=(5, 5))
plt.scatter(x[inside], y[inside], color='blue', s=1)
plt.scatter(x[~inside], y[~inside], color='red', s=1)
plt.title(f"Monte Carlo Pi (n={n})")
plt.show()
