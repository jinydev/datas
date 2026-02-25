---
layout: docs
title: "03. pydataset 주요 자료 가져오기"
---

## 03. pydataset 주요 자료 가져오기

#### ① 주요 자료 titanic 가져오기

데이터에 대한 정보를 모를 때 편리하게 사용할 수 있다. 타이타닉 데이터셋은 1912년 영국에서 미국으로의 처녀 출항에 침몰한 타이타닉 배의 생존자와 사망자 정보 데이터셋이다.

```python
df = data('titanic', show_doc=True)
```

다음 `df = data('dataset_id')`는 'dataset_id'의 데이터셋을 가져올 수 있다. 다음은 유명한 타이타닉 데이터셋을 가져오는 코드이다.

```python
df = data('titanic')
print(df)
```
**출력:**
```
          class     age    sex survived
1     1st class  adults    man      yes
2     1st class  adults    man      yes
3     1st class  adults    man      yes
4     1st class  adults    man      yes
5     1st class  adults    man      yes
...         ...     ...    ...      ...
1312  3rd class   child  women       no
1313  3rd class   child  women       no
1314  3rd class   child  women       no
1315  3rd class   child  women       no
1316  3rd class   child  women       no

[1316 rows x 4 columns]
```

다음으로 타이타닉 데이터셋 정보를 볼 수 있다.

```python
df.info()
```

다음으로 타이타닉 데이터셋의 열 정보를 볼 수 있다.

```python
df.describe()
```
**출력:**
```
            class     age    sex survived
count        1316    1316   1316     1316
unique          3       2      2        2
top     3rd class  adults    man       no
freq          706    1207    869      817
```

다음은 좌석 등급인 열 'class'의 종류와 빈도 수이다.

```python
df['class'].value_counts()
# 3rd class    706
# 1st class    325
# 2nd class    285
# Name: class, dtype: int64
```

다음은 열 'age'의 종류와 빈도 수이다.

```python
df.age.value_counts()
# adults    1207
# child      109
# Name: age, dtype: int64
```

다음은 열 'sex'의 종류와 빈도 수이다.

```python
df.sex.value_counts()
# man      869
# women    447
# Name: sex, dtype: int64
```

다음은 생존자 정보인 열 'survived'의 종류와 빈도 수이다.

```python
df.survived.value_counts()
# no     817
# yes    499
# Name: survived, dtype: int64
```

다음은 데이터프레임에서 모든 열의 종류와 빈도 수이다.

```python
df.value_counts()
```

#### ② 자동차 연비 자료 mpg 가져오기

다음으로 데이터프레임 `all_data`에서 열 `title`이 문자열 'car'를 포함한 행을 알아볼 수 있다. 데이터셋 id로 `mpg`가 보인다. 데이터셋 mpg(miles per gallon)는 1999년과 2008년의 인기 차종 38개에 대한 연비 데이터이다.

```python
all_data[all_data.title.str.contains('car')]
```

위에서 찾은 연비 데이터 `mpg`로 데이터를 가져오자.

```python
df_mpg = data('mpg')
print(df_mpg)
```

미국 자동차 연비 데이터인 `mpg`의 요약 정보는 다음과 같다.

```python
data('mpg', show_doc=True)
```

데이터프레임 `df_mpg`의 정보는 다음과 같다.

```python
df_mpg.info()
```

연비 데이터의 데이터프레임 값이 수인 열의 주요 통계 정보는 다음과 같다.

```python
df_mpg.describe()
```

연비 데이터의 모델인 열 `model`의 종류는 다음과 같다.

```python
df_mpg.model.value_counts()
```

연비 데이터의 실린더 수인 열 `cyl`의 종류는 다음과 같다.

```python
df_mpg.cyl.value_counts()
```

연비 데이터의 자동차 회사 정보인 열 `manufacturer`의 빈도는 다음과 같다.

```python
df_mpg.manufacturer.value_counts()
```
