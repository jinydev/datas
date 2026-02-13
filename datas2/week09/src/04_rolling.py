import yfinance as yf
import matplotlib.pyplot as plt

# 데이터 준비
df = yf.download("AAPL", start="2022-01-01", end="2023-12-31")

# 1. 이동평균선 계산
df['MA20'] = df['Close'].rolling(window=20).mean() # 단기
df['MA60'] = df['Close'].rolling(window=60).mean() # 중기

# 2. 시각화
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close', alpha=0.3) # 원본은 흐리게
plt.plot(df.index, df['MA20'], label='MA20 (Short)', color='orange')
plt.plot(df.index, df['MA60'], label='MA60 (Long)', color='blue')

plt.title("Apple Stock - Moving Average")
plt.legend()
plt.show()

# 3. [응용] 골든크로스 시점 (눈으로 확인해보기)
# 주황색 선이 파란색 선을 뚫고 올라가는 지점이 골든 크로스입니다.
