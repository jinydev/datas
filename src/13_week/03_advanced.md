---
layout: default
title: "13주차 3강: 최강의 모델 만들기 (Grid Search)"
---

# 13주차 3강: 최강의 모델 만들기 (Grid Search)

## 13.3.1. 하이퍼파라미터 튜닝

모델에는 사람이 직접 설정해줘야 하는 값들이 있습니다. 이를 **하이퍼파라미터**라고 합니다.
- 의사결정나무: `max_depth` (나무 깊이), `min_samples_split`.
- K-Means: `n_clusters` (K값).

이걸 3으로 할지 10으로 할지 어떻게 알까요?

## 13.3.2. Grid Search (그리드 서치)

> **전략**: "가능한 모든 조합을 다 넣어보자!"

```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

# 튜닝할 파라미터 후보들
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10]
}

# 그리드 서치 객체 생성
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(),
    param_grid=param_grid,
    cv=5 # 교차 검증도 같이 수행!
)

# 학습 시작 (모든 경우의 수 다 해봄)
grid_search.fit(X_train, y_train)

print("최적의 파라미터:", grid_search.best_params_)
print("최고 점수:", grid_search.best_score_)
```

이 과정을 마치면 여러분의 모델은 **최적의 상태**로 튜닝됩니다.
