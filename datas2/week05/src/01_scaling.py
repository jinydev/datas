# 01_scaling.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 데이터 준비
df = sns.load_dataset('titanic')
# 결측치 제거 (실습 편의상)
data = df[['age', 'fare']].dropna()

print("=== 원본 데이터 통계 ===")
print(data.describe())

# 3. StandardScaler 적용
scaler_std = StandardScaler()
# fit_transform: 학습하고 변환까지 한 번에
data_std = scaler_std.fit_transform(data)
# 결과가 numpy array이므로 다시 DataFrame으로 변환
df_std = pd.DataFrame(data_std, columns=['age', 'fare'])

print("\n=== 표준화 후 데이터 통계 (평균~0, 표준편차~1) ===")
print(df_std.describe())

# 4. MinMaxScaler 적용
scaler_minmax = MinMaxScaler()
data_minmax = scaler_minmax.fit_transform(data)
df_minmax = pd.DataFrame(data_minmax, columns=['age', 'fare'])

print("\n=== 정규화 후 데이터 통계 (최소0, 최대1) ===")
print(df_minmax.describe())

# 10. 시각적 비교 (산점도)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(data['age'], data['fare'], color='blue', alpha=0.5)
plt.title('Original Data')
plt.xlabel('Age')
plt.ylabel('Fare')

plt.subplot(1, 3, 2)
plt.scatter(df_std['age'], df_std['fare'], color='red', alpha=0.5)
plt.title('StandardScaler (Z-Score)')
plt.xlabel('Age (Scaled)')
plt.ylabel('Fare (Scaled)')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.scatter(df_minmax['age'], df_minmax['fare'], color='green', alpha=0.5)
plt.title('MinMaxScaler (0-1)')
plt.xlabel('Age (Scaled)')
plt.ylabel('Fare (Scaled)')
plt.grid(True)

plt.tight_layout()
plt.show()

# 12. 로그 변환과의 비교 (Fare 분포)
import numpy as np
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.histplot(df_std['fare'], kde=True, color='red')
plt.title('Standard Scaler (Still Skewed)')

plt.subplot(1, 2, 2)
# 로그 변환은 분포의 모양을 핍니다.
sns.histplot(np.log1p(data['fare']), kde=True, color='purple')
plt.title('Log Transformation (Normal-like)')

plt.show()
