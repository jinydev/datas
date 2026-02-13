import pandas as pd

# 1. 문자열을 날짜로 변환
dates = ['2023-01-01', '2023-12-25', '2024-05-05']
dt_dates = pd.to_datetime(dates)

print(dt_dates)

# 2. 정보 추출
print("연도:", dt_dates.year)
print("월:", dt_dates.month)
print("요일:", dt_dates.day_name())

# 3. [응용 예제] 생일 요일 찾기
my_birthday = "1995-10-20" # 예시 날짜
bdb = pd.to_datetime(my_birthday)
print(f"내 생일 {my_birthday}은 {bdb.day_name()}입니다.")

# 4. 날짜 계산 (10000일 살아보기)
from datetime import timedelta
future_10000 = bdb + timedelta(days=10000)
print(f"내가 태어난지 10000일 되는 날은 {future_10000}입니다.")
