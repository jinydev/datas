import pandas as pd
import numpy as np

# 더러운 데이터 생성
df = pd.DataFrame({
    'Name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'Age': [20, 25, np.nan, 22, 150], # NaN과 150(이상치) 존재
    'Score': [90, 80, 70, np.nan, 50] # NaN 존재
})

print("=== 원본 데이터 ===")
print(df)

# 1. 결측치 처리 (Age는 평균으로 채우고, Score는 지우기)
mean_age = df['Age'][df['Age'] < 100].mean() # 150살 제외하고 평균 계산
df['Age'] = df['Age'].fillna(mean_age)
df = df.dropna(subset=['Score'])

# 2. 이상치 처리 (100살 넘으면 평균으로 수정)
df.loc[df['Age'] > 100, 'Age'] = mean_age

print("\n=== 수술 후 데이터 ===")
print(df)
