---
layout: docs
title: "04. loc[index[i]]로 행 참조"
---

## 04. loc[index[i]]로 행 참조

`pf.index[0]`은 첫 번째 행 이름을 반환한다. 그러므로 `pf.loc[pf.index[0]]`으로 첫 번째의 행 결과를 시리즈로 반환받을 수 있다.

```python
pf.loc[pf.index[0]] # 첫 번째 행 검색
```

다음처럼 내부에 목록으로 기술하면 데이터프레임을 반환받을 수 있다.

```python
pf.loc[[pf.index[0]]] # 첫 번째 행 검색
```

다음으로 슬라이싱도 가능하다.

```python
pf.loc[pf.index[1:4]] # 슬라이싱 행 검색
```

다음으로 위에서 반환받은 데이터프레임의 일부 열로 구성되는 데이터프레임을 반환받을 수 있다.

```python
pf.loc[pf.index[1:4]][['기말', '과제']]
```
