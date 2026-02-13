# 14주차 3강: 정답 및 해설 (Solutions)

## 14.3.1. 문제 1. Pandas 기초

```python
import pandas as pd

data = {
    'Name': ['Kim', 'Lee', 'Park', 'Choi'],
    'Age': [25, 35, 28, 40],
    'City': ['Seoul', 'Busan', 'Incheon', 'Seoul']
}
df = pd.DataFrame(data)

# 30세 이상 필터링
print(df[df['Age'] >= 30])
```

## 14.3.2. 문제 2. 결측치 처리

```python
import numpy as np
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6], 'C': [7, 8, 9]})

# 결측치 제거
df_clean = df.dropna()
print(df_clean)
```

## 14.3.3. 문제 3. 머신러닝 (분류)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

# 1. 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. 모델 학습
model = LogisticRegression(max_iter=1000) # max_iter는 경고 방지용
model.fit(X_train, y_train)

# 3. 예측 및 평가
y_pred = model.predict(X_test)
print("정확도:", accuracy_score(y_test, y_pred))
```

## 14.3.4. 문제 4. 군집화 (K-Means)

```python
from sklearn.cluster import KMeans

# 모델 생성 (3개 그룹)
kmeans = KMeans(n_clusters=3, random_state=42)

# 학습 (정답 y는 사용하지 않음!)
kmeans.fit(X)

# 그룹 예측
labels = kmeans.predict(X)
print(labels)
```
