---
layout: python
title: "3.4.4 집합"
---

# 3.4.4 집합

## 집합 개요와 활용

파이썬의 집합(set)은 중복된 원소가 없는 순서가 없는 자료형이다. 집합은 중괄호 `{ }` 안에 쉼표 `,`로 구분된 값을 넣어 생성한다. 수정 불가능한 집합 원소는 추가나 삭제가 가능하다. 즉, 집합 자체는 수정 가능하다. 집합의 원소는 중복을 허용하지 않으므로 멤버쉽 검사와 중복 제거에 주로 사용될 수 있다. 집합은 값의 중복을 허용하지 않기 때문에 중복된 데이터를 제거하는 데 유용하다.

- `{element0, element1, element2, ..., elementn}`
    - 각 element는 고유한(unique) 값으로 중복을 허용하지 않으며
    - 원소의 순서는 의미가 없으며
    - 원소는 `int`, `float`, `str`, `tuple` 등 수정 불가능(immutable)한 것이어야 함

다음 코드로 집합 `basket`을 만들 수 있다.

```python
basket = {'apple', 'orange', 'apple', 'pear'}
basket
```
**출력:**
```
{'orange', 'apple', 'pear'}
```

함수 `len()`으로 집합 원소의 수를 확인할 수 있다.

```python
len(basket)

print('grape' in basket)
print('apple' in basket)
```
**출력:**
```
False
True
```

자료형 집합을 사용하면 합집합, 교집합, 차집합과 같은 집합 연산을 효과적으로 수행할 수 있다. 다음은 집합 연산을 직접 수행한 코드이다.

```python
A = {1, 2, 3, 4, 5, 6, 7}
B = {3, 4, 5, 6, 7}

print(A.union(B))            # 합집합
print(A.intersection(B))     # 교집합
print(A.difference(B))       # 차집합
print(B.difference(A))       # 차집합
print(A.symmetric_difference(B)) # 대칭 차집합 (여집합)
```
**출력:**
```
{1, 2, 3, 4, 5, 6, 7}
{3, 4, 5, 6, 7}
{1, 2}
set()
{1, 2}
```

다음처럼 집합 연산자로도 가능하다.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6, 7}

print(A | B) # 합집합
print(A & B) # 교집합
print(A - B) # 차집합
print(B - A) # 차집합
print(A ^ B) # 대칭 차집합
```
**출력:**
```
{1, 2, 3, 4, 5, 6, 7}
{3, 4}
{1, 2}
{5, 6, 7}
{1, 2, 5, 6, 7}
```

집합 자체의 메소드 `add(item)`으로 `item`을 삽입할 수 있다. 삽입된 항목의 순서는 없다.

```python
basket = {'apple', 'orange', 'apple', 'pear'}
basket.add('banana')
basket
```
**출력:**
```
{'apple', 'banana', 'orange', 'pear'}
```

`[1, 2]`와 같은 수정 가능한 리스트는 집합의 원소가 될 수 없다. 그러므로 리스트를 삽입할 수 없다.

```python
myset = {0}
print(myset)
myset.add([1, 2]) # 오류
```
**오류:**
```
TypeError: unhashable type: 'list'
```

`(1, 2)`와 같은 수정 불가능한 튜플은 집합의 원소로 삽입할 수 있다.

```python
myset = {0}
myset.add((1, 2))
myset
```
**출력:**
```
{(1, 2), 0}
```

집합 메소드 `remove(item)`으로 원소 `item`을 삭제할 수 있다.

```python
myset.remove(0)
myset
```
**출력:**
```
{(1, 2)}
```
