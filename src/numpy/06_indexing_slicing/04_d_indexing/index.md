---
layout: numpy
title: "4.6.4 1차원 배열의 색인"
---

# 4.6.4 배열 색인

## 4.4.4 1차원 배열의 색인

다음 numpy `ndarray` 배열 `x`가 있다.

```python
x = np.arange(10)
x
```
**출력:**
```
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

다음의 단순한 첨자나 슬라이싱은 이미 알아보았다.

```python
print(x[1])
print(x[:5])
```
**출력:**
```
1
[0 1 2 3 4]
```

표준 파이썬의 리스트와는 다르게 `numpy`의 `ndarray`는 여러 원소의 인덱싱이 가능하다. numpy `ndarray`의 정수 배열(또는 리스트) 인덱싱을 사용하면 배열에서 여러 임의 항목을 선택할 수 있다. 정수 배열 또는 리스트 `[2]`와 `[2, 3]`은 배열에서 참조할 첨자 목록을 나타낸다.

```python
print(x[[2]])
print(x[[2, 3]])
```
**출력:**
```
[2]
[2 3]
```

색인은 반환 값을 `ndarray` 배열이다.

```python
x[[2, 3, 5, 8]]
```
**출력:**
```
array([2, 3, 5, 8])
```

인덱스로는 리스트와 `ndarray` 모두 가능하다. 첨자는 음수 값도 허용되며 다음과 같이 작동한다.

```python
x[np.array([5, 3, -4, 8])]
```
**출력:**
```
array([5, 3, 6, 8])
```

색인 값이 범위를 벗어나면 `IndexError`가 발생한다.

```python
x[np.array([10])]
```
**오류:**
```
IndexError: index 10 is out of bounds for axis 0 with size 10
```
