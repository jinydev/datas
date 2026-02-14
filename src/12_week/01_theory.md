---
layout: home
title: "12주차 1강: 이메일이 스팸인가요? (Classification Models)"
---

# 12주차 1강: 이메일이 스팸인가요? (Classification Models)

## 12.1.1. 로지스틱 회귀 (Logistic Regression)

> **핵심**: "이 데이터가 정답일 확률은 몇 %인가?"를 계산하여, 50%가 넘으면 1(Yes), 아니면 0(No)으로 분류합니다.

선형 회귀가 직선을 긋는 것이라면, 로지스틱 회귀는 **S자 곡선(Sigmoid 함수)**을 사용하여 데이터를 0과 1 사이로 압축합니다.

```python
from sklearn.linear_model import LogisticRegression

# 모델 생성 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 예측 (0 또는 1)
y_pred = model.predict(X_test)
```

## 12.1.2. 의사결정나무 (Decision Tree)

> **핵심**: **스무고개** 게임과 같습니다. 데이터를 가장 잘 구분할 수 있는 질문을 계속 던져서 정답을 찾습니다.

- 장점: 모델이 왜 그런 판단을 내렸는지 이해하기 쉽습니다. (시각화 가능)
- 단점: 학습 데이터에만 너무 맞춤화될 수 있습니다. (과대적합 주의)

```python
from sklearn.tree import DecisionTreeClassifier

# 모델 생성 및 학습
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)
```

### 12.1.2.1. 시각적 예제 (Mermaid)

```mermaid
graph TD
    A[날개가 있는가?] -->|Yes| B[알을 낳는가?]
    A -->|No| C[포유류인가?]
    B -->|Yes| D[조류 (Bird)]
    B -->|No| E[곤충 (Insect)]
```
