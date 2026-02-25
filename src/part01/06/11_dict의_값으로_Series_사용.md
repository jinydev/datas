---
layout: docs
title: "11. dict의 값으로 Series 사용"
---

## 11. dict의 값으로 Series 사용

시리즈 s1, s2, s3를 만든다.

```python
import pandas as pd

s1 = pd.Series([90, 80, 60, 66])
s2 = pd.Series([45, 73, 83, 99])
s3 = pd.Series([92, 75, 82, 75])
```

위에서 만든 시리즈를 dict의 값으로 대입하여 `df`를 생성한다. 기본 인덱스로 데이터프레임이 생성된다.

```python
df = pd.DataFrame({'국어': s1, '영어': s2, '수학': s3})
print(df)
```

다음 코드로 행 레이블을 지정하면 다음과 같다.

```python
df.index = ['노', '장', '박', '강']
print(df)
```

시리즈 사용 시 주의할 점이 있다. 시리즈의 인덱스가 바로 데이터프레임의 행 레이블이 된다는 것이다. 다음 코드에서 시리즈의 인덱스와 같은 데이터프레임의 인덱스에 값이 저장된다. 지정되지 않은 원소는 결측값인 `NaN(Not a Number)`으로 저장된다.

```python
df = pd.DataFrame({'A': pd.Series([10, 20, 30], index=[0, 1, 2]),
                   'B': pd.Series([3, 2, 1], index=[1, 2, 3])})
print(df)
```

다음처럼 시리즈 2개를 `index`를 붙여 생성하고, 1개는 기본 인덱스로 생성한다.

```python
s1 = pd.Series([90, 80, 60], index=['노', '장', '박'])
s2 = pd.Series([45, 73, 99], index=['장', '박', '강'])
s3 = pd.Series([92, 75, 82, 75])
```

위에서 만든 시리즈를 사용하고 `index`도 지정해서 `df`를 생성한다. 결과적으로 데이터프레임의 행 레이블에 맞는 시리즈 인덱스의 자료만이 저장되는 것을 알 수 있다.

```python
df = pd.DataFrame({'국어': s1, '영어': s2, '수학': s3},
                  index=['노', '장', '박', '강'])
print(df)
```
