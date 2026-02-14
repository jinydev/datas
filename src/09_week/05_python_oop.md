---
layout: home
title: "9주차 5강: 객체지향 프로그래밍 (OOP)"
---

# 9주차 5강: 객체지향 프로그래밍 (OOP)

> **학습목표**: 파이썬의 핵심 개념인 **객체(Object)**와 **클래스(Class)**를 이해하고, 나만의 데이터 타입을 만들어 봅니다. 판다스의 DataFrame도 결국 하나의 '객체'라는 것을 깨닫게 될 것입니다.

## 9.5.1. 클래스와 객체 (Class & Object)

가장 흔한 비유인 **붕어빵 틀(Class)**과 **붕어빵(Object)**으로 이해해 봅시다.

*   **클래스(Class)**: 설계도. "붕어빵은 이렇게 생겼고, 팥이 들어간다"라고 정의한 것.
*   **객체(Object/Instance)**: 설계도로 실제 찍어낸 결과물. "팥 붕어빵", "슈크림 붕어빵".

```python
# 1. 클래스 정의 (설계도 만들기)
class Dog:
    # 생성자 (__init__): 객체가 처음 만들어질 때 호출됨
    def __init__(self, name, breed):
        self.name = name   # 속성(Attribute)
        self.breed = breed

    # 메서드 (Method): 객체의 행동
    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다!")

# 2. 객체 생성 (실체 만들기)
my_dog = Dog("백구", "진돗개")
your_dog = Dog("초코", "푸들")

# 3. 사용하기
print(my_dog.name) # 백구
my_dog.bark()      # 백구가 멍멍 짖습니다!
```

<br>

---

<br>

## 9.5.2. `self`란 무엇인가?

클래스 안의 함수(메서드)에는 항상 첫 번째 인자로 `self`가 들어갑니다.
**`self`는 "나 자신(객체 그 자체)"을 가리킵니다.**

*   `my_dog.bark()`를 호출하면 파이썬은 내부적으로 `Dog.bark(my_dog)`처럼 처리합니다.
*   그래서 `bark` 함수 안에서 `self.name`을 쓰면 `my_dog.name`("백구")을 가져올 수 있는 것이죠.

<br>

---

<br>

## 9.5.3. 상속 (Inheritance)

이미 있는 클래스의 기능을 **물려받아서** 새로운 클래스를 만드는 것입니다. "재사용"의 끝판왕입니다.

```python
# Dog 클래스를 상속받은 'JindoDog' 클래스
class JindoDog(Dog):
    def hunt(self):
        print(f"{self.name}가 사냥을 합니다!")

# 부모(Dog)의 기능도 쓰고, 내 기능(hunt)도 쓰고!
dog2 = JindoDog("황구", "진돗개")
dog2.bark() # 부모님께 물려받은 기능
dog2.hunt() # 나만의 기능
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: **클래스**는 설계도이고, **객체**는 그 설계도로 만든 실체입니다.
*   **[핵심 2]**: **`__init__`**은 객체를 초기화(준비)하는 함수이며, **`self`**는 객체 자신을 가리키는 키워드입니다.
*   **[핵심 3]**: **상속**을 사용하면 기존 코드를 복사하지 않고도 기능을 확장하거나 재사용할 수 있습니다.
