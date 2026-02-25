---
layout: docs
title: "04. Series 생성과 활용"
---

## 04. Series 생성과 활용

#### ① Series 생성

다음의 다양한 종류의 입력으로 생성할 수 있다.

* 1차원 ndarray, 목록, 딕셔너리 또는 Series
* 2차원 numpy.ndarray
* 하나의 Series
* 다른 하나의 DataFrame

키워드 인자 `name='first'`로 속성 `name` 지정이 가능하다.

```python
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8], name='first')
print(s)
```
**출력:**
```
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
Name: first, dtype: float64
```

#### ② Series 주요 속성

생성한 시리즈 `s`의 `name`은 다음 속성으로 알아볼 수 있다.

```python
s.name
# 'first'
```

생성한 시리즈 `s`의 기본 index는 `RangeIndex(start=0, stop=6, step=1)`이다.

```python
s.index
# RangeIndex(start=0, stop=6, step=1)
```

생성한 시리즈 `s`의 속성 `values`는 시리즈의 값으로 `ndarray` 자료형이다.

```python
s.values
# array([ 1.,  3.,  5., nan,  6.,  8.])
```

속성 `shape`로 시리즈의 차수와 모양을 알 수 있다.

```python
s.shape
# (6,)
```

속성 `size`로 시리즈의 원소 수를 알 수 있다.

```python
s.size
# 6
```

#### ③ 시리즈 인덱싱과 index, 슬라이싱

시리즈는 첨자로 원소값을 반환받을 수 있다.

```python
s[1]
# 3.0
```

시리즈는 인덱싱 `1:5`로 1에서 4까지의 원소의 부분 시리즈를 반환받을 수 있다. 즉, 반환값도 시리즈이다.

```python
s[1:5]
```
**출력:**
```
1    3.0
2    5.0
3    NaN
4    6.0
Name: first, dtype: float64
```

다음 코드로 이미 생성된 시리즈에 다시 문자열의 `index`를 지정할 수 있다.

```python
s.index = list('abcdef')
print(s)
```
**출력:**
```
a    1.0
b    3.0
c    5.0
d    NaN
e    6.0
f    8.0
Name: first, dtype: float64
```

새로 지정한 색인으로도 참조 가능하다.

```python
print(s['b'], s['e'])
# 3.0 6.0
```

물론, 새로 지정한 인덱싱으로 부분 시리즈를 반환받을 수 있다. 레이블 인덱싱이 정수 인덱싱과 다른 것은 마지막인 'e'를 포함한다는 것이다.

```python
s['c':'e']
```
**출력:**
```
c    5.0
d    NaN
e    6.0
Name: first, dtype: float64
```

다음 인덱싱으로도 첨자 'b'에서 'f'까지의 원소로 구성된 시리즈를 반환한다.

```python
s['b':'f']
```
**출력:**
```
b    3.0
c    5.0
d    NaN
e    6.0
f    8.0
Name: first, dtype: float64
```

레이블인 문자열 `index`를 지정해도 기본 정수 `index`는 사용할 수 있다. 다음 인덱싱으로도 첨자 0에서 2까지의 원소로 구성된 시리즈를 반환한다.

```python
s[0:3]
```
**출력:**
```
a    1.0
b    3.0
c    5.0
Name: first, dtype: float64
```

다음으로 첨자 1에서 3까지의 원소로 구성된 시리즈를 뷰로 반환한다.

```python
s1 = s[1:4]
print(s1)
```
**출력:**
```
b    3.0
c    5.0
d    NaN
Name: first, dtype: float64
```

`s1[0]`으로는 3이 참조된다.

```python
s1[0]
# 3.0
```

다음 코드로 `s1`의 첫 원소를 10으로 수정할 수 있다.

```python
s1[0] = 10
print(s1)
```
**출력:**
```
b    10.0
c     5.0
d     NaN
Name: first, dtype: float64
```

위에서 수정된 값은 원본 `s`에도 반영이 된 것을 확인할 수 있다.

```python
print(s)
```
**출력:**
```
a     1.0
b    10.0
c     5.0
d     NaN
e     6.0
f     8.0
Name: first, dtype: float64
```

다음으로 시리즈 `index`를 달리 지정할 수 있다.

```python
s.index = np.arange(1, 7)
print(s)
```
**출력:**
```
1     1.0
2    10.0
3     5.0
4     NaN
5     6.0
6     8.0
Name: first, dtype: float64
```

새로운 정수 첨자로 하나의 원소를 참조할 수 있다.

```python
s[1]
# 1.0
```

그러나 새로운 정수 첨자에는 0이 없으므로 다음 `s[0]`으로는 오류가 발생한다.

```python
# s[0]
# KeyError: 0
```
0에서부터 시작되는 기본 정수 첨자 대신에 다른 정수 첨자를 지정하는 것은 권장하지 않는다.

다음처럼 정수 슬라이싱은 기본 정수 첨자로 간주해 부분 시리즈를 반환한다.

```python
s[1:3]
```
**출력:**
```
2    10.0
3     5.0
Name: first, dtype: float64
```

#### ④ 시리즈 고급 인덱싱

다음 이름이 `age`인 시리즈를 생성해 변수 `age`에 저장한다.

```python
import pandas as pd

age = pd.Series([9, 17, 32, 45, 65, 98], index=list('abcdef'), name='age')
print(age)
```
**출력:**
```
a     9
b    17
c    32
d    45
e    65
f    98
Name: age, dtype: int64
```

다음이 고급 인덱싱으로 numpy 배열과 같이 `[첨자 목록]`으로 각 원소로 구성된 시리즈를 반환한다. 위 결과는 스칼라 값이나 다음 결과는 시리즈이다.

```python
age[[1, 3, 5]]
```
**출력:**
```
b    17
d    45
f    98
Name: age, dtype: int64
```

우리가 지정한 문자열 첨자로도 고급 첨자는 가능하다.

```python
age[['a', 'f', 'd']]
```
**출력:**
```
a     9
f    98
d    45
Name: age, dtype: int64
```

다음 코드 `age[['c']]`처럼 하나의 레이블 인덱스도 리스트로 지정하면 결과는 시리즈이다.

```python
age[['c']]
```
**출력:**
```
c    32
Name: age, dtype: int64
```

#### ⑤ 시리즈 논리 참조(블리안 인덱싱)

다음 시리즈 `s`가 있다.

```python
import pandas as pd

s = pd.Series([3, 6, -3, 0, -4, 8, -7])
print(s)
```

`s > 0`인 논리(condition) 결과의 시리즈를 반환한다.

```python
s > 0
```
**출력:**
```
0     True
1     True
2    False
3    False
4    False
5     True
6    False
dtype: bool
```

다음 코드는 조건 `s%2 == 0`의 논리 결과의 시리즈를 반환한다.

```python
s % 2 == 0
```

`s[s > 0]`을 수행하면 값이 `True`인 원소만으로 구성된 시리즈가 반환된다.

```python
s[s > 0]
```
**출력:**
```
0    3
1    6
5    8
dtype: int64
```

다음 조건 연산의 논리 인덱싱으로 양수이고 2로 나누어 떨어지는 값만으로 구성된 시리즈를 반환한다.

```python
s[(s > 0) & (s % 2 == 0)]
```
**출력:**
```
1    6
5    8
dtype: int64
```
