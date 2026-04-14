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

**[출력 확인: 완벽하게 꾸며진 직관적인 차트]**

![Hero vs Monster 차트 마스터피스](img/hero_monster_style.svg)

> **💡 데이터 분석가의 시선**
> 용사(파란 선)는 초반에 안정적으로 성장하지만 후반부 성장폭이 둔화되는 반면, 괴물(빨간 점선)은 후반부 레벨 4~5 구간에서 **기하급수적(Exponential)**으로 체력이 뻥튀기됨을 시각적으로 단번에 파악할 수 있습니다!

이처럼 각자의 특성을 살린 색과 스타일을 적용하면, 단순히 예쁜 것을 넘어 **데이터의 숨겨진 이야기**를 듣는 사람에게 순식간에 전달하는 멋진 그래프 프레젠테이션이 가능해집니다.
