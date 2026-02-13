# 01_timeseries_intro.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# 1. 시계열 데이터 생성
# 2023-01-01부터 365일간의 데이트
dates = pd.date_range(start='2023-01-01', periods=365, freq='D')
# 추세(Trend) + 계절성(Seasonality) + 노이즈(Noise)
trend = np.linspace(0, 100, 365) # 우상향
seasonality = 10 * np.sin(np.linspace(0, 3.14 * 12, 365)) # 월 1회 주기
noise = np.random.normal(0, 2, 365)
values = trend + seasonality + noise

df = pd.DataFrame({'Date': dates, 'Value': values})
# Datetime Index 설정 (필수)
df.set_index('Date', inplace=True)

print("=== 데이터 확인 ===")
print(df.head())

# 2. 시각화
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['Value'], label='Original')
plt.title('Synthesized Time Series Data')
plt.legend()
plt.show()

# 3. 이동 평균 (Rolling Mean) - 추세 파악
df['MA7'] = df['Value'].rolling(window=7).mean()   # 7일 이동평균
df['MA30'] = df['Value'].rolling(window=30).mean() # 30일 이동평균

plt.figure(figsize=(12, 5))
plt.plot(df.index, df['Value'], label='Original', alpha=0.5)
plt.plot(df.index, df['MA7'], label='7 Days MA', linewidth=2)
plt.plot(df.index, df['MA30'], label='30 Days MA', linewidth=2, color='red')
plt.title('Moving Average')
plt.legend()
plt.show()

# 4. 시계열 분해 (Decomposition)
# model='additive' (가법 모델), freq=30 (주기 설정)
# statsmodels 라이브러리 필요
result = seasonal_decompose(df['Value'], model='additive', period=30)

plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(result.observed)
plt.ylabel('Observed')

plt.subplot(4, 1, 2)
plt.plot(result.trend)
plt.ylabel('Trend')

plt.subplot(4, 1, 3)
plt.plot(result.seasonal)
plt.ylabel('Seasonal')

plt.subplot(4, 1, 4)
plt.plot(result.resid)
plt.ylabel('Residual')
plt.tight_layout()
plt.show()

# 5. 자기상관 (ACF) - 주기성 확인
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(df['Value'], lags=50, ax=ax[0])
plot_pacf(df['Value'], lags=50, ax=ax[1])
plt.show()
