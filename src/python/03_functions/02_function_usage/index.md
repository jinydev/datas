---
layout: python
title: "3.3.2 함수 선언과 사용"
---

# 3.3.2 함수 선언과 사용

## 학습목표
본 장에서는 파이썬의 `def` 키워드를 이용해 직접 나만의 함수를 **선언 및 정의**하고 **호출**하는 실전 문법을 체득합니다. 다중 매개변수, 기본값(Default) 세팅, 그리고 한 번에 여러 값을 튜플로 묶어서 뱉어내는 파이썬만의 독특한 다중 반환(`return`) 기법을 능숙하게 다룰 수 있게 됩니다.

특정한 기능을 수행하는 함수를 직접 정의해 봅니다. 파이썬에서 사용자 정의 함수를 선언하려면 `def` 키워드 블록을 활용합니다.

## 기본 선언 구조

```python
def function_name(parameters):
    """함수에 대한 설명을 적는 독스트링(Docstring) 칸입니다."""
    function_body
    return value
```

- `function_name`: 함수의 이름. 이를 직접 호출할 수 있습니다.
- `parameters`: 매개변수. 함수에 인가해주는 외부 입력 재료입니다.
- `return value`: 함수 명령을 전부 수행한 뒤 본체로 다시 뱉어내는 완제품 결괏값입니다 (없으면 `None`을 기본 반환).

```python
# 매개변수와 반환값이 모두 있는 함수 선언
def add_two(x, y):
    result = x + y
    return result

print(add_two(3, 4)) # 작동 결과: 7
```

## 함수 호출 (Function Call)

앞서 배운 '쿠키 공장' 비유를 실제로 코드로 구현해 보겠습니다.

```python
def make_cookie(dough, sugar):  # 오븐 이름(함수명)과 재료 투입구(매개변수)
    print("반죽을 섞고 맛있게 굽습니다...")
    return dough + "맛 쿠키"      # 완성품 배출구 (반환값)

my_snack = make_cookie("초코", 30) 
print(f"내가 만든 간식: {my_snack}") # 결과: 초코맛 쿠키
```

함수 안에서 직전에 만든 또 다른 함수를 자유롭게 부를 수도 있습니다. 마치 일관된 작업을 분담해서 수행하는 통일된 공장처럼 여러 함수를 연쇄적으로 호출하여 하나의 큰 시스템을 설계하게 됩니다.

```python
def pack_box(flavor):
    print("상자를 준비합니다.")
    cookie = make_cookie(flavor, 10) # 내부에서 쿠키 굽는 함수를 연쇄 호출!
    print(f"{cookie}를 상자에 담았습니다!")
    return "선물 세트 완성"

print(pack_box("딸기"))
```

## 함수 매개변수 기본값 (Default Params)

매개변수의 설계상 자주 쓰이는 고정값이 있다면 `=` 연산자를 이용해 미리 기본값을 세팅해둘 수 있습니다. 이를 통해 유연한 함수 호출이 가능해집니다.

```python
def circle_area(r = 1):
    import math
    return math.pi * r**2

# 매개변수 값을 안주면 기본값(1)으로 처리
print("기본 면적:", circle_area())      

# 매개변수를 넘기면 해당 값(4.5)으로 덮어씌움
print("적용 면적:", circle_area(4.5))   

# 키워드 인자로 파라미터 이름을 명시할 수 있음
print("키워드 매칭:", circle_area(r=5.6))
```

## 다중 반환 (Multiple Returns)

반환해야 할 값이 여러 개 존재할 때, `return`에 콤마 `,`로 나열하면 파이썬은 이들을 통째로 하나의 튜플(Tuple) 구조로 묶어서 반환해주는 강력함을 탑재하고 있습니다.

```python
def sum_sub(x, y):
    plus = x + y
    minus = x - y
    return plus, minus

result = sum_sub(10, 3)
print(result) # (13, 7)
```

## 코딩 스타일 가이드 (PEP 8)
파이썬 언어 생태계는 PEP8 스타일을 가장 폭넓게 지지합니다.
- 함수명과 변수명은 모두 소문자로 하되, 띄어쓰기를 밑줄(`_`)로 처리하는 **스네이크 케이스(snake_case)** 규칙을 사용하세요. 
- 나쁜 예: `CalculateSum()`, 좋은 예: `calculate_sum()`

## 정리
드디어 남이 깎아 놓은 바퀴를 가져다 쓰는 수준을 넘어, 스네이크 케이스에 맞춰 내 코드베이스를 스스로 모듈화하는 창조자의 영역에 진입했습니다. 특히 `return plus, minus`처럼 여러 결과값을 한 번에 튜플 포장지로 깔끔하게 묶어 던지는 문법은 C나 자바 같은 언어 대비 파이썬이 가지는 극강의 표현식임을 꼭 체감하시기 바랍니다.
