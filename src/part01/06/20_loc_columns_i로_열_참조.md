---
layout: docs
title: "06. loc[:, columns[i]]로 열 참조"
---

## 06. loc[:, columns[i]]로 열 참조

`pf.columns[0]`은 첫 번째 열 이름을 반환한다. 그러므로 `pf.loc[:, pf.columns[0]]`으로 첫 번째의 열 결과를 시리즈로 반환받을 수 있다.

```python
pf.loc[:, pf.columns[0]] # 첫 번째 열 조회
```

다음처럼 내부에 목록으로 기술하면 데이터프레임을 반환받을 수 있다.

```python
pf.loc[:, [pf.columns[0]]] # 첫 번째 열 조회 데이터프레임 반환
```

다음으로 슬라이싱도 가능하다.

```python
pf.loc[:, pf.columns[1:]] # 슬라이싱 열 검색
```

다음으로 위에서 반환받은 데이터프레임의 일부 열로 구성되는 데이터프레임을 반환받을 수 있다.

```python
pf.loc[:, pf.columns[1:]][['기말', '과제']]
```
