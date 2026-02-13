import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2023-01-01", end="2023-12-31")
df['MA20'] = df['Close'].rolling(window=20).mean()

# 상단선, 하단선 (표준편차 이용)
df['Upper'] = df['MA20'] + 10 # 대략 10달러 위
df['Lower'] = df['MA20'] - 10 # 대략 10달러 아래

plt.figure(figsize=(10, 5))

# 1. 메인 주가
plt.plot(df.index, df['Close'], label='Close', color='black')

# 2. 이동평균선
plt.plot(df.index, df['MA20'], label='MA20', linestyle='--')

# 3. 영역 채우기 (Upper와 Lower 사이를 칠해줌)
plt.fill_between(df.index, df['Lower'], df['Upper'], color='gray', alpha=0.2, label='Band')

plt.title("Stock Price with Band")
plt.legend()
plt.show()
