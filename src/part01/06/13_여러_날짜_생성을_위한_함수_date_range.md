---
layout: docs
title: "13. 여러 날짜 생성을 위한 함수 date_range()"
---

## 13. 여러 날짜 생성을 위한 함수 date_range()

함수 `date_range()`를 통해 연속된 날짜인 `DatetimeIndex`를 얻을 수 있다. 다음으로 2025년 1월 1일부터 6일간의 시퀀스를 생성한다.

```python
dates = pd.date_range("20250101", periods=6)
print(dates)
```
위 반환 값의 원소는 시간 데이터를 나타내는 `Timestamp` 자료형이다.

```python
dates[0]
# Timestamp('2025-01-01 00:00:00', freq='D')
```

인자 `periods`가 없다면 `end` 인자로 지정할 수 있다. 인자 `end`는 포함되며 마지막 값이다.

```python
dates = pd.date_range("20250101", end='20250110')
print(dates)
```

인자 `freq='3D'`로 다음 날짜를 3일 후로 지정할 수 있다.

```python
dates = pd.date_range("20250101", periods=6, freq='3D')
print(dates)
```

인자 `freq='3H'`로 다음 시간을 3시간 후로 지정할 수 있다.

```python
dates = pd.date_range("20250101", periods=6, freq='3H')
print(dates)
```

인자 `freq='W'`로 다음 날짜를 1주 후로 지정할 수 있다. 시작일은 `start`에 지정한 날을 포함해서 이후 첫 일요일이 시작이다. 키워드 인자 `freq='W-SUN'`과 같다.

```python
dates = pd.date_range("20250101", periods=6, freq='W')
print(dates)
```

키워드 인자 `freq='W-TUE'`로 시작일이 매주 화요일이 된다.

```python
dates = pd.date_range("20240101", periods=6, freq='W-TUE')
print(dates)
```

키워드 인자 `freq='W-FRI'`로 시작일이 매주 금요일이 된다.

```python
dates = pd.date_range("20240101", periods=6, freq='W-FRI')
print(dates)
```

인자 `freq='M'`으로 다음 날짜를 1달 후로 지정할 수 있다. 시작일은 `start`에 지정한 날을 포함해서 월의 마지막 일자가 시작이다.

```python
dates = pd.date_range("20250101", periods=6, freq='M')
print(dates)
```

인자 `freq='MS'`로 지정하며 시작일은 `start`에 지정한 날을 포함해서 월의 시작 일자가 된다.

```python
dates = pd.date_range("20250101", periods=6, freq='MS')
print(dates)
```
