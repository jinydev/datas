import numpy as np
import matplotlib.pyplot as plt

# 1. 가상의 365일 데이터 생성
days = np.arange(365) # 0일 ~ 364일

# 2. 추세 (Trend): 시간이 갈수록 값이 커짐
trend = days * 0.1 

# 3. 계절성 (Seasonality): 사인 함수로 파동 만들기
season = np.sin(days * 0.1) * 5

# 4. 불규칙성 (Noise): 랜덤한 값
noise = np.random.randn(365) * 2

# 최종 시계열 데이터
data = trend + season + noise

plt.figure(figsize=(10, 4))
plt.plot(days, data)
plt.title("Synthetic Time Series (Trend + Season + Noise)")
plt.xlabel("Day")
plt.ylabel("Value")
plt.show()
