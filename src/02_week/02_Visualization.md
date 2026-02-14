---
layout: home
title: "2주차 1강: 데이터 시각화란? (Introduction)"
---

# 2주차 1강: 데이터 시각화란? (Introduction)

> **학습목표**: 데이터 시각화의 중요성을 이해하고(앤스콤의 4분할), 파이썬의 대표적인 시각화 라이브러리인 Matplotlib의 기본 구조(Figure, Axes)를 익힙니다.

## 2.1.1. 왜 시각화를 먼저 배울까요? (Why Visualization First?)

> **데이터 시각화(Data Visualization)**: 데이터의 숨겨진 패턴과 이야기를 찾아내는 **탐정의 돋보기**입니다.

보통 프로그래밍 수업은 지루한 문법부터 시작합니다. 하지만 우리는 반대로 합니다. **눈에 보이는 결과물**을 먼저 만들어보면 흥미가 생기고, 더 복잡한 코드도 배우고 싶어지기 때문입니다.

### 2.1.1.1. 숫자 vs 그림 (Numbers vs Pictures)
다음 두 가지 정보를 비교해 보세요.

**[정보 A: 숫자]**
```python
[10, 25, 40, 55, 70, 85, 100]
```
그냥 숫자들이 커지는구나... 정도만 알 수 있습니다.

**[정보 B: 그래프]**
(우상향하는 화살표나 그래프 이미지를 상상해 보세요 📈)
한눈에 "아! 성장이 가파르게 이루어지고 있구나!"라고 직관적으로 느낄 수 있습니다.

### 2.1.1.2. 앤스콤의 4분할 (Anscombe's Quartet)
유명한 예시로 '앤스콤의 4분할'이 있습니다. 평균, 분산 등 통계 수치는 모두 같지만, 그래프를 그려보면 전혀 다른 모양을 가진 4개의 데이터셋입니다.

```mermaid
graph LR
    A[데이터셋 1, 2, 3, 4] --> B{통계 분석}
    B --> C[평균 같음<br>분산 같음<br>상관계수 같음]
    C -- "숫자만 보면?" --> D[똑같은 데이터네? (오해)]
    
    A --> E{시각화}
    E --> F[모양 1: 선형<br>모양 2: 곡선<br>모양 3: 이상치<br>모양 4: 수직선]
    F -- "그려 보면?" --> G[전혀 다르네! (진실)]
    
    style D fill:#ffcccc,stroke:#333
    style G fill:#ccffcc,stroke:#333
```

**즉, 숫자는 거짓말을 할 수 있지만 그리면 진실이 드러납니다.**

---

## 2.1.2. Matplotlib 소개 및 다양한 플롯 (Introduction & Plot Types)

### 2.1.2.1. Matplotlib란?
> **"Matplotlib는 파이썬에서 정적, 애니메이션, 대화형 시각화를 생성하는 포괄적인 라이브러리입니다."**
> (Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.)

데이터 분석가들이 가장 먼저 배우는 시각화 도구로, 마치 **디지털 도화지와 물감**과 같습니다.

### 2.1.2.2. 다양한 플롯 유형 (Plot Types)
데이터의 성격에 따라 적절한 그래프를 선택해야 합니다.

```mermaid
mindmap
  root((데이터 시각화<br>선택 가이드))
    비교(Comparison)
      막대그래프(Bar)
      라인차트(Line) - 추세
    관계(Relationship)
      산점도(Scatter)
      히트맵(Heatmap)
    분포(Distribution)
      히스토그램(Histogram)
      박스플롯(Boxplot)
    구성(Composition)
      파이차트(Pie)
      누적막대(Stacked Bar)
```

| 플롯 유형 (Plot Type)          | 설명 (Description)                                 | 용도 (Usage)                      |
| :----------------------------- | :------------------------------------------------- | :-------------------------------- |
| **선 플롯 (Line Plot)**        | 데이터 포인트들을 선으로 연결한 그래프             | 📈 시계열 데이터, 추세 변화 확인   |
| **산점도 (Scatter Plot)**      | 두 변수 간의 관계를 점으로 표현                    | 🌌 상관관계 파악 (예: 키와 몸무게) |
| **막대그래프 (Bar Chart)**     | 범주별 데이터의 크기를 막대로 표현                 | 📊 데이터 비교 (예: 반별 성적)     |
| **히스토그램 (Histogram)**     | 데이터의 **분포(Distribution)**를 표현             | ⛰️ 데이터가 몰려있는 구간 확인     |
| **파이 차트 (Pie Chart)**      | 전체 데이터 중 각 부분의 **비율(Proportion)** 표현 | 🥧 점유율 확인 (예: 선거 득표율)   |
| **등고선 플롯 (Contour Plot)** | 3차원 데이터를 2차원 평면에 등고선으로 표현        | 🗺️ 지형, 높이, 밀도 표현           |

### 2.1.2.3. 라이브러리 설치 및 불러오기
Colab에는 이미 설치되어 있지만, 로컬 환경(VS Code)에서는 설치가 필요합니다.

```bash
pip install matplotlib
```

보통 `plt`라는 별명(alias)으로 줄여서 부릅니다.
```python
import matplotlib.pyplot as plt
```

---

## 2.1.3. Matplotlib의 기본 구조 (Anatomy of a Plot)

그림을 그리기 위해 도구의 명칭을 정확히 알아야 합니다.

```mermaid
classDiagram
    class Figure {
        전체 도화지
        (Title, Legends)
    }
    class Axes {
        실제 그래프 영역
        (Plotting Area)
    }
    class Axis {
        X축, Y축
        (Ruler)
    }
    
    Figure *-- Axes : 포함 (1개 이상)
    Axes *-- Axis : 포함 (X, Y)
    
    note for Figure "가장 큰 틀\n(Window)"
    note for Axes "서브플롯\n(Subplot)"
```

- **Figure (그림)**: 전체 도화지입니다. 그래프가 그려지는 가장 큰 틀입니다.
- **Axes (축)**: 실제 그래프가 그려지는 영역입니다. 하나의 Figure 안에 여러 개의 Axes(서브플롯)가 들어갈 수 있습니다.
- **Axis (축 눈금)**: X축(X-Axis)과 Y축(Y-Axis)입니다.

다음 시간부터 이 도구들을 이용해 본격적으로 그림을 그려보겠습니다. 🎨
