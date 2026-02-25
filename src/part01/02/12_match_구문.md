---
layout: docs
title: "02. match 구문"
---

## 02. match 구문

파이썬 구문 `match`는 자바, C 언어의 `switch` 구문과 비슷하며 다음 형식과 같다. 구문에서 `match`와 `case`, `default`는 키워드이다. 연산식 또는 변수 `exp`의 값을 각 `case`의 `value1`, `value2` 등과 비교하고, 첫 번째로 일치하는 `case`를 찾으면 해당 `case` 이후의 블록인 `statements`를 실행한다. 어떤 `case`와도 일치하지 않으면 옵션인 `case _:` 이후의 블록을 실행한다.

```python
match exp:
    case value1:
        statements
    case value2:
        statements
    case _:
        statements
```

- `exp`: `match` 구문에서 평가할 식(expression)이나 변수이며, 이 값이 어떤 `case`와 일치하는지 확인
- `value1`, `value2`, ...: 여러 개의 경우(case)를 정의하며, `exp`의 값과 각 경우를 비교
- `statements`: 각 경우에 해당하는 실행 문장이 정의되는 블록으로, `exp`의 값이 해당하는 경우, 해당 블록이 실행

다음 구문 `match` 문장에서 `value`가 `apple`이므로 `case 'apple'`에 적용되어 출력 값은 사과이다.

```python
value = "apple"
match value:
    case 'apple':
        result = "사과"
    case 'banana':
        result = "바나나"
    case _:
        result = "기타"

print(result)
```
**출력:**
```
사과
```

다음은 `value`가 `banana`이므로 `result`에 저장된 값은 바나나이다.

```python
value = "banana"
match value:
    case 'apple':
        result = "사과"
    case 'banana':
        result = "바나나"

print(result)
```
**출력:**
```
바나나
```

다음은 `mango`로 비교할 값이 `case`에 없으므로 `case _:` 블록이 실행되어 `None`이 출력된다.

```python
value = "mango"

match value:
    case 'apple':
        result = "사과"
    case 'banana':
        result = "바나나"
    case _:
        result = None

print(result)
```
**출력:**
```
None
```
