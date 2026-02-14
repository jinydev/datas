---
layout: home
title: "2주차 3강: 그래프 속성과 스타일링 (Attributes & Styling)"
---

# 2주차 3강: 그래프 속성과 스타일링 (Attributes & Styling)

> **학습목표**: Matplotlib의 핵심 속성(`Attribute`)들을 이해하고, 이를 조합하여 나만의 멋진 그래프를 디자인합니다.

## 2.3.1. 주요 속성 (Key Attributes)

그래프를 꾸미는 것은 마치 캐릭터를 커스터마이징하는 것과 같습니다. Matplotlib이 제공하는 다양한 옵션을 알아봅시다.

### 2.3.1.1. 색상 (Color, `c`)
선의 색상을 지정합니다. 색상 이름이나 HEX 코드를 사용할 수 있습니다.

| 색상 이름 (Name)       | 설명   | HEX 코드  |
| :--------------------- | :----- | :-------- |
| `'b'` 또는 `'blue'`    | 파란색 | `#0000FF` |
| `'g'` 또는 `'green'`   | 초록색 | `#008000` |
| `'r'` 또는 `'red'`     | 빨간색 | `#FF0000` |
| `'c'` 또는 `'cyan'`    | 청록색 | `#00FFFF` |
| `'m'` 또는 `'magenta'` | 자주색 | `#FF00FF` |
| `'y'` 또는 `'yellow'`  | 노란색 | `#FFFF00` |
| `'k'` 또는 `'black'`   | 검은색 | `#000000` |
| `'w'` 또는 `'white'`   | 흰색   | `#FFFFFF` |

### 2.3.1.2. 마커 (Marker, `marker`)
데이터 포인트의 위치를 표시하는 도형입니다.

| 마커  | 설명            | 예시          |
| :---: | :-------------- | :------------ |
| `'.'` | 점 (Point)      | 작은 점       |
| `'o'` | 원 (Circle)     | 동그라미      |
| `'v'` | 역삼각형        | 아래쪽 화살표 |
| `'^'` | 삼각형          | 위쪽 화살표   |
| `'s'` | 사각형 (Square) | 네모          |
| `'*'` | 별 (Star)       | 별 모양       |
| `'+'` | 플러스          | 더하기 기호   |

### 2.3.1.3. 선 스타일 (Linestyle, `ls`)
선의 모양을 결정합니다.

| 스타일 | 설명            | 모양   |
| :----: | :-------------- | :----- |
| `'-'`  | 실선 (Solid)    | ────── |
| `'--'` | 파선 (Dashed)   | ------ |
| `':'`  | 점선 (Dotted)   | ...... |
| `'-.'` | 쇄선 (Dash-dot) | -.-.-. |

### 2.3.1.4. 기타 속성
- **`linewidth` (lw)**: 선의 굵기 (기본값: 1.5)
- **`markersize` (ms)**: 마커의 크기
- **`alpha`**: 투명도 (0.0 ~ 1.0 사이, 0은 투명, 1은 불투명)
- **`label`**: 범례에 표시될 이름

---

## 2.3.2. [실습] 스타일링 종합 예제

위에서 배운 속성들을 모두 사용하여 그래프를 꾸며봅시다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
days = [1, 2, 3, 4, 5]
price = [100, 120, 110, 150, 170]

# 그래프 그리기 (속성 대잔치!)
plt.figure(figsize=(10, 6))

plt.plot(days, price, 
         color='green',          # 선 색상: 초록
         marker='o',             # 마커: 원
         linestyle='--',         # 선 스타일: 점선
         linewidth=2,            # 선 굵기: 2
         markersize=10,          # 마커 크기: 10
         markerfacecolor='yellow', # 마커 내부 색상: 노랑
         alpha=0.8,              # 투명도: 0.8
         label='Stock Price')    # 범례 이름

# 제목 및 축 설정
plt.title("Styling Practice", fontsize=20)
plt.xlabel("Day", fontsize=15)
plt.ylabel("Price ($)", fontsize=15)

# 그리드와 범례
plt.grid(True, axis='y', linestyle=':', alpha=0.5) # Y축에만 점선 그리드
plt.legend(fontsize=12, loc='upper left') # 범례 위치 지정

plt.show()
```

---

## 2.3.3. [도전] 게임 캐릭터 스탯 비교

두 캐릭터의 능력치를 한 그래프에 그려서 비교해 봅시다.

```python
# 데이터: 레벨에 따른 체력 변화
level = [1, 2, 3, 4, 5]
hero_hp = [100, 120, 150, 190, 240]    # 용사 체력
monster_hp = [80, 130, 200, 300, 450]  # 몬스터 체력

plt.figure(figsize=(8, 5))

# 용사: 파란색 실선, 원 마커
plt.plot(level, hero_hp, label='Hero', c='b', ls='-', marker='o', lw=2)

# 몬스터: 빨간색 쇄선, X 마커
plt.plot(level, monster_hp, label='Monster', c='r', ls='-.', marker='x', lw=2)

# 꾸미기
plt.title("Hero vs Monster HP Growth")
plt.xlabel("Level")
plt.ylabel("HP")
plt.legend()
plt.grid(True, alpha=0.3)

# 그래프 저장하기 (dpi=300 고해상도)
plt.savefig('hero_vs_monster.png', dpi=300)

plt.show()
```

> **인사이트**: 레벨 3부터 몬스터의 성장세가 가파릅니다. 초반 공략이 중요하겠군요!
