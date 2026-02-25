---
layout: docs
title: "09. 여러 Series로 DataFrame 생성"
---

## 09. 여러 Series로 DataFrame 생성

다음 Series `courses`를 정의한다.

```python
courses = pd.Series(["Spark","PySpark","Hadoop"], name='courses')
print(courses)
```

다음 Series `fees`를 정의한다.

```python
fees = pd.Series([250000, 300000, 200000], name='fees')
print(fees)
```

위 두 시리즈 `courses`와 `fees`를 열로 하는 데이터프레임은 다음처럼 생성할 수 있다.

```python
df = pd.DataFrame({courses.name: courses, fees.name: fees})
print(df)
```

또는 `pd.concat([목록])`을 이용해 간단히 데이터프레임을 생성할 수 있다. 이는 목록의 항목을 붙인 데이터프레임을 반환한다.

```python
courses = pd.Series(["Spark", "PySpark","Hadoop"], name='courses')
fees = pd.Series([250000, 300000, 200000], name='fees')

df = pd.concat([courses, fees], axis=1)
print(df)
```

위 코드에서 `axis=1`을 생략하면 `axis=0`이 되어 세로로 추가된 시리즈 파환한다.

```python
df = pd.concat([courses, fees])
print(df)
```

물론, 다음으로도 데이터프레임을 생성할 수 있다. 그러나 하나의 시리즈가 행이 된다. 시리즈의 `name`은 행의 `index`가 된다.

```python
df = pd.DataFrame([courses, fees])
print(df)
```

다음 `df.T`의 속성(transpose)으로 행과 열을 바꿔 위에서 만든 것처럼 시리즈를 열로 만들 수 있다.

```python
df.T
```

다음 코드로 빈 데이터프레임을 생성하자.

```python
df = pd.DataFrame()
```

다음 코드로 빈 `df`에 열 `courses`를 만든다.

```python
courses = pd.Series(["Spark","PySpark","Hadoop"], name='courses')
df[courses.name] = courses
print(df)
```

다음 코드로 `df`에 다시 열 `fees`를 추가한다.

```python
fees = pd.Series([250000, 300000, 200000], name='fees')
df[fees.name] = fees
print(df)
```
