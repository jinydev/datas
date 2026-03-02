---
layout: python
title: "3.4.2 사전"
---

# 3.4.2 사전

![Dictionary Concept Illustration](/assets/images/concept/05_dictionary.png)
*(사전/딕셔너리 개념도: 고유한 열쇠(Key)를 통해 특정 보관함의 데이터(Value)를 즉각적으로 찾아 꺼내는 구조)*

## 사전 개요와 생성 (Sequential vs Associative Array)

프로그래밍에서 데이터를 저장하는 방식은 크게 기차처럼 순서대로 나열되는 **순차 배열(Sequential Array, 예: 리스트)**과 사물함처럼 키를 통해 데이터에 직접 접근하는 **연관 배열(Associative Array, 예: 딕셔너리/사전)**로 나뉩니다.
"사과"가 어디 있는지 찾을 때 리스트는 첫 번째 칸부터 끝까지 다 열어봐야 하지만, 사전은 "사과"라는 **이름표(Key)**만 알면 그 즉시 위치를 찾아 꺼낼 수 있어(매우 빠름) 이름이나 ID로 데이터를 검색해야 할 때 안성맞춤입니다.

파이썬에서 사전(dictionary)은 키(key)와 값(value)의 쌍을 저장하는 자료형이다. 사전은 중괄호 `{ }`로 둘러싸여 있으며, 각 쌍은 쉼표 `,`로 구분되어 있다. 다음처럼 쉼표로 구분된 `키:값` 쌍들을 중괄호 `{ }`로 묶어 사전을 정의할 수 있다. 콜론 `:`은 각 키와 연관된 값을 구분한다.

- `{key1: value1, key2: value2, ..., keyn: valuen}`
    - `키: 값` 형태로 키와 값은 콜론 `:`으로 구분하며 항목들은 쉼표 `,`로 구분
    - 메소드 `items()`로 `(키, 값)` 항목의 목록 형태인 `dict_items`를 반환
    - `key1, key2, ..., keyn`: 키는 수정 불가능(또는 불변, immutable, hashable)한 자료형만 가능
    - 메소드 `keys()`로 키의 목록 형태인 `dict_keys`를 반환
    - `value1, value2, ..., valuen`: 값은 모든 자료형이 가능
    - 메소드 `values()`로 값의 목록 형태인 `dict_values`를 반환

다음은 사전의 특성이다.

- **데이터 조직화**: 키와 값의 쌍을 사용하여 데이터를 구조화하고 관리할 수 있다.
- **빠른 검색**: 키를 사용하여 값을 빠르게 찾을 수 있다.
- **중복 제거**: 사전은 키가 고유하므로 중복된 데이터를 쉽게 제거할 수 있다.

다음처럼 중괄호 `{ }`를 사용하여 사전을 생성할 수 있다. 키와 값을 콜론 `:`을 사용해 `키: 값`으로 구분된다. 사전의 자료형은 `class 'dict'`이다.

```python
mart = {'라면': 1200, '음료수': 1500, '과자': 800}
print(mart, type(mart))
```
**출력:**
```
{'라면': 1200, '음료수': 1500, '과자': 800} <class 'dict'>
```

사전은 키를 사용하여 값을 참조할 수 있다.

```python
print(mart['라면'])
print(mart['과자'])
print(mart['음료수'])
```
**출력:**
```
1200
800
1500
```

## [실전 예제] 게임 캐릭터 프로필 만들기 (사전 기초)

리스트가 번호(인덱스)로 데이터를 관리한다면, 딕셔너리(사전)는 **이름표(Key)**로 데이터를 관리하는 '금고'입니다.

```python
# 3.4.2 캐릭터 정보 생성 (Key: Value)
profile = {
    "name": "Antigravity",
    "level": 10,
    "hp": 100
}

# 3.4.2 데이터 확인 (Key로 Value 찾기)
print(profile["name"]) # 결과: Antigravity

# 3.4.2 데이터 수정 (레벨 업)
profile["level"] = 11 
print(f"레벨 업! 현재 레벨: {profile['level']}")

# 3.4.2 새로운 데이터 추가 (직업 전직)
profile["job"] = "Wizard" 
print(profile)
```

다음처럼 하나의 사전에 다양한 자료형의 키나 값을 사용할 수 있다. 다만 키는 수정할 수 없는 자료형인 `int`, `float`, `bool`, `str`, `tuple`, `frozenset` 등이 가능하다. 수정 가능한 자료형인 `list`, `set`, `dict`는 키가 될 수 없다.

