---
layout: home
title: "1주차 2강: 파이썬 기초 1 (Python Basics 1)"
---

# 1주차 2강: 파이썬 기초 1 (Python Basics 1)

> **학습 목표**
> 1.  파이썬의 기본 구조와 실행 방법을 이해합니다.
> 2.  **변수(Variable)**와 **자료형(Data Type)**의 개념을 익힙니다.
> 3.  **입출력(Input/Output)**과 **문자열(String)**을 다루는 방법을 배웁니다.

## 1.2.1. 파이썬의 시작 (Hello World)

프로그래밍의 전통에 따라 첫 번째 코드는 화면에 인사를 출력하는 것입니다.

```python
print("Hello, Python!")
```

-   `print()`: 괄호 안의 내용을 화면에 출력하는 **함수(Function)**입니다.
-   `"Hello, Python!"`: 따옴표(`"`)로 감싸진 글자를 **문자열(String)**이라고 합니다.

---

## 1.2.2. 변수와 자료형 (Variables & Data Types)

### 1.2.2.1. 변수 (Variable)
변수는 데이터를 담는 **그릇**입니다. 그릇에 이름을 붙여서 데이터를 저장하고 꺼내 씁니다.

```python
name = "Antigravity"
level = 1
hp = 100.5
```

-   `=` 등호는 "같다"는 뜻이 아니라, **"오른쪽의 값을 왼쪽 변수에 넣어라(할당해라)"**는 뜻입니다.

### 1.2.2.2. 자료형 (Data Type)
변수에 담기는 데이터의 종류입니다.

| 자료형                     | 설명               | 예시                     |
| :------------------------- | :----------------- | :----------------------- |
| **int** (Integer)          | 정수 (소수점 없음) | `1`, `-5`, `100`         |
| **float** (Floating-point) | 실수 (소수점 있음) | `3.14`, `100.5`, `-0.01` |
| **str** (String)           | 문자열 (텍스트)    | `"Hello"`, `'Python'`    |
| **bool** (Boolean)         | 참/거짓 (논리값)   | `True`, `False`          |

```python
# 자료형 확인하기: type() 함수
print(type(name))   # <class 'str'>
print(type(level))  # <class 'int'>
```

---

## 1.2.3. 기본 연산 (Basic Operations)

컴퓨터는 계산기(Computer)에서 유래했습니다. 기본적인 사칙연산을 해봅시다.

```python
a = 10
b = 3

print(a + b)  # 덧셈: 13
print(a - b)  # 뺄셈: 7
print(a * b)  # 곱셈: 30
print(a / b)  # 나눗셈: 3.3333... (결과는 항상 실수)
print(a // b) # 몫: 3 (정수 나눗셈)
print(a % b)  # 나머지: 1 (중요! 짝수/홀수 판별 등에 사용)
print(a ** b) # 거듭제곱: 1000 (10의 3승)
```

---

## 1.2.4. 문자열 다루기 (String Manipulation)

데이터 분석에서 텍스트 데이터 처리는 매우 중요합니다.

### 1.2.4.1. 문자열 연결
```python
first_name = "Harry"
last_name = "Potter"
full_name = first_name + " " + last_name
print(full_name) # Harry Potter
```

### 1.2.4.2. f-string (포맷팅)
문자열 안에 변수를 쏙 집어넣는 가장 편리한 방법입니다. 문자열 앞에 `f`를 붙이고, 변수를 `{}` 안에 넣으세요.

```python
name = "Iron Man"
age = 45
print(f"I am {name}, and I am {age} years old.")
# 출력: I am Iron Man, and I am 45 years old.
```

### 1.2.4.3. 인덱싱과 슬라이싱 (Indexing & Slicing)
문자열의 특정 부분을 뽑아냅니다. **파이썬은 숫자를 0부터 셉니다.**

```python
text = "ABCDEFG"

print(text[0])   # 첫 번째 글자: 'A'
print(text[1])   # 두 번째 글자: 'B'
print(text[-1])  # 마지막 글자: 'G'

print(text[0:3]) # 0번부터 3번 '직전'까지: 'ABC' (0, 1, 2)
```

> **[실습]** 자신의 이름과 나이를 변수에 저장하고, f-string을 사용하여 자기소개를 출력해 보세요.