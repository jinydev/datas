# 02_customer_segmentation.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. 데이터 생성 (가상의 쇼핑몰 데이터)
np.random.seed(42)
n_samples = 200
# 그룹 1: 수입 적고 지출 적은
g1 = np.random.normal(loc=[25, 20], scale=[5, 5], size=(50, 2))
# 그룹 2: 수입 적고 지출 많은
g2 = np.random.normal(loc=[25, 80], scale=[5, 5], size=(50, 2))
# 그룹 3: 수입 많고 지출 적은
g3 = np.random.normal(loc=[80, 20], scale=[10, 5], size=(50, 2))
# 그룹 4: 수입 많고 지출 많은
g4 = np.random.normal(loc=[80, 80], scale=[10, 5], size=(50, 2))
# 그룹 5: 중간 (평범)
g5 = np.random.normal(loc=[50, 50], scale=[10, 10], size=(50, 2))

data = np.vstack([g1, g2, g3, g4, g5])
df = pd.DataFrame(data, columns=['Annual Income (k$)', 'Spending Score (1-100)'])

# 2. EDA
print("=== 데이터 미리보기 ===")
print(df.head())

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=df)
plt.title('Customer Data Distribution')
plt.show()

# 4. 전처리 (스케일링)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 5. Elbow 기법
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), inertia, 'marker')
plt.title('Elbow Method')
plt.show()
# 5개에서 꺾인다고 가정하고 진행

# 6. K-Means 모델링 (K=5)
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
df['Cluster'] = clusters

# 8. 클러스터 시각화 및 해석
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='deep', s=100)

# 중심점 역변환 (원래 좌표로 복구해서 찍기)
centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X', label='Centroids')

plt.title('Customer Segments')
plt.legend()
plt.show()

# 18. 그룹별 통계 확인
print("\n=== 클러스터별 평균 특성 ===")
print(df.groupby('Cluster').mean())

# 예시 해석:
# Cluster 0: 평균 소득 25, 평균 지출 79 (YOLO 그룹)
# Cluster 1: 평균 소득 80, 평균 지출 80 (VIP 그룹)
# ... 등등 데이터 결과에 따라 해석
