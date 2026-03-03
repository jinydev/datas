---
layout: python
title: "3.5.3 추상화와 인터페이스"
---

# 3.5.3 추상화와 인터페이스 (Abstraction & Interface)

## 학습목표
본 장에서는 몸통 구현 없이 오직 자식 클래스가 반드시 지켜야 할 뼈대(규칙)만 세워두는 **'추상 베이스 클래스(ABC)'**의 통제 목적을 파악합니다. 파이썬만의 느슨하고 자유로운 '덕 타이핑(Duck Typing)' 문화 속에서도, 대형 프로젝트의 에러를 원천 봉쇄하기 위해 견고한 **인터페이스(Interface) 계약**을 어떻게 코드로 강제 조항화하는지 익힙니다.

설계가 복잡한 대형 시스템을 개발하다 보면 어떤 클래스들은 직접 인스턴스화하여 사용하기 위함이 아니라, 오직 수많은 **하위 클래스들이 반드시 지켜야 할 '엄격한 틀과 규칙'을 정의하는 데에만 목적**을 두는 경우가 있습니다. 상속과 다형성의 심화 과정인 **추상화(Abstraction)**에 대해 알아봅시다.

![Interface Blueprint Concept](/assets/images/oop/03_abstraction.png)
*(위 다이어그램: 추상적인 외곽선(인터페이스)이 제시한 고정된 규격 모양에, 구체적 구현물(클래스)들이 정확히 맞아떨어져 플러그인 되는 구조를 시각화합니다.)*



## 파이썬과 덕 타이핑 (Duck Typing)

인터페이스의 개념을 논하기에 앞서 파이썬의 독특한 특성을 짚고 넘어가야 합니다. 자바(Java)와 같은 엄격한 언어는 `interface`라는 예약어가 아예 따로 존재합니다. 하지만 파이썬은 철저히 **"만약 어떤 새가 오리처럼 걷고 오리처럼 꽥꽥거린다면, 그 새는 오리다"**라는 **덕 타이핑** 철학을 따릅니다.

파이썬에서는 클래스의 근본 태생이 무엇이든 간에, 객체가 호출에 필요한 속성과 메서드만 동일하게 가지고 있다면 전혀 문제 삼지 않고 동적으로 타입 판별을 넘깁니다. 즉, 굳이 인터페이스라는 강제적 규약을 시스템으로 만들지 않아도 개발자의 약속만으로 작동할 수 있다는 뜻입니다. 

그러나 시스템이 방대해지고 협업 인원이 늘어나면 이런 '느슨한 약속'만으로는 실수가 빈번해져 치명타를 입을 수 있습니다. 여기서 등장하는 것이 `abc` 모듈입니다.

## abc 패키지와 추상 베이스 클래스 (ABC)

파이썬은 공식적으로 `abc` (Abstract Base Classes) 모듈을 제공하여 강력한 통제를 요하는 추상 클래스를 작성할 수 있도록 돕습니다.

**추상 클래스란?**
- 오직 메서드의 '선언'만 존재하고 구현체(코드)는 없는 클래스입니다.
- 스스로는 인스턴스(객체)를 만들 수 없습니다. (예: `shape = Shape()` 형태로 생성 시 에러 발생)
- 반드시 자식 클래스가 이 추상 클래스를 상속받아 **구현을 완성(오버라이딩)**해야만 비로소 인스턴스화가 가능합니다. 이를 통해 **규칙을 엄격하게 강제**합니다.

```python
from abc import ABC, abstractmethod

# 추상 베이스 클래스 (반드시 ABC를 상속받아야 함)
class Shape(ABC):
    
    # @abstractmethod 데코레이터를 붙이면 추상 메서드가 됩니다.
    @abstractmethod
    def get_area(self):
        # 여기는 구현을 적지 않고 pass 하거나 Docstring만 적습니다.
        pass

# 에러 테스트
# s = Shape()
# TypeError: Can't instantiate abstract class Shape with abstract method get_area
```

## 인터페이스(추상화) 강제하기

자식 클래스가 Shape를 상속받았는데 실수로 `get_area` 메서드를 구현하지 않았다면 어떻게 될까요? 파이썬은 실행 단계가 아니라 자식 객체가 생성되는 그 순간 자체를 차단하여 방어합니다.

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    # get_area() 를 빼먹고 구현하지 않았을 경우!

# 테스트
# c = Circle(5)
# TypeError: Can't instantiate abstract class Circle with abstract method get_area
```

이처럼 예외와 실수를 원천봉쇄할 수 있습니다. 정상적으로 사용하려면 어떻게 해야할까요?

```python
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self): # 반드시 똑같은 이름으로 구현해야 함
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def get_area(self): # 반드시 똑같은 이름으로 구현해야 함
        return self.w * self.h

#  완벽하게 작동함
c = Circle(5)
r = Rectangle(4, 5)

print(f"원 넓이: {c.get_area()}")
print(f"사각형 넓이: {r.get_area()}")
```

## 요약

이처럼 **프로그래머 간의 통신용 계약서** 역할을 하는 것이 바로 객체지향의 추상화 인터페이스입니다.
1. `ABC`를 사용하여 '이것들은 반드시 구현해라'라는 틀 껍데기만 만들어 놓는다.
2. 하위 개발자는 본인의 용도에 맞게 그 틀 안을 구체적인 코드로 채워 완성한다.
3. 이를 통해 설계자는 시스템의 일관성을 100% 보장하면서도 다형성 파이프라인(파츠 조립)을 유지할 수 있다.

## 정리
단순히 혼자서 작은 스크립트를 짤 때는 추상화 같은 깐깐한 통제 장치가 오히려 거추장스러울 수 있습니다. 그러나 100명의 개발자가 협업하는 대규모 프레임워크나 외부 라이브러리(API) 환경에서는 "이 클래스 이름과 규격만큼은 하늘이 두 쪽 나도 무조건 빠짐없이 구현해 놔!"라고 강제하는 이 인터페이스(Interface) 계약서야말로 런타임 쇼크 에러를 100% 막아내는 최후의 철책선임을 깊이 새겨두면 좋습니다.
