---
layout: docs
title: "12. 열과 전체 자료형 속성 dtypes"
---

## 12. 열과 전체 자료형 속성 dtypes

다음 `df`는 키워드 인자 `data`에 `dict` `d`를 대입해 생성한다.

```python
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)
```

다음 속성 `df.dtypes`로 열과 전체 자료형을 알 수 있다. 정수의 기본형이 `int64`이다.

```python
df.dtypes
```

다시 `d`를 사용해 데이터프레임을 생성할 경우, 키워드 인자 `dtype=np.int8` 설정으로 정수 자료형을 `int8`로 지정할 수 있다.

```python
df = pd.DataFrame(data=d, dtype=np.int8)
df.dtypes
```
