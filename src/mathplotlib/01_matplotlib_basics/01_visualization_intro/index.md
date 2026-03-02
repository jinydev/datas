---
layout: mathplotlib
title: "5.1.1 데이터 시각화 개요"
---

# 5.1.1 데이터 시각화 기초

## 5.1.1 데이터 시각화 개요

### ① 왜 시각화를 먼저 배울까요? (Why Visualization First?)

> **데이터 시각화(Data Visualization)**: 데이터의 숨겨진 패턴과 이야기를 찾아내는 **탐정의 돋보기**입니다.

숫자는 앤스콤의 4분할(Anscombe's Quartet) 예시처럼 평균과 분산이 같아도 실제 분포는 완전히 다를 수 있습니다. 숫자는 거짓말을 할 수 있지만 그리면 진실이 드러납니다. 우리는 파이썬의 핵심 문법을 익힌 뒤, 눈에 보이는 결과물을 만들어내며 데이터 분석의 흥미를 느끼고자 시각화를 먼저 다룹니다.

### ② 다양한 플롯 유형 (Plot Types)

| 플롯 유형 (Plot Type)          | 설명 (Description)                                 | 용도 (Usage)                      |
| :----------------------------- | :------------------------------------------------- | :-------------------------------- |
| **선 플롯 (Line Plot)**        | 데이터 포인트들을 선으로 연결한 그래프             | 📈 시계열 데이터, 추세 변화 확인   |
| **산점도 (Scatter Plot)**      | 두 변수 간의 관계를 점으로 표현                    | 🌌 상관관계 파악 (예: 키와 몸무게) |
| **막대그래프 (Bar Chart)**     | 범주별 데이터의 크기를 막대로 표현                 | 📊 데이터 비교 (예: 반별 성적)     |
| **히스토그램 (Histogram)**     | 데이터의 **분포(Distribution)**를 표현             | ⛰️ 데이터가 몰려있는 구간 확인     |
| **파이 차트 (Pie Chart)**      | 전체 데이터 중 각 부분의 **비율(Proportion)** 표현 | 🥧 점유율 확인 (예: 선거 득표율)   |

### ③ 데이터 시각화 패키지 matplotlib 개요

Matplotlib은 파이썬에서 2D 그래픽 그림을 생성하는 데 사용되는 데이터 시각화 라이브러리이다. 주로 과학 및 엔지니어링 분야에서 데이터를 시각적으로 탐색하고 표현하는 데 널리 사용되며, 다양한 차트, 플롯, 히스토그램 등을 생성할 수 있다.

![Matplotlib](img/page_002.png)

- **다양한 플롯 유형**: 선 플롯, 산점도, 막대 그래프, 히스토그램, 파이 차트, 3D 플롯 등 다양한 플롯 유형을 지원
- **높은 커스터마이징 가능성**: 그래프의 모든 요소에 대한 세부적인 제어가 가능하며, 플롯의 스타일, 색상, 레이블 등을 사용자가 자유롭게 커스터마이징이 가능
- **Jupyter 노트북 통합**: 주피터 노트북과 통합되어 대화형 환경에서 사용이 편리
- **다양한 출력 포맷 지원**: PNG, PDF, SVG, EPS 등 다양한 이미지 파일 형식으로 저장
- **내장된 텍스트 및 주석 지원**: 플롯에 텍스트와 주석을 추가하여 그림에 설명을 달 수 있음
- **세련된 색상 및 컬러맵**: 다양한 컬러맵과 색상을 활용하여 시각적인 표현을 높일 수 있음

### ② 설치 확인과 한글 처리 준비

다음 코드로 `numpy`와 `matplotlib`의 버전을 확인해 패키지 설치를 확인하자. 아나콘다는 기본으로 `numpy`와 `matplotlib`가 설치되어 있다. 설치가 안 되었다면 설치가 필요하거나 이미 설치된 인터프리터로 변경한다.

```python
import numpy as np
import matplotlib as mpl

print(np.__version__)
print(mpl.__version__)
```
**출력:**
```
1.24.3
3.7.1
```

다음은 노트북에서 그림을 선명하게 하는 명령이다.

```python
%config InlineBackend.figure_format = 'retina'
```

다음은 한글을 처리하기 위한 코드이다. `rc`는 실행 시간 환경 설정(runtime configuration)을 의미한다. 인터프리터에서 실행 시간에 한 번만 실행되면 이후에 영향을 미친다.

```python
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
```

위 문장은 다음 `plt.rcParams[]` 설정 문장으로도 가능하다.

```python
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
```