---
layout: python
title: "03. 다양한 에러 잡기"
description: "파이썬에서 여러 종류의 예외(IndexError, KeyError, ZeroDivisionError 등)가 발생했을 때 각각을 다르게 식별하여 분기 처리하는 방법을 배웁니다."
keywords: "파이썬, python, 다중 예외처리, 여러개 에러 잡기, IndexError, KeyError, ZeroDivisionError, Exception, try-except"
---

# 3. 다양한 에러 개별적으로 잡기

여러 종류의 각기 다른 에러를 하나로 퉁치지 않고 성격에 맞게 각각 다르게 분기 처리하여, 원인에 따라 맞춤형 대응이 가능하게 만들 수 있습니다.

![다중 예외 처리 라우팅 애니메이션](./img/multiple_exceptions_anim.svg)
*(다이어그램: 우편물을 분류하는 것처럼, 발생한 에러 객체의 종류와 일치하는 첫 번째 `except` 블록으로 떨어져 맞춤형 처리가 이루어지는 라우팅 과정을 묘사한 애니메이션입니다.)*

---

## 🛑 주요 예외 종류별 상세 설명

### 1. `KeyError` (키가 없음)
딕셔너리 자료형에서 내부에 존재하지 않는 키(Key) 값을 꺼내려고 시도할 때 발생합니다.
![KeyError 웹툰](./img/key_error_webtoon.png)
*(웹툰 비유: 책장이나 자물쇠(딕셔너리)에 맞는 열쇠(키)가 아예 없어 들어가지 않고 쩔쩔매고 있는 답답한 상황입니다.)*

### 2. `IndexError` (순번 초과)
리스트, 튜플 등 반복 가능한(Iterable) 자료형이 가지고 있는 실제 길이(크기)를 벗어난 범위를 허공에서 찾으려 할 때 발생합니다.
![IndexError 웹툰](./img/index_error_webtoon.png)
*(웹툰 비유: 딱 3칸짜리 작은 상자 안에서 10번째 물건을 꺼내려고 빈 허공을 뒤적이며 혼란에 빠진 모습입니다.)*

### 3. `ZeroDivisionError` (0으로 나누기)
수학적으로 정의될 수 없는 불가능한 연산인, 어떤 숫자를 분모 `0`으로 나누려고 시도할 때 터지는 에러입니다.
![ZeroDivisionError 웹툰](./img/zero_division_error_webtoon.png)
*(웹툰 비유: 계산기로 10을 0으로 나누자 블랙홀이 생겨나 주변 문서와 집기들을 모두 빨아들이고 있는 치명적인 수학 법칙 파탄 장면입니다.)*

### 4. `Exception` (나머지 모든 에러 방어)
위에서 구체적으로 지명하여 잡지 못한 미지의 예기치 않은 에러들을 전부 포괄하여 블랙홀처럼 잡아내는 최상위 방어망입니다.

---

## 💻 다중 예외 처리 코드 다형성 (Polymorphism)

위의 개념을 바탕으로, 우선순위에 따라 순서대로 `except` 블록을 구성하면 아래와 같은 강력한 무적의 방어 구조가 완성됩니다.

```python
try:
    # 💥 에러가 발생 가능한 복합적인 로직들
    my_dict = {"name": "Alice"}
    print(my_dict["age"]) # -> 여기서 KeyError 발생 시 곧바로 1번 블록으로 추락!
    
    number = 10 / 0 # -> ZeroDivisionError 발생 환경 구비 완료!
    
# 1번 블록: KeyError 방어
except KeyError:
    print("딕셔너리에 해당 키(항목)가 존재하지 않습니다!")
    
# 2번 블록: IndexError 방어
except IndexError:
    print("배열의 범위를 벗어난 접근입니다!")
    
# 3번 블록: ZeroDivisionError 방어
except ZeroDivisionError:
    print("수학적인 오류(0으로 나누기)가 발생했습니다!")
    
# 4번 블록: 최후의 보루 방어망
except Exception as e:
    # Exception은 모든 에러를 포괄하는 최상위 부모 클래스(부대장)입니다.
    # 특정하지 못한 나머지 모든 에러를 흡수하기 위해 반드시 맨 마지막 맨 밑에 배치해야 합니다.
    print(f"알 수 없는 치명적인 에러가 통보되었습니다: {e}")
```

> **[주의 사항]** 
> 위 코드에서 만약 `except Exception:` 블록을 첫 줄(맨 위)에 올려두면 그 어떤 에러든 간에 첫 번째 그물망에서 모두 걸려버리므로, 아래에 있는 상세 에러들(KeyError, IndexError 등)의 블록은 영원히 도달할 수 없는 `Dead Code`(죽은 코드)가 되어버립니다!

---

## 🎧 다중 예외 처리 & Vibe Coding

> **🗣️ 학생 프롬프트 (AI에게 이렇게 명령해 보세요):**
> "파이썬에서 딕셔너리(dictionary)와 리스트(list)를 둘 다 쓰는 코드를 하나 만들어봐. 이 코드 안에서는 `KeyError`와 `IndexError`가 각각 발생할 가능성이 있어. 다중 `except` 문을 사용해서 이 두 가지 에러를 어떻게 각각 따로 라우팅하여 별도의 메시지로 처리할 수 있는지, 친절한 주석이 달린 예제 코드와 쉬운 비유 설명을 덧붙여 줘."

---

## 📝 코딩 영단어 정복

* **Multiple**: 다수의, 복합적인. (여러 가지의 예외를 한꺼번에 다루는 다중 예외 처리에서 사용됩니다.)
* **Index**: 색인, 순번. (`IndexError`는 데이터가 정렬된 순번의 범위를 벗어날 때 발생하는 에러입니다.)
* **Key**: 열쇠, 핵심 식별자. (`KeyError`는 자물쇠(딕셔너리)를 열기 위한 정확한 열쇠 이름이 없을 때 발생합니다.)
* **Hierarchy**: 계층, 서열. (예외 클래스들의 족보/서열을 나타냅니다. `Exception`은 이 서열의 가장 높은 꼭대기에 있는 보스입니다.)
