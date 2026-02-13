# 01_clustering_intro.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. 데이터 준비 (Iris)
iris = load_iris()
X = iris.data
y = iris.target # 실제 정답 (비교용으로만 사용)

# 2. 스케일링 (필수)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. K-Means 군집화
kmeans = KMeans(n_clusters=3, random_state=42)
pred_kmeans = kmeans.fit_predict(X_scaled) 
# pred_kmeans는 0, 1, 2 레이블을 가짐 (실제 품종 번호와 일치한다는 보장 없음)

# 4. 평가 (실루엣 점수)
sil_score = silhouette_score(X_scaled, pred_kmeans)
print(f"K-Means Silhouette Score: {sil_score:.4f}")

# 5. 엘보우 기법 (최적의 K 찾기)
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), inertia, 'bo-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# 6. PCA 차원 축소 (시각화를 위해 4차원 -> 2차원)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(f"PCA 설명된 분산 비율: {pca.explained_variance_ratio_}")

# 7. 시각화 비교
plt.figure(figsize=(15, 5))

# 실제 품종
plt.subplot(1, 3, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title("Actual Species")

# K-Means 결과
plt.subplot(1, 3, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=pred_kmeans, cmap='viridis')
# 중심점 표시
centers_pca = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers_pca[:, 0], centers_pca[:, 1], s=100, c='red', marker='X')
plt.title("K-Means Clustering")

# DBSCAN 결과
dbscan = DBSCAN(eps=0.5, min_samples=5)
pred_dbscan = dbscan.fit_predict(X_scaled)
plt.subplot(1, 3, 3)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=pred_dbscan, cmap='viridis')
plt.title("DBSCAN (Outliers detected)")
plt.show()

# DBSCAN은 밀도가 낮은 점들을 -1(보라색)로 분류하여 이상치로 처리함
