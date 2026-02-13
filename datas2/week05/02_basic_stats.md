# 5-2. 기본 통계 함수 (Sum, Mean, Median)

## 1. 판다스와 넘파이의 통계
둘 다 비슷합니다. 함수 이름도 거의 같습니다.

```python
import pandas as pd
import numpy as np

scores = [80, 90, 75, 100, 60]

# 넘파이로 계산
print("평균:", np.mean(scores))
print("합계:", np.sum(scores))
print("최대값:", np.max(scores))

# 판다스로 계산 (시리즈)
s = pd.Series(scores)
print("평균:", s.mean())
print("중앙값:", s.median())
```

## 2. 데이터프레임 전체 통계
표(DataFrame)에서는 열(Column)별로 계산해줍니다.

```python
data = {
    '국어': [80, 90, 70],
    '수학': [100, 50, 80],
    '영어': [90, 100, 90]
}
df = pd.DataFrame(data)

# 과목별 평균
print(df.mean()) 
```

## 3. 한방에 요약하기 (.describe)
이거 하나면 끝납니다. **강력 추천!**

```python
# 개수, 평균, 표준편차, 최소, 25%, 50%, 75%, 최대값을 보여줍니다.
print(df.describe())
```

## 4. 핵심 정리
*   `mean()`: 평균, `sum()`: 합계, `max()`: 최대, `min()`: 최소.
*   `df.describe()`: 주요 통계량을 한 번에 표로 보여주는 마법의 함수.
