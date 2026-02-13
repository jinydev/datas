import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 가상의 매출 데이터 (Long Format)
data = {
    'Store': ['Gangnam', 'Gangnam', 'Hongdae', 'Hongdae', 'Gangnam', 'Hongdae'],
    'Item': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Apple'],
    'Sales': [100, 200, 150, 100, 120, 130]
}
df = pd.DataFrame(data)

# 1. 피벗 테이블 생성
# 행: Store, 열: Item, 값: Sales의 합계(sum)
pivot_df = df.pivot_table(index='Store', columns='Item', values='Sales', aggfunc='sum')

print("=== Pivot Table ===")
print(pivot_df)

# 2. 피벗 테이블을 바로 히트맵으로 그리기 (꿀조합)
plt.figure(figsize=(6, 4))
sns.heatmap(pivot_df, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Sales Heatmap")
plt.show()
