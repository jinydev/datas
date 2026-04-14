---
layout: pandas
title: "6.1.2 Series(시리즈) 개요"
---

# 6.1.2 Series (시리즈) 개요

**[수학적 의미: 인덱스를 가진 1차원 벡터(Vector)]**
수학에서 방향과 크기를 가진 1차원 배열(Vector) 개념에, 각 원소의 고유한 **주소 값(Index Label)**을 라벨링(Labeling)하여 매핑시킨 자료 구조입니다. 일반적인 배열이 `0, 1, 2...` 형태의 정수 위치로만 접근 가능하다면, 시리즈는 해시(Hash)맵처럼 문자로 된 이름표를 통해서도 데이터에 접근할 수 있습니다.

**[비유로 이해하기: 번호표가 붙어 있는 1열 서랍장]**
- 서랍장 한 칸 한 칸에 데이터(`Values`)가 들어 있고, 서랍장 겉면에는 네임펜으로 적어둔 이름표(`Index`)가 붙어 있습니다. 
- 시리즈 상단에는 이 서랍장의 전체 용도를 알려주는 명패(`Name`)가 달려 있습니다.
- 표의 관점에서는 **엑셀 시트에서 세로로 길게 한 줄(Column)만 추출한 형태**와 동일합니다.

---

### [1단계] Series의 핵심 3요소

판다스의 Series 객체는 다음 세 가지 주요 속성을 가집니다.
1. **Values (값)**: 실제 데이터가 담기는 공간입니다. 내부적으로 초고속 연산을 위한 NumPy 배열(`ndarray`) 형태로 저장됩니다.
2. **Index (인덱스/이름표)**: 값을 식별할 수 있는 레이블 키입니다. 기본값으로 `0, 1, 2...` 숫자가 배정되지만, 문자열(`'a', 'b', 'c'`)이나 날짜 등 원하는 형태의 이름표를 붙일 수 있습니다.
3. **Name (이름/명패)**: 이 시리즈 데이터 전체의 묶음 이름을 지정할 수 있습니다. 데이터프레임의 열(Column) 이름으로 자동 사용됩니다.

![Series 구조 애니메이션](./img/series_structure.svg)

---

### [2단계] Series 생성 맛보기

파이썬 리스트(List)를 기반으로 직접 인덱스와 이름을 지정하여 시리즈를 조립해 봅시다.

```python
import pandas as pd

# 1. 과일의 가격 데이터를 가지는 리스트 준비
prices = [1500, 3000, 2000, 500]

# 2. 각 데이터에 매칭될 이름표(Index) 준비
fruit_names = ["Apple", "Banana", "Orange", "Kiwi"]

# 3. Series 조립하기! (데이터명: '과일 단가표')
s = pd.Series(data=prices, index=fruit_names, name="과일 단가표")

print("🍎 판다스 Series 생성 완료:\n")
print(s)

# 내부 속성 훔쳐보기
print("\n--- 내부 구조 ---")
print("1) 값(values):", s.values)
print("2) 인덱스(index):", s.index)
print("3) 이름(name):", s.name)
```

**[실행 결과]**
```text
🍎 판다스 Series 생성 완료:

Apple     1500
Banana    3000
Orange    2000
Kiwi       500
Name: 과일 단가표, dtype: int64

--- 내부 구조 ---
1) 값(values): [1500 3000 2000  500]
2) 인덱스(index): Index(['Apple', 'Banana', 'Orange', 'Kiwi'], dtype='object')
3) 이름(name): 과일 단가표
```

![리스트 조립을 통한 Series 생성 과정](./img/series_creation.svg)

> **핵심 요약:** Series는 데이터(values), 데이터의 주소(index), 데이터의 테마(name)가 하나로 결합된 스마트한 1차원 데이터 보관함입니다!