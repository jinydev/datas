# 03_data_manipulation.py
import pandas as pd

# 샘플 데이터: 쇼핑몰 주문 내역
data = {
    '주문일자': ['2023-01-01', '2023-01-02', '2023-01-05', '2023-02-10'],
    '구매금액': [50000, 150000, 30000, 200000],
    '고객등급': ['Silver', 'Gold', 'Silver', 'VIP'] # 현재 등급
}
df = pd.DataFrame(data)

print("=== 원본 데이터 ===")
print(df)

# 13. 날짜형 변환
df['주문일자'] = pd.to_datetime(df['주문일자'])

# 14. 날짜 정보 추출 (파생 변수 생성 1)
df['월'] = df['주문일자'].dt.month
df['요일'] = df['주문일자'].dt.day_name()

# 3. 사칙연산 파생 변수 생성 2 (포인트 적립)
# 구매금액의 1%를 포인트로 적립
df['보너스포인트'] = df['구매금액'] * 0.01

# 5. apply() 함수 사용 (조건부 로직)
def classify_vip(amount):
    if amount >= 100000:
        return "High Value"
    else:
        return "Normal"

df['구매유형'] = df['구매금액'].apply(classify_vip)

# 11. 컬럼 이름 변경
df = df.rename(columns={'구매금액': '금액'})

# 8. 필요 없는 컬럼 삭제 (고객등급 컬럼 삭제)
# axis=1 은 열 방향
df_dropped = df.drop('고객등급', axis=1)

print("\n=== 가공 후 데이터 ===")
print(df_dropped)
print("\n=== 컬럼별 타입 확인 ===")
print(df_dropped.dtypes)
