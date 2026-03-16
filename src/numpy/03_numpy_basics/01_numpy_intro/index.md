---
layout: numpy
title: "4.1.1 과학용 컴퓨팅 패키지 numpy 개요"
---

# 4.3.1 넘파이 기초와 벡터/행렬의 이해

![파이썬 넘파이 연금술사](../img/numpy_basics.png)

<div style="text-align: center; margin: 30px 0;">
  <!-- SVG ndarray 차원 진화 애니메이션 -->
  <svg width="450" height="250" viewBox="0 0 450 250" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4fd1c5" />
        <stop offset="100%" stop-color="#319795" />
      </linearGradient>
      <linearGradient id="plateGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#e2e8f0"/>
        <stop offset="50%" stop-color="#cbd5e0"/>
        <stop offset="100%" stop-color="#e2e8f0"/>
      </linearGradient>
      <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
        <feDropShadow dx="2" dy="4" stdDeviation="3" flood-color="#a0aec0" flood-opacity="0.6"/>
      </filter>
    </defs>

    <!-- 배경 픽셀 그리드 은은하게 -->
    <path d="M0,50 L450,50 M0,100 L450,100 M0,150 L450,150 M0,200 L450,200" stroke="#f7fafc" stroke-width="2"/>
    <path d="M50,0 L50,250 M100,0 L100,250 M150,0 L150,250 M200,0 L200,250 M250,0 L250,250 M300,0 L300,250 M350,0 L350,250 M400,0 L400,250" stroke="#f7fafc" stroke-width="2"/>

    <!-- 1. Scalar (0D) -->
    <g transform="translate(60, 100)">
      <circle cx="0" cy="0" r="15" fill="#f6ad55" filter="url(#shadow)">
        <animate attributeName="cy" values="0; -10; 0" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="0" y="-30" font-family="Arial" font-size="12" font-weight="bold" fill="#718096" text-anchor="middle">0D (Scalar)</text>
    </g>

    <!-- 화살표 1 -->
    <path d="M90,100 L120,100" stroke="#cbd5e0" stroke-width="3" stroke-dasharray="5,3">
      <animate attributeName="stroke-dashoffset" from="16" to="0" dur="1s" repeatCount="indefinite"/>
    </path>

    <!-- 2. Vector (1D) -->
    <g transform="translate(160, 100)">
      <g filter="url(#shadow)">
        <rect x="-30" y="-15" width="20" height="30" fill="url(#boxGrad)" rx="2" stroke="#2c7a7b" stroke-width="1"/>
        <rect x="-10" y="-15" width="20" height="30" fill="url(#boxGrad)" rx="2" stroke="#2c7a7b" stroke-width="1"/>
        <rect x="10" y="-15" width="20" height="30" fill="url(#boxGrad)" rx="2" stroke="#2c7a7b" stroke-width="1"/>
      </g>
      <text x="0" y="-30" font-family="Arial" font-size="12" font-weight="bold" fill="#718096" text-anchor="middle">1D (Vector)</text>
      <!-- 반짝이는 스캐너 효과 -->
      <line x1="-35" y1="-20" x2="-35" y2="20" stroke="#3182ce" stroke-width="2" opacity="0.8">
        <animate attributeName="x1" values="-35; 35; -35" dur="3s" repeatCount="indefinite"/>
        <animate attributeName="x2" values="-35; 35; -35" dur="3s" repeatCount="indefinite"/>
      </line>
    </g>

    <!-- 화살표 2 -->
    <path d="M210,100 L240,100" stroke="#cbd5e0" stroke-width="3" stroke-dasharray="5,3">
      <animate attributeName="stroke-dashoffset" from="16" to="0" dur="1s" repeatCount="indefinite"/>
    </path>

    <!-- 3. Matrix (2D) -->
    <g transform="translate(290, 80)">
      <g filter="url(#shadow)">
        <animateTransform attributeName="transform" type="translate" values="0,0; 0,-5; 0,0" dur="3s" repeatCount="indefinite"/>
        <!-- 1행 -->
        <rect x="-30" y="0" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <rect x="-10" y="0" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <rect x="10" y="0" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <!-- 2행 -->
        <rect x="-30" y="20" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <rect x="-10" y="20" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <rect x="10" y="20" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <!-- 3행 -->
        <rect x="-30" y="40" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <rect x="-10" y="40" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
        <rect x="10" y="40" width="20" height="20" fill="#4299e1" rx="2" stroke="#2b6cb0" stroke-width="1"/>
      </g>
      <text x="0" y="-10" font-family="Arial" font-size="12" font-weight="bold" fill="#718096" text-anchor="middle">2D (Matrix)</text>
    </g>

    <!-- 화살표 3 -->
    <path d="M340,100 L370,100" stroke="#cbd5e0" stroke-width="3" stroke-dasharray="5,3">
      <animate attributeName="stroke-dashoffset" from="16" to="0" dur="1s" repeatCount="indefinite"/>
    </path>

    <!-- 4. Tensor (3D Stack) -->
    <g transform="translate(400, 70)">
      <g filter="url(#shadow)">
        <!-- 뒤쪽 레이어 -->
        <rect x="-20" y="0" width="30" height="40" fill="#718096" opacity="0.6"/>
        <!-- 중간 레이어 -->
        <rect x="-15" y="10" width="30" height="40" fill="#a0aec0" opacity="0.8"/>
        <!-- 앞쪽 레이어 (메인 Matrix) -->
        <rect x="-10" y="20" width="30" height="40" fill="#2b6cb0" stroke="#bee3f8" stroke-width="1">
          <animate attributeName="fill" values="#2b6cb0; #3182ce; #2b6cb0" dur="2s" repeatCount="indefinite"/>
        </rect>
        
        <!-- 행렬 선 긋기 장식 -->
        <line x1="-10" y1="33" x2="20" y2="33" stroke="#bee3f8" stroke-width="1" opacity="0.5"/>
        <line x1="-10" y1="46" x2="20" y2="46" stroke="#bee3f8" stroke-width="1" opacity="0.5"/>
        <line x1="0" y1="20" x2="0" y2="60" stroke="#bee3f8" stroke-width="1" opacity="0.5"/>
        <line x1="10" y1="20" x2="10" y2="60" stroke="#bee3f8" stroke-width="1" opacity="0.5"/>
      </g>
      <text x="0" y="0" font-family="Arial" font-size="12" font-weight="bold" fill="#718096" text-anchor="middle">3D (Tensor)</text>
    </g>

    <!-- 하단 설명 -->
    <rect x="75" y="170" width="300" height="30" fill="url(#plateGrad)" rx="15" opacity="0.8"/>
    <text x="225" y="190" font-family="monospace" font-size="13" font-weight="bold" fill="#2d3748" text-anchor="middle">.shape == (Depth, Rows, Columns)</text>

  </svg>
  <p style="color: #718096; font-size: 0.9em; margin-top: -10px;"><em>[그림] 점, 선, 면, 입체로 확장되는 ndarray 차원 진화</em></p>
