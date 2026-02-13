import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Pandas & Numpy 핵심 복습
# 가상의 쇼핑몰 데이터 생성
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03'],
    'Product': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana'],
    'Sales': [1000, 500, 1200, 800, 600],
    'Quantity': [5, 10, 6, 8, 12]
}

df = pd.DataFrame(data)
print("=== 원본 데이터 ===")
print(df)

# 2. [응용 예제] 매출 분석
print("\n=== 상품별 총 매출 (Groupby) ===")
# 상품별로 묶어서 Sales의 합계를 구함
total_sales = df.groupby('Product')['Sales'].sum()
print(total_sales)

print("\n=== 가장 많이 팔린 상품 (Sort) ===")
# 매출 순으로 정렬
sorted_sales = total_sales.sort_values(ascending=False)
print(sorted_sales)

# 시각화
plt.figure(figsize=(6, 4))
plt.bar(sorted_sales.index, sorted_sales.values, color=['red', 'orange', 'yellow'])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.show()
