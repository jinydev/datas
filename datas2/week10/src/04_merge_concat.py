import pandas as pd

# 1. 고객 정보 (User DB)
users = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Kim', 'Lee', 'Park'],
    'level': ['VIP', 'Gold', 'Silver']
})

# 2. 구매 내역 (Order DB)
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104],
    'user_id': [1, 1, 2, 4], # 4번 유저는 정보가 없음!
    'amount': [1000, 2000, 500, 300]
})

print("=== Users ===")
print(users)
print("\n=== Orders ===")
print(orders)

# 3. Merge (Inner Join)
# 양쪽에 모두 정보가 있는 경우만 (4번 유저와 3번 유저 탈락)
merged_inner = pd.merge(orders, users, left_on='user_id', right_on='id', how='inner')
print("\n=== Merged (Inner) ===")
print(merged_inner)

# 4. Merge (Left Join)
# 구매 내역은 다 살리고, 고객 정보가 없으면 NaN으로 채움 (4번 유저 살림)
merged_left = pd.merge(orders, users, left_on='user_id', right_on='id', how='left')
print("\n=== Merged (Left) ===")
print(merged_left)
