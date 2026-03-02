---
layout: python
title: "3.5.2 상속과 다형성"
---

# 3.5.2 상속과 다형성 (Inheritance & Polymorphism)

객체지향 프로그래밍(OOP)이 수많은 개발자들에게 사랑받는 가장 큰 이유 중 하나는 코드를 매우 효율적으로 '재사용'하고 '확장'할 수 있다는 점입니다. 그 중심에는 흔히 부모와 자식 관계로 묘사되는 **상속(Inheritance)**이 있습니다.

![Inheritance Hierarchy Concept](/assets/images/oop/02_inheritance.png)
*(위 다이어그램: 부모 클래스의 유전 형질이 아래 레벨의 수많은 자식 클래스에게 그대로 전파되며 각자만의 고유한 영역으로 가지치기하는 구조)*

---

## 3.5.2 상속 (Inheritance) 이란?

현실 세계에서 부모가 자식에게 재산이나 유전적 특성을 물려주듯이, 파이썬에서는 **미리 만들어둔 클래스(부모 클래스)의 모든 속성과 메서드를 그대로 새로운 클래스(자식 클래스)에게 물려줄 수 있습니다.**
- **부모 클래스 (Parent/Super/Base Class)**: 물려주는 원본 클래스
- **자식 클래스 (Child/Sub/Derived Class)**: 물려받아 새롭게 확장하는 클래스

상속을 사용하면 중복된 코드를 여러 번 작성할 필요 없이, 공통 기능은 부모가 정의하고 자식은 본인만의 특별한 기능만 추가(확장)하면 됩니다.

### 상속의 기본 형태

```python
# 3.5.2 부모 클래스 선언
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹습니다.")

# 3.5.2 자식 클래스 선언 (괄호 안에 부모 클래스 이름을 넣습니다)
class Dog(Animal):
    def bark(self):
        print(f"{self.name}이(가) 멍멍 짖습니다!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name}이(가) 야옹하고 웁니다.")

# 3.5.2 활용
dog1 = Dog("바둑이")
dog1.eat()  # 부모인 Animal에게서 물려받은 메서드 사용 가능
dog1.bark() # 자신의 고유 메서드

cat1 = Cat("나비")
cat1.eat()
cat1.meow()
```

## 3.5.2 부모 호출: `super()`

자식 클래스에서 자체적인 생성자 `__init__`을 만들면 부모 클래스의 생성자는 자동으로 호출되지 않습니다. 이때 부모 클래스의 기능을 끌어와야 한다면 `super()` 함수를 사용합니다.

```python
class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name) # 부모 클래스인 Animal의 생성자를 강제 호출 (name 세팅)
        self.wing_span = wing_span # 자식 클래스만의 새로운 속성 추가
        
    def fly(self):
        print(f"{self.name}이(가) 날개를 폅니다. 길이는 {self.wing_span}cm 입니다.")

bird1 = Bird("참새", 20)
bird1.eat() # 정상 작동
bird1.fly()
```

## 3.5.2 메서드 오버라이딩 (Method Overriding)

부모에게 물려받은 기능이 마음에 들지 않으면 **자식 클래스에서 재정의(덮어쓰기)** 할 수 있습니다. 이를 오버라이딩이라고 부릅니다.

```python
class Duck(Animal):
    # 부모의 eat 메서드를 완전히 덮어씌움
    def eat(self):
        print(f"{self.name}이(가) 부리로 곡물을 쪼아 먹습니다.")

duck1 = Duck("도널드")
duck1.eat() # Animal의 "밥을 먹습니다"가 아닌, 오버라이딩된 결과물 출력
```

## 3.5.2 다형성 (Polymorphism)

'다형성'은 한자어로 '다양한 형태를 가진다'라는 뜻입니다. 프로그래밍 관점에서 다형성은 **하나의 메서드 이름으로 객체마다 서로 다른 동작을 수행**하게 만드는 객체지향의 꽃입니다.

위의 오버라이딩을 활용하면 완벽한 다형성을 구현할 수 있습니다. 코드로 살펴보겠습니다.

```python
animals = [Dog("멍멍이"), Cat("야옹이"), Duck("오리"), Animal("동물")]

for animal in animals:
    animal.eat() # 어떤 객체가 오든 동일하게 eat()을 호출하지만 결과는 각각 다릅니다!
```

**[출력문]**
> 멍멍이이(가) 밥을 먹습니다.  
> 야옹이이(가) 밥을 먹습니다.  
> 오리이(가) 부리로 곡물을 쪼아 먹습니다.  
> 동물이(가) 밥을 먹습니다.  

메인 루프는 리스트에 들어 있는 녀석이 강아지인지, 오리인지 알 필요 없이 무조건 `.eat()`만 지시하면 됩니다. 내부 로직은 개별 객체가 알아서 각자의 다형성에 맞게 처리하기 때문에, 코드가 극도로 유연해지고 확장성이 무제한에 가까워집니다.
