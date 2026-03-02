---
layout: mathplotlib
title: "5.1.5 그래프 속성과 스타일링"
---

## 5.1.5 그래프 속성과 스타일링 (Attributes & Styling)

Matplotlib의 핵심 속성(`Attribute`)들을 이해하고, 이를 조합하여 나만의 멋진 그래프를 디자인할 수 있습니다.

#### ① 주요 속성 (Key Attributes)

그래프를 꾸미는 것은 마치 캐릭터를 커스터마이징하는 것과 같습니다. Matplotlib이 제공하는 다양한 옵션을 알아봅시다.

* **색상 (Color, `c` 또는 `color`)**: 선의 색상을 지정합니다. `'b'`(파랑), `'g'`(초록), `'r'`(빨강), `'k'`(검정) 등의 약어나 HEX 코드를 사용할 수 있습니다.
* **마커 (Marker, `marker`)**: 데이터 포인트의 위치를 표시하는 도형입니다. `'.'`(점), `'o'`(원), `'^'`(삼각형), `'s'`(사각형), `'*'`(별) 등이 있습니다.
* **선 스타일 (Linestyle, `ls` 또는 `linestyle`)**: 선의 모양을 결정합니다. `'-'`(실선), `'--'`(파선), `':'`(점선), `'-.'`(쇄선) 등이 있습니다.
* **`linewidth` (lw)**: 선의 굵기 (기본값: 1.5)
* **`markersize` (ms)**: 마커의 크기
* **`alpha`**: 투명도 (0.0 ~ 1.0 사이, 0은 투명, 1은 불투명)
* **`label`**: 범례에 표시될 이름입니다. 이후 `plt.legend()`를 호출해야 표시됩니다.

#### ② 스타일링 종합 실습

다양한 속성들을 종합적으로 적용하여 두 시리즈의 데이터를 가진 직관적인 그래프를 그려보겠습니다. 용사와 몬스터의 레벨별 체력 성장을 비교하는 그래프입니다.

```python
import matplotlib.pyplot as plt

# 5.1.5 데이터 준비
level = [1, 2, 3, 4, 5]
hero_hp = [100, 120, 150, 190, 240]    # 용사 체력
monster_hp = [80, 130, 200, 300, 450]  # 몬스터 체력

plt.figure(figsize=(8, 5))

# 5.1.5 용사: 파란색 실선, 원(circle) 마커, 선굵기 2
plt.plot(level, hero_hp, label='Hero (용사)', c='b', ls='-', marker='o', lw=2)

# 5.1.5 몬스터: 빨간색 쇄선, X 마커, 선굵기 2
plt.plot(level, monster_hp, label='Monster (괴물)', c='r', ls='-.', marker='x', lw=2)

# 5.1.5 제목 및 축 레이블 꾸미기
plt.title("Hero vs Monster HP Growth", fontsize=15)
plt.xlabel("Level", fontsize=12)
plt.ylabel("HP", fontsize=12)

# 5.1.5 범례 표시 및 그리드 설정
plt.legend(fontsize=11)
plt.grid(True, axis='y', linestyle=':', alpha=0.5)

plt.show()
```

이처럼 각자의 특성을 살린 색과 스타일을 적용하면 정보를 명확하게 전달하는 멋진 그래프를 만들 수 있습니다.
