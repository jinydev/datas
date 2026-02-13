---
layout: default
title: "11주차 2강: 미래를 예측해 보자 (Linear Regression)"
---

# 11주차 2강: 미래를 예측해 보자 (Linear Regression)

## 11.2.1. 데이터 분리 (Train/Test Split)

모의고사를 풀면서 공부했는데, 수능 문제로 똑같은 모의고사가 나오면 실력을 제대로 평가할 수 있을까요?
그래서 데이터를 두 개로 나눕니다.

- **학습 데이터 (Train Set)**: 공부할 때 쓰는 문제집 (80%).
- **테스트 데이터 (Test Set)**: 최종 실력 평가용 수능 문제 (20%).

```python
from sklearn.model_selection import train_test_split
import numpy as np

# 공부 시간(X)과 점수(y) 데이터
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# 데이터 나누기 (8:2 비율)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("학습용 개수:", len(X_train)) # 8개
print("테스트용 개수:", len(X_test)) # 2개
```

## 11.2.2. 선형 회귀 모델 학습

> **Q. 공부를 12시간 하면 몇 점을 받을까?**

```python
from sklearn.linear_model import LinearRegression

# 1. 모델 생성
model = LinearRegression()

# 2. 모델 학습 (공부 시키기) -> fit(문제, 정답)
model.fit(X_train, y_train)

# 3. 예측하기 (시험 보기) -> predict(새로운 문제)
prediction = model.predict([[12]]) # 2차원 배열로 넣어야 함
print("12시간 공부 시 예상 점수:", prediction)
# [120.]
```

기계가 `점수 = 10 * 시간`이라는 규칙을 스스로 찾아냈습니다!