```python
data = {1: '일', 3.14: 2.71, (1, 2): '튜플', 'list': [1, 2, 3]}
data
```

다음처럼 수정 가능한 리스트는 키로 사용할 수 없다.

```python
data = {1: '일', 3.14: 2.71, [1, 2]: '리스트', 'list': [1, 2, 3]}
```
**오류:**
```
TypeError: unhashable type: 'list'
```

내장 함수 `dict(item)`으로 사전을 만들 수 있다. 인자 `item`은 리스트나 튜플이면 가능하다. 리스트나 튜플은 키와 값을 갖는 리스트 또는 튜플을 항목으로 가질 수 있다.

```python
f_cnt = dict((('apple', 2), ('banana', 5), ('orange', 3)))
f_cnt
```
**출력:**
```
{'apple': 2, 'banana': 5, 'orange': 3}
```

특히, 다음처럼 과일 이름을 키로 하고 해당 과일 가격을 값으로 지정해 사전을 만들 수 있다. 여기서 생성된 키는 문자열이며, 각각 `apple`, `banana`, `orange`이나 기술은 따옴표 없이 기술해야 한다.

```python
f_price = dict(apple=4000, banana=3000, orange=2000)
f_price
```
**출력:**
```
{'apple': 4000, 'banana': 3000, 'orange': 2000}
```

## 항목 삽입과 메소드 keys()

사전에 없는 항목을 참조해 값을 대입하면 새로운 `키: 값`의 쌍이 추가된다. 다음 `mart['삼각김밥'] = 1700`으로 키 '삼각김밥'의 값 1700을 저장할 수 있다.

```python
mart = {'라면': 1200, '음료수': 1500, '과자': 800}

mart['삼각김밥'] = 1700
mart
```
**출력:**
```
{'라면': 1200, '음료수': 1500, '과자': 800, '삼각김밥': 1700}
```

이미 있는 항목을 참조해 값을 저장하면 이전 값이 수정된다.

```python
mart['과자'] = 900
mart
```
**출력:**
```
{'라면': 1200, '음료수': 1500, '과자': 900, '삼각김밥': 1700}
```

사전의 메소드 `keys()`는 사전의 모든 키를 자료형 `dict_keys`로 반환한다.

```python
mart.keys()
```
**출력:**
```
dict_keys(['라면', '음료수', '과자', '삼각김밥'])
```

사전의 메소드 `values()`는 사전의 모든 값을 자료형 `dict_values`로 반환한다.

```python
mart.values()
```
**출력:**
```
dict_values([1200, 1500, 900, 1700])
```

메소드 `items()`는 사전의 모든 키와 값의 쌍을 자료형 `dict_items`로 반환한다.

```python
mart.items()
```
**출력:**
```
dict_items([('라면', 1200), ('음료수', 1500), ('과자', 900), ('삼각김밥', 1700)])
```

## 사전을 다루는 추가 고급 메서드: get()과 update()

**1. `get()`: 안전하게 값 가져오기**
없는 키를 바로 찾으면 에러(`KeyError`)가 발생해 프로그램이 멈출 수 있습니다. `get()`을 쓰면 에러 대신 `None`이나 지정한 기본값을 반환하여 안전합니다.

```python
profile = {'name': 'Antigravity'}
# 3.4.2 print(profile['age']) # 에러 발생!

age = profile.get('age', 20) # 'age' 키가 없으면 기본값 20을 반환
print(age) # 3.4.2 ```

**2. `update()`: 딕셔너리 병합하기**
두 개의 딕셔너리를 하나로 합칩니다. 만약 키가 겹치면 뒤에 들어온 딕셔너리의 값으로 기존 값을 덮어씁니다.

```python
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
a.update(b)
print(a) # {'x': 1, 'y': 3, 'z': 4}
```

## 딕셔너리 컴프리헨션 (Dict Comprehension)

리스트 컴프리헨션처럼 딕셔너리도 한 줄로 우아하게 만들 수 있습니다. 전처리에서 매핑(Mapping) 테이블을 만들 때 매우 유용합니다.

```python
names = ['Alice', 'Bob', 'Charlie']
ids = [101, 102, 103]

# 3.4.2 두 리스트를 zip으로 합쳐서 딕셔너리로!
student_dict = {name: id_num for name, id_num in zip(names, ids)}

print(student_dict)
# 3.4.2 {'Alice': 101, 'Bob': 102, 'Charlie': 103}
```
