import yfinance as yf
import matplotlib.pyplot as plt

# 1. 데이터 가져오기
btc = yf.download("BTC-USD", start="2020-01-01")

# 2. 최고점 날짜 찾기
max_price = btc['Close'].max()
max_date = btc['Close'].idxmax()
print(f"역대 최고가: {max_price:.2f}달러 ({max_date.date()})")

# 3. 수익률 비교 (2020년 투자 vs 2021년 투자)
price_2020 = btc.loc['2020-01-01']['Close']
price_2021 = btc.loc['2021-01-01']['Close']
current_price = btc['Close'].iloc[-1] # 가장 최근 가격

profit_2020 = (current_price - price_2020) / price_2020 * 100
profit_2021 = (current_price - price_2021) / price_2021 * 100

print(f"2020년 존버 수익률: {profit_2020:.2f}%")
print(f"2021년 존버 수익률: {profit_2021:.2f}%")

# 시각화
plt.figure(figsize=(10, 5))
plt.plot(btc['Close'], label='BTC Price')
plt.scatter(max_date, max_price, color='red', s=100, label='Max Price')
plt.title("Bitcoin Price History")
plt.legend()
plt.show()
