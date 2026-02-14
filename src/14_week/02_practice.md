---
layout: home
title: "14주차 2강: 최종 실전 모의고사 (Final Exam)"
---

# 14주차 2강: 최종 실전 모의고사 (Final Exam)

## 14.2.1. 문제 1. Pandas 기초
다음 데이터를 이용하여 데이터프레임을 만들고, **나이가 30세 이상인 사람**만 출력하세요.

```python
data = {
    'Name': ['Kim', 'Lee', 'Park', 'Choi'],
    'Age': [25, 35, 28, 40],
    'City': ['Seoul', 'Busan', 'Incheon', 'Seoul']
}
```

## 14.2.2. 문제 2. 결측치 처리
다음 데이터프레임에서 결측치(NaN)가 있는 행을 **모두 제거**하고 결과를 출력하세요.

```python
import numpy as np
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6], 'C': [7, 8, 9]})
```

## 14.2.3. 문제 3. 머신러닝 (분류)
아이리스(붓꽃) 데이터를 학습하여 꽃의 종류를 분류하는 모델을 만들고 정확도를 평가하세요.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 여기에 코드를 작성하세요 (데이터 분리 -> 모델 학습 -> 예측 -> 평가)
```

## 14.2.4. 문제 4. 군집화 (K-Means)
위 아이리스 데이터를 사용하여, 정답(`y`) 없이 `X` 데이터만으로 **3개의 그룹**으로 군집화하세요.
(Hint: `KMeans`, `fit`, `predict`)
