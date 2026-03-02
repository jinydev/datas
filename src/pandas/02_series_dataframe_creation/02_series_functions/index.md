---
layout: pandas
title: "6.2.2 Series 활용 함수"
---

## 6.2.2 Series 활용 함수

#### ① Series의 정렬

다음은 학생의 성적을 저장한 시리즈이다.

```python
import pandas as pd

s = ['희빈', '수영', '현수', '지호', '지민']
p = pd.Series([99, 84, 92, 65, 78], index=s)
print(p)
```
**출력:**
```
희빈    99
수영    84
현수    92
지호    65
지민    78
dtype: int64
```

다음 코드로 시리즈의 `name`과 `index`의 `name`도 지정할 수 있다.

```python
p.name = '수학성적'
p.index.name = 'st_name'
print(p)
```

시리즈의 함수 `sort_values()`로 시리즈의 값을 오름차순으로 정렬할 수 있다.

```python
p.sort_values()
```
**출력:**
```
st_name
지호    65
지민    78
수영    84
현수    92
희빈    99
Name: 수학성적, dtype: int64
```

시리즈의 함수 `sort_values(ascending=False)`로 시리즈의 값을 내림차순으로 정렬할 수 정렬할 수 있다.

```python
p.sort_values(ascending=False)
```

시리즈의 함수 `sort_index()`로 학생이름인 `index`의 값을 오름차순으로 정렬할 수 있다.

```python
p.sort_index()
```

시리즈의 함수 `sort_index(ascending=False)`로 `index`의 값을 내림차순으로 정렬할 수 있다.

```python
p.sort_index(ascending=False)
```

#### ② Series의 기본 통계

시리즈의 함수 `max()`, `min()`으로 최댓값과 최솟값을 알 수 있다.

```python
print(p.max())
print(p.min())
# 6.2.2 # 6.2.2 ```

시리즈의 함수 `mean()`, `median()`으로는 평균값과 중간값을 알 수 있다.

```python
print(p.mean())
print(p.median())
# 6.2.2 # 6.2.2 ```

시리즈의 함수 `count()`와 속성 `size`로 시리즈의 원소 수를 알 수 있다.

```python
print(p.count())
print(p.size)
# 6.2.2 # 6.2.2 ```

시리즈의 함수 `describe()`로 시리즈의 기초 통계량을 알 수 있다.

```python
p.describe()
```

#### ③ Series의 count()와 value_counts()

**[실전 꿀팁]: 데이터 파악의 핵심 `value_counts()`**
`value_counts()`는 각 데이터 항목이 몇 번 등장했는지 세어주는 기능으로, 실무 데이터 분석에서 **가장 많이 쓰는 함수 Top 3** 안에 듭니다. 설문조사 응답 빈도 분포 현황이나 범주형(Category) 데이터의 개수를 파악할 때 필수적으로 사용됩니다.

다음 시리즈를 하나 생성하자. `np.nan`이나 `None`은 값이 없는 결측치(missing value)라 한다.

```python
import numpy as np
import pandas as pd

s = pd.Series([3, 1, 1, 2, None, np.nan, 4, 6, 6, np.nan])
print(s)
```

결측값은 `NaN(Not a Number)`이나 `None`으로 표시된다.

함수 `s.count()`는 결측값을 제외한 값의 시리즈의 원소 수가 반환된다.

```python
s.count()
# 6.2.2 ```

함수 `s.value_counts()`는 고유한 값의 빈도를 포함하는 시리즈를 반환한다. 결과 개체는 첫 번째 요소가 가장 자주 발생하는 요소가 되도록 내림차순으로 정렬된다. 기본적으로 결측값인 NA 값을 제외한다.

```python
s.value_counts()
```
**출력:**
```
1.0    2
6.0    2
3.0    1
2.0    1
4.0    1
dtype: int64
```

키워드 인자 `dropna=False`는 결측값인 NA 값을 포함할 수 있다.

```python
s.value_counts(dropna=False)
```

키워드 인자 `sort=False`는 정렬을 안 할 수 있다.

```python
s.value_counts(sort=False, dropna=False)
```

키워드 인자 `bins=4`는 값의 범위를 구하는 구간 수를 지정할 수 있다. 결과 시리즈의 첨자가 구간이며 값이 해당 구간의 빈도수이다. 많은 빈도 구간부터 정렬되어 표시된다. 구간의 왼쪽은 미포함이며 오른쪽은 포함이다. 이러한 표기 방식을 반 열린 구간(half-open bins) 방식이라 한다.

```python
s.value_counts(bins=4)
```

작은 값부터 큰 값으로 쉽게 보려면 키워드 인자 `sort=False`로 정렬되지 않게 한다.

```python
s.value_counts(bins=4, sort=False)
```

구간 `bins`를 정수가 아닌 구간을 직접 나열한 목록으로 입력할 수 있다.

```python
s.value_counts(bins=[0.5, 3.5, 6.5], sort=False)
```