---
layout: home
title: "13주차 2강: 모의고사는 여러 번 (Cross Validation)"
---

# 13주차 2강: 모의고사는 여러 번 (Cross Validation)

## 13.2.1. K-Fold 교차 검증

데이터를 학습용(Train)과 테스트용(Test)으로 한 번만 나누면, "운 좋게 쉬운 문제만 테스트셋에 걸릴" 수도 있습니다.
그래서 **K번 돌아가면서 검증**합니다.

> **과정 (K=5일 때)**
> 1. 데이터를 5등분 합니다.
> 2. (1,2,3,4)로 공부하고 (5)로 시험 -> 점수 A
> 3. (1,2,3,5)로 공부하고 (4)로 시험 -> 점수 B
> ...
> 5. 최종 점수 = (A+B+C+D+E) / 5

이렇게 하면 모델의 진짜 실력을 더 정확하게 알 수 있습니다.

```python
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

# 5-Fold 교차 검증
scores = cross_val_score(model, X, y, cv=5)

print("각 회차별 점수:", scores)
print("평균 점수:", scores.mean())
```
