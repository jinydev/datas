---
layout: python
title: "3.2.3 반복문 for와 while"
---

# 3.2.3 반복문 for와 while

![반복문의 개념: 조건을 만족할 때까지 끝없이 도는 쳇바퀴나 톱니바퀴](img/loops_concept.png)

타 프로그래밍 언어들은 루프(Loop)를 매우 중요하게 취급합니다. 왜냐하면 반복 작업 처리에 반복문 이외의 대안이 거의 없기 때문입니다. 반면 파이썬은 **리스트 내포(List Comprehension)**와 패키지의 **벡터화 연산(ex Numpy)**을 통해 반복 작업을 보다 간결하게 치환하는 경우가 많습니다. 그럼에도 불구하고 핵심 제어 구조인 `for`와 `while` 반복문은 흐름 명확성에 큰 이점이 있어 매우 기본적으로 알아야 합니다.

## 반복문 동작 흐름 (Mermaid)

반복문의 본질은 조건을 만족하는 동안 특정 블록의 코드를 끝없이 회전(Loop)시키는 것입니다. 아래 다이어그램은 반복문 기반 알고리즘의 전형적인 동작 흐름을 나타냅니다.

```mermaid
graph TD
    A([Start Loop]) --> B{반복 조건 평가<br/>(항목이 남았는가? / 참인가?)}
    B -- Yes/True --> C[반복 몸체(Body) 구문 실행]
    C --> B
    B -- No/False --> D([Exit Loop])
```

## 횟수와 구조 중심의 반복문 for

`for` 구문은 `in` 이후의 리스트, 튜플, 문자열 등 항목이 있는 집합적 구조를 하나씩 처음부터 끝까지 순회합니다. `for` 마지막 콜론 `:`은 반드시 필요하며 탭(Tab) 들여쓰기로 블록을 생성해야 합니다.

```python
# 3.2.3 내장 range(1, 6)을 이용해 1부터 5까지 반복
for x in range(1, 6):
    print(x)
```

모임형 자료형(리스트 안의 원소 등)을 직접 꺼낼 수도 있습니다.

```python
fruits = ["apple", 2500, "banana", 500]
for item in fruits:
    print(item)
```

## [유용한 테크닉] f-string과 zip() 함수의 결합
데이터를 짝지어서 출력할 때 최신 파이썬의 꽃인 **f-string** 포매팅 기법(Python 3.6+)과 `zip()` 내장 함수를 묶어서 사용하면 매우 가독성이 높습니다.
- **f-string**: 중괄호 `{}` 안에 변수나 표현식을 직접 삽입해 문자열을 동적으로 생성
- **zip()**: 여러 개의 객체를 병렬로 묶어 같은 인덱스끼리 튜플로 매칭

```python
names = ["John", "Alice", "Bob"]
ages = [25, 30, 22]

# 3.2.3 서로 다른 두 리스트를 zip으로 묶어 병렬 반복 순회
for name, age in zip(names, ages):
    # f"..." 형태로 간편하게 변수 삽입 문자열 출력
    print(f"Name: {name}, Age: {age}살")
```
**출력:**
```
Name: John, Age: 25살
Name: Alice, Age: 30살
Name: Bob, Age: 22살
```

##  조건 중심의 반복문 while

`while 조건식: 블록` 구문은 조건이 `True`인 동안은 영원히 블록을 반복 실행합니다. 

```python
i = 1
total = 0

#  i가 10 이하일 때까지만 계속 반복
while i <= 10:
    total += i
    i += 1  # 이 증감식이 없으면 끝나지 않음 (무한 루프)

print(total) # 결과: 55
```

## [유용한 테크닉] 무한 루프 탈출, break

만약 `while`의 조건식을 변수 없이 그냥 `True`로 강제 고정시켜버리면 이는 절대 스스로 끝나지 않는 무한 루프(Infinite Loop)가 됩니다. 이럴 땐 프로그램 내부에서 특정 종료 조건을 감지하여 `break` 명령어를 사용해 강제로 쳇바퀴를 깨부수고 탈출시킬 수 있습니다.

```python
i = 0
while True:  # 일단 영원히 반복!
    i += 3
    if i > 10:
        break    # 10을 초과하면 반복문을 강제로 파괴하고 종료함
    print(i)
```
**출력:**
```
3
6
9
```

## [종합 실습] 텍스트 RPG 전투 시스템 만들기

결론적으로 조건문(`if`), 반복문(`for` 또는 `while`), 그리고 자료구조(리스트)를 잘 버무리면 제법 복잡한 로직도 손쉽게 구현할 수 있습니다. 위에서 배운 개념들을 모두 활용해 간단한 전투 예제를 만들어 봅시다.

**시나리오:**
1. 플레이어의 초기 체력은 100입니다.
2. 몬스터 리스트의 몬스터를 순서대로 만납니다. (`for` 반복문)
3. 랜덤하게 공격 데미지를 입습니다.
4. 중간에 체력이 0 이하가 되면 `break`로 전체 게임 오버 처리를 합니다.

```python
import random # 랜덤 숫자를 뽑기 위한 모듈

player_hp = 100
monsters = ["Slime", "Wolf", "Dragon"]

print("⚔️ 모험을 시작합니다!")

for monster in monsters:
    print(f"\n--- {monster}와의 전투 시작! ---")
    
    # 10에서 50 사이의 랜덤 데미지 생성
    damage = random.randint(10, 50) 
    player_hp -= damage
    
    print(f"으악! {monster}에게 {damage}의 데미지를 입었습니다.")
    
    # 체력 체크 통제 구문 (if ~ else)
    if player_hp <= 0:
        print(f"체력이 {player_hp}이 되었습니다.")
        print("💀 Game Over... 눈앞이 캄캄해집니다.")
        break # 반복문을 즉시 종료하고 빠져나갑니다.
    else:
        print(f"휴... 남은 체력: {player_hp}")

# 3.2.3 전체 전투 반복문이 정상적으로 끝난 뒤 생존 확인
if player_hp > 0:
    print("\n🎉 축하합니다! 모든 몬스터를 물리치고 승리했습니다!")
```
