---
layout: pandas
title: "6.3.7 행과 열 참조"
---

## 6.3.7 행과 열 참조

다음 코드처럼 `pf.loc['행명', '열명']`으로 행과 열에 맞는 한 원소를 참조할 수 있다.

```python
pf.loc['윤일형', '출석']
# 6.3.7 ```

다음 코드처럼 행과 열에는 슬라이싱이 가능하다.

```python
pf.loc['윤일형':'유한빈', '기말']
```

다음 코드는 행과 열이 모두 슬라이싱으로 데이터프레임을 반환한다.

```python
pf.loc['윤일형':'유한빈', '기말':'과제']
```

다음 `pf.index[0], pf.columns[1]`로 행명과 열명을 대체할 수 있다.

```python
pf.loc[pf.index[0], pf.columns[1]]
# 6.3.7 ```

다음으로 행 슬라이싱한 열의 시리즈를 반환받을 수 있다.

```python
pf.loc[pf.index[0:3], pf.columns[2]]
```

다음으로 행과 열을 슬라이싱한 데이터프레임을 반환받을 수 있다.

```python
pf.loc[pf.index[0:3], pf.columns[2:]]
```