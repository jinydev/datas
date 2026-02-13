# 02_stock_prediction.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.metrics import mean_squared_error

# 1. 데이터 수집 (Apple 주식)
# 2020년부터 현재까지
print("Downloading data...")
# yfinance 설치 필요: pip install yfinance
# 실습 환경에 따라 데이터가 안 받아질 경우 CSV 로드 대체
try:
    df = yf.download('AAPL', start='2020-01-01', end='2023-12-31')
except:
    print("인터넷 연결을 확인하세요.")
    # 데모용 데이터 생성
    dates = pd.date_range('2020-01-01', '2023-12-31')
    df = pd.DataFrame(np.random.randn(len(dates)).cumsum() + 100, index=dates, columns=['Close'])

print(df.head())

# 2. 데이터 분리 (Time Split)
train_data = df[:'2022-12-31']['Close']
test_data = df['2023-01-01':]['Close']

plt.figure(figsize=(12, 6))
plt.plot(train_data, label='Train')
plt.plot(test_data, label='Test')
plt.title('AAPL Stock Price')
plt.legend()
plt.show()

# 3. ARIMA 모델링 (pmdarima 없을 경우 statsmodels로 간단 구현)
# pip install pmdarima
from statsmodels.tsa.arima.model import ARIMA

print("\nFitting ARIMA model...")
# (p, d, q) = (5, 1, 0) : 과거 5일치 보고, 1차 차분 사용
model = ARIMA(train_data, order=(5, 1, 0))
model_fit = model.fit()
print(model_fit.summary())

# 4. 예측
forecast_steps = len(test_data)
forecast = model_fit.forecast(steps=forecast_steps)
# forecast는 Series 형태

# 5. 결과 시각화
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, test_data, label='Actual')
plt.plot(test_data.index, forecast, label='Forecast', color='red')
plt.title('ARIMA Prediction vs Actual')
plt.legend()
plt.show()

# 6. 평가 (RMSE)
rmse = np.sqrt(mean_squared_error(test_data, forecast))
print(f"RMSE: {rmse:.2f}")

# 7. 볼린저 밴드 그리기 (보조지표)
df['MA20'] = df['Close'].rolling(window=20).mean()
df['Std20'] = df['Close'].rolling(window=20).std()
df['Upper'] = df['MA20'] + (df['Std20'] * 2)
df['Lower'] = df['MA20'] - (df['Std20'] * 2)

plt.figure(figsize=(12, 6))
# 최근 1년만 확대
recent = df['2023':]
plt.plot(recent.index, recent['Close'], label='Close')
plt.plot(recent.index, recent['Upper'], 'g--', label='Upper Band')
plt.plot(recent.index, recent['Lower'], 'g--', label='Lower Band')
plt.fill_between(recent.index, recent['Upper'], recent['Lower'], color='gray', alpha=0.1)
plt.title('Bollinger Bands (2023)')
plt.legend()
plt.show()
