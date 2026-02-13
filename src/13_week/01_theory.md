---
layout: default
title: "13주차 1강: 끼리끼리 모여라 (K-Means Clustering)"
---

# 13주차 1강: 끼리끼리 모여라 (K-Means Clustering)

## 13.1.1. K-Means 원리

> **비지도 학습**: 정답(Label)이 없는 데이터에서 패턴을 찾습니다.
> **K-Means**: 데이터를 **K개의 그룹(Cluster)**으로 묶습니다. 중심점(Centroid)을 이동시키며 그룹을 최적화합니다.

### 13.1.1.1. 시나리오: 고객 세분화 (Customer Segmentation)
쇼핑몰 고객들을 구매 패턴에 따라 3개 그룹(VIP, 일반, 잠재고객)으로 나누고 싶습니다. 하지만 누가 VIP인지 정해진 건 없습니다.

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 데이터 (구매 횟수, 총 구매액)
X = ... 

# 모델 생성 (3개 그룹으로 나누겠다)
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# 그룹 예측 (0, 1, 2 중 하나로 분류됨)
labels = model.predict(X)
```

## 13.1.2. 몇 개의 그룹이 좋을까? (Elbow Method)

K를 2개로 할지, 5개로 할지 어떻게 알까요?
그룹 내 오차(Inertia)가 급격히 줄어들다가 완만해지는 지점(팔꿈치, Elbow)을 찾습니다.

```python
inertias = []
for k in range(1, 10):
    model = KMeans(n_clusters=k)
    model.fit(X)
    inertias.append(model.inertia_)

plt.plot(range(1, 10), inertias, marker='o')
plt.show() # 꺾이는 지점이 최적의 K!
```
