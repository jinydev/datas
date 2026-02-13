# 8주차 2강: 데이터프레임 만들기 (Creation)

## 8.2.1. 딕셔너리로 만들기 (Dictionary to DataFrame)

가장 직관적인 방법은 "키(Key) = 열 이름", "값(Value) = 데이터 리스트" 형태로 만드는 것입니다.


<br>

---

<br>

### 8.2.1.1. 시나리오: 게임 캐릭터 명단 만들기

```python
import pandas as pd

# 데이터 준비 (딕셔너리)
data = {
    'Name': ['Hero', 'Mage', 'Tanker', 'Healer'],
    'Level': [10, 15, 8, 12],
    'Class': ['Warrior', 'Wizard', 'Knight', 'Priest']
}

# 데이터프레임 생성
df = pd.DataFrame(data)

print(df)
```

**[출력 결과]**
```
     Name  Level    Class
0    Hero     10  Warrior
1    Mage     15   Wizard
2  Tanker      8   Knight
3  Healer     12   Priest
```

- 자동으로 0, 1, 2, 3이라는 **인덱스(Index)** 번호가 붙은 것을 볼 수 있습니다.


<br>

---

<br>

## 8.2.2. 리스트로 만들기 (List of Lists)

행(Row) 단위로 데이터를 넣을 수도 있습니다. 이때는 열 이름을 따로 지정해줘야 합니다.

```python
# 데이터 (리스트의 리스트)
rows = [
    ['Sword', 100, 5000],
    ['Shield', 50, 3000],
    ['Potion', 0, 50]
]

# 열 이름 지정
columns = ['Item', 'Damage', 'Price']

df_items = pd.DataFrame(rows, columns=columns)
print(df_items)
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: (내용 채우기)
*   **[핵심 2]**: (내용 채우기)
*   **[핵심 3]**: (내용 채우기)
