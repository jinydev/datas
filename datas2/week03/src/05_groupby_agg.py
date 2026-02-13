# 05_groupby_agg.py
import pandas as pd

# 샘플 데이터: 편의점 판매 기록
data = {
    '지점': ['강남점', '강남점', '강남점', '홍대점', '홍대점', '홍대점'],
    '요일': ['월', '화', '수', '월', '화', '수'],
    '상품': ['물', '커피', '물', '커피', '물', '커피'],
    '판매량': [10, 20, 15, 50, 30, 45],
    '매출': [10000, 40000, 15000, 100000, 30000, 90000]
}
df = pd.DataFrame(data)

print("=== 원본 데이터 ===")
print(df)

# 3. groupby 기본 (지점별 총 매출)
print("\n=== 지점별 총 매출 (sum) ===")
# 지점별로 묶어서 '매출' 열의 합계를 구함
branch_sales = df.groupby('지점')[['매출']].sum()
print(branch_sales)

# 6. 여러 함수 적용 (판매량은 합계, 매출은 평균)
print("\n=== 지점별 판매량 합계와 매출 평균 ===")
agg_res = df.groupby('지점').agg({
    '판매량': 'sum',
    '매출': 'mean'
})
print(agg_res)

# 5. 다중 그룹핑 (지점별 + 상품별 판매량)
print("\n=== 지점별+상품별 판매량 평균 ===")
multi_group = df.groupby(['지점', '상품'])[['판매량']].mean()
print(multi_group)

# 11. 피벗 테이블 (행: 지점, 열: 요일, 값: 매출)
print("\n=== 피벗 테이블 (요일별 매출) ===")
pivot = pd.pivot_table(df, index='지점', columns='요일', values='매출', aggfunc='sum')
# 요일 순서가 가나다순이라 뒤죽박죽일 수 있음 (나중에 정렬 필요)
print(pivot)

# 14. Transform (지점별 매출 평균을 원본 데이터 옆에 붙이기)
df['지점평균매출'] = df.groupby('지점')['매출'].transform('mean')
print("\n=== 지점평균매출 컬럼 추가 (Transform) ===")
print(df)
