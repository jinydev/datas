---
layout: pandas
title: "6.2.11 날짜를 포함한 데이터프레임"
---

# 6.2.11 날짜를 포함한 데이터프레임

다음 변수 `dates`에는 연속된 날짜 6개가 저장된다. 자동으로 `freq='D'`가 된다.

```python
dates = pd.date_range("20250302", periods=6)
print(dates)
```

위 `dates`를 `index`로 지정하고 열 이름 목록 각각 A, B, C, D로 지정한 `df`를 만든다.

```python
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
```