</div>

## 1. 수학적 의미: 차원(Dimension)이란 무엇인가?
앞선 2장에서 우리는 변수가 폭발하는 연립방정식을 통제하기 위해 '행렬(Matrix)'이라는 숫자 타일 덩어리를 고안했습니다. 
이를 수학적 차원(Dimension) 공간과 연결해 보면, 형태에 따라 크게 4가지 등급으로 분류됩니다.

- **스칼라 (0D Tensor)**: 방향이 없는 단 하나의 점, 숫자입니다. (비유: `HP = 100`, 통장 잔고 1개)
- **벡터 (1D Tensor)**: 숫자들이 한 줄로 길게 늘어선 1차원 선분입니다. (비유: 일렬로 늘어선 기차, `[국, 영, 수]`)
- **행렬 (2D Tensor)**: 직사각형 표처럼 가로, 세로 2개의 축(행과 열)을 가진 평면 배열입니다. (비유: 엑셀 스프레드시트, 단일 흑백 이미지)
- **고차원 텐서 (3D+ Tensor)**: 행렬이 여러 장 겹쳐 입체가 된 덩어리 축입니다. (비유: 루빅스 큐브, 빛의 삼원색 RGB가 겹친 컬러 이미지)

## 2. 수기 계산 시뮬레이션: 파이썬 리스트의 한계
당신이 과일 상인이고 오늘 사과 3개 각각의 가격(100원, 200원, 300원)에 물가 상승률 10%를 모두 올려받고 싶다고 가정해 봅시다.
일반적인 수학 수기 노트였다면 괄호를 치고 밖에서 `1.1`을 곱해버리면 끝납니다. 즉, $1.1 \times [100, 200, 300]$.

하지만 기본 파이썬 리스트로 이 수학 계산을 시도하면 어떻게 될까요?
`[100, 200, 300] * 1.1` 은 파이썬 에러를 발생시킵니다. 어쩔 수 없이 `for` 문을 돌리며 승용차를 3번 탑승해 각각 수치를 곱하고 빈 리스트에 `append` 해야 합니다. 원소가 100만 개라면 자동차는 메모리 주소를 100만 번 찾아 헤매다 퍼져버립니다.

## 3. Numpy 강림: 다차원 배열(ndarray) 컨테이너 트럭 
바로 이때 데이터 과학의 핵심 엔진인 **Numpy(Numerical Python)**가 강림합니다. 
Numpy 제공하는 핵심 타입인 `ndarray`(N-Dimensional Array)는 오직 "규격화된 화물형 숫자"만 싣고 다니는 **대형 컨테이너 트럭**입니다. 
데이터가 메모리에 빈틈없이 일렬로 연속(Contiguous) 배치되어 있기 때문에, 방금 전 사과 가격 인상 문제 같은 것을 CPU가 순식간에 **한 번의 덧셈/곱셈 폭격(Vectorization)**으로 전멸시켜 버립니다. 루프(`for`문)가 필요 없는 세계에 오신 것입니다.

## 4. 실전 파이썬 예제
코드를 통해 직접 확인해 봅니다. Numpy를 불러와 1차원 벡터 기차를 만들고, 수학 공식을 통째로 던져보겠습니다.

```python
import numpy as np

# 파이썬 리스트를 넣으면, 강력한 연속 메모리 ndarray 기체로 조립됩니다.
prices = np.array([100, 200, 300]) 
print("타입:", type(prices)) 

# 1.1배 상수(스칼라) 곱셈 한 방 폭격! for 루프가 필요없습니다.
new_prices = prices * 1.1
print("인상된 가격:", new_prices)
```
**출력:**
```text
타입: <class 'numpy.ndarray'>
인상된 가격: [110. 220. 330.]
```
