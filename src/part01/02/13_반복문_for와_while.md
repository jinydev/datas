---
layout: docs
title: "03. 반복문 for와 while"
---

## 03. 반복문 for와 while

### 반복문 for

다음 `for` 구문으로 `in` 이후의 리스트(list), 튜플(tuple), 딕셔너리(dictionary), 집합(set) 등의 항목이 있는 모임형으로 반복할 수 있다. 다음 구문으로 1에서 5까지 반복한다. `for` 마지막 콜론 `:`은 반드시 필요하며 이후 반복 몸체는 들여쓰기로 블록을 구성해야 한다.

```python
for x in range(1, 6):
    print(x)
```
**출력:**
```
1
2
3
4
5
```

다음 코드로 리스트 `num`을 구성하는 원소 10, 20, 30, 40으로 반복한다. 리스트는 모든 자료형 항목의 나열인 자료형으로 다음 단원에서 자세히 학습할 예정이다.

```python
num = [10, 20, 30, 40]
for i in num:
    print(i)
```
**출력:**
```
10
20
30
40
```

다음 코드로는 리스트 `fruits`를 구성하는 원소 "apple", 2500, "banana", 500, "mango", 2000으로 반복한다.

```python
fruits = list(["apple", 2500, "banana", 500, "mango", 2000])
for x in fruits:
    print(x)
```
**출력:**
```
apple
2500
banana
500
mango
2000
```

### 반복문 while

다음 `while 조건: 블록` 구문으로 조건이 `True`이면 블록을 반복하는 구문을 구현할 수 있다. 다음 코드는 1부터 10까지의 합을 `sum`에 구해 출력한다.

```python
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1

print(sum)
```
**출력:**
```
55
```
