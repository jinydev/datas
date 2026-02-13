# pip install yfinance 가 필요합니다.
import yfinance as yf
import matplotlib.pyplot as plt

# 1. 데이터 다운로드 (애플, 테슬라)
# 기간: 2023년 1월 1일 ~ 현재
aapl = yf.download("AAPL", start="2023-01-01", end="2023-12-31")
tsla = yf.download("TSLA", start="2023-01-01", end="2023-12-31")

print(aapl.head())

# 2. 종가(Close) 비교 그래프
plt.figure(figsize=(10, 5))
plt.plot(aapl.index, aapl['Close'], label='Apple')
plt.plot(tsla.index, tsla['Close'], label='Tesla', color='red')
plt.title("Stock Price Analysis (2023)")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()

# 3. 수익률 비교 (Normalized)
# 시작 가격을 100으로 맞추면 비교하기 쉽습니다.
aapl_norm = aapl['Close'] / aapl['Close'].iloc[0] * 100
tsla_norm = tsla['Close'] / tsla['Close'].iloc[0] * 100

plt.figure(figsize=(10, 5))
plt.plot(aapl_norm, label='Apple (Normalized)')
plt.plot(tsla_norm, label='Tesla (Normalized)', color='red')
plt.title("Stock Return Rate Analysis")
plt.legend()
plt.show()
