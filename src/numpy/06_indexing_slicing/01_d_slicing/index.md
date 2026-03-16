---
layout: numpy
title: "4.4.1 1차원 배열의 첨자와 슬라이싱"
---

# 4.6.1 1차원 배열의 첨자와 슬라이싱

![배열 인덱싱과 레이저 커팅](../img/indexing_slicing.png)

<div style="text-align: center; margin: 30px 0;">
  <!-- SVG 배열 슬라이싱 및 인덱싱 애니메이션 -->
  <svg width="500" height="250" viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- 기본 데이터 블록 -->
      <linearGradient id="normalBlock" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#4a5568"/>
        <stop offset="100%" stop-color="#2d3748"/>
      </linearGradient>
      <!-- 선택된/추출된 데이터 블록 -->
      <linearGradient id="selectedBlock" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#48bb78"/>
        <stop offset="100%" stop-color="#2f855a"/>
      </linearGradient>
      <!-- 레이저 커터 글로우 -->
      <filter id="laserGlow" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
      <!-- 추출 블록 글로우 -->
      <filter id="extractGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="5" stdDeviation="4" flood-color="#48bb78" flood-opacity="0.6"/>
      </filter>
    </defs>

    <!-- 뒷배경 장식 -->
    <rect x="0" y="0" width="500" height="250" fill="#f7fafc" rx="8"/>
    <text x="250" y="30" font-family="Arial" font-size="16" font-weight="bold" fill="#4a5568" text-anchor="middle">
      Numpy Slicing: 정밀 데이터 추출
    </text>

    <!-- 원본 배열 (아래쪽) -->
    <g transform="translate(50, 160)">
      <text x="-20" y="20" font-family="monospace" font-size="14" font-weight="bold" fill="#a0aec0">a</text>
      
      <!-- 인덱스 번호 가이드 -->
      <g font-family="monospace" font-size="12" fill="#a0aec0" text-anchor="middle">
        <text x="25" y="-10">0</text>
        <text x="75" y="-10">1</text>
        <text x="125" y="-10" fill="#48bb78" font-weight="bold">2</text>
        <text x="175" y="-10" fill="#48bb78" font-weight="bold">3</text>
        <text x="225" y="-10" fill="#48bb78" font-weight="bold">4</text>
        <text x="275" y="-10">5</text>
        <text x="325" y="-10">6</text>
        <text x="375" y="-10">7</text>
      </g>

      <!-- 8개의 배열 블록 (1D Array) -->
      <!-- 인덱스 0, 1 -->
      <rect x="0" y="0" width="48" height="35" fill="url(#normalBlock)" rx="4"/>
      <text x="24" y="22" font-family="monospace" font-size="14" fill="#fff" text-anchor="middle">10</text>
      <rect x="50" y="0" width="48" height="35" fill="url(#normalBlock)" rx="4"/>
      <text x="74" y="22" font-family="monospace" font-size="14" fill="#fff" text-anchor="middle">20</text>
      
      <!-- 타겟 구역 박스 효과 (강조점) -->
      <rect x="100" y="-3" width="146" height="41" fill="none" stroke="#48bb78" stroke-width="2" stroke-dasharray="5,5" rx="5"/>
      
      <!-- 인덱스 2, 3, 4 (타겟 대상) -->
      <rect x="100" y="0" width="48" height="35" fill="url(#selectedBlock)" rx="4" opacity="0.3"/>
      <text x="124" y="22" font-family="monospace" font-size="14" fill="#a0aec0" text-anchor="middle">30</text>
      <rect x="150" y="0" width="48" height="35" fill="url(#selectedBlock)" rx="4" opacity="0.3"/>
      <text x="174" y="22" font-family="monospace" font-size="14" fill="#a0aec0" text-anchor="middle">40</text>
      <rect x="200" y="0" width="48" height="35" fill="url(#selectedBlock)" rx="4" opacity="0.3"/>
      <text x="224" y="22" font-family="monospace" font-size="14" fill="#a0aec0" text-anchor="middle">50</text>
      
      <!-- 인덱스 5, 6, 7 -->
      <rect x="250" y="0" width="48" height="35" fill="url(#normalBlock)" rx="4"/>
      <text x="274" y="22" font-family="monospace" font-size="14" fill="#fff" text-anchor="middle">60</text>
      <rect x="300" y="0" width="48" height="35" fill="url(#normalBlock)" rx="4"/>
      <text x="324" y="22" font-family="monospace" font-size="14" fill="#fff" text-anchor="middle">70</text>
      <rect x="350" y="0" width="48" height="35" fill="url(#normalBlock)" rx="4"/>
      <text x="374" y="22" font-family="monospace" font-size="14" fill="#fff" text-anchor="middle">80</text>
    </g>

    <!-- 슬라이싱 빔 커터 모션 -->
    <g transform="translate(150, 155)">
      <line x1="-3" y1="-80" x2="-3" y2="40" stroke="#f56565" stroke-width="2" filter="url(#laserGlow)" opacity="0">
        <animate attributeName="opacity" values="0; 1; 1; 0" dur="4s" repeatCount="indefinite" begin="0s"/>
      </line>
      <circle cx="-3" cy="-25" r="4" fill="#fff" filter="url(#laserGlow)" opacity="0">
        <animate attributeName="opacity" values="0; 1; 1; 0" dur="4s" repeatCount="indefinite" begin="0s"/>
        <animate attributeName="cy" values="-80; 40" dur="1s" repeatCount="indefinite" begin="0s"/>
      </circle>
    </g>
    <g transform="translate(298, 155)">
      <line x1="3" y1="-80" x2="3" y2="40" stroke="#f56565" stroke-width="2" filter="url(#laserGlow)" opacity="0">
        <animate attributeName="opacity" values="0; 1; 1; 0" dur="4s" repeatCount="indefinite" begin="0.5s"/>
      </line>
      <circle cx="3" cy="-25" r="4" fill="#fff" filter="url(#laserGlow)" opacity="0">
        <animate attributeName="opacity" values="0; 1; 1; 0" dur="4s" repeatCount="indefinite" begin="0.5s"/>
         <animate attributeName="cy" values="-80; 40" dur="1s" repeatCount="indefinite" begin="0.5s"/>
      </circle>
    </g>

    <!-- 공중으로 추출(Slicing)되어 올라가는 텐서 뷰 -->
    <g transform="translate(150, 80)">
       <!-- 위빙 모션 애니메이션 -->
       <animateTransform attributeName="transform" type="translate" values="150,150; 150,80; 150,80; 150,150" dur="4s" repeatCount="indefinite" keyTimes="0; 0.3; 0.8; 1"/>
       <g filter="url(#extractGlow)">
         <!-- 추출된 블록들 -->
         <rect x="0" y="0" width="48" height="35" fill="url(#selectedBlock)" rx="4" stroke="#68d391" stroke-width="2"/>
         <text x="24" y="22" font-family="monospace" font-size="14" fill="#fff" font-weight="bold" text-anchor="middle">30</text>
         <rect x="50" y="0" width="48" height="35" fill="url(#selectedBlock)" rx="4" stroke="#68d391" stroke-width="2"/>
         <text x="74" y="22" font-family="monospace" font-size="14" fill="#fff" font-weight="bold" text-anchor="middle">40</text>
         <rect x="100" y="0" width="48" height="35" fill="url(#selectedBlock)" rx="4" stroke="#68d391" stroke-width="2"/>
         <text x="124" y="22" font-family="monospace" font-size="14" fill="#fff" font-weight="bold" text-anchor="middle">50</text>
       </g>
    </g>

    <!-- 코드 스니펫 표시 중앙 상단 -->
    <rect x="180" y="55" width="140" height="30" fill="#2d3748" rx="4" opacity="0.9"/>
    <text x="250" y="75" font-family="monospace" font-size="16" font-weight="bold" fill="#68d391" text-anchor="middle">
      b = a[2:5]
    </text>

    <!-- 하단 설명 -->
    <text x="250" y="235" font-family="Arial" font-size="12" fill="#718096" text-anchor="middle">
      Start 위치(2)부터 Stop 위치(5) 직전까지의 데이터를 원본 구역에서 도려내어 띄워줍니다.
    </text>
  </svg>
  <p style="color: #718096; font-size: 0.9em; margin-top: -10px;"><em>[그림] 방대한 데이터 블록에서 원하는 구역만 레이저로 정밀 절단하는 슬라이싱 기술</em></p>
</div>

## 4.6.1 1차원 배열의 첨자와 슬라이싱

## 4.4.1 1차원 배열의 첨자와 슬라이싱

다음 코드로 1에서 9까지 제곱한 원소로 구성되는 1차원 배열 `a`로 구성된다.

```python
import numpy as np

a = np.power(np.arange(10), 2)
a
```
**출력:**
```
array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81], dtype=int32)
```

0부터 시작되는 정수 첨자로 배열을 참조할 수 있다. 끝부터 -1로 시작되는 음수도 가능하다.

```python
print(a[3])
print(a[-2])
```
**출력:**
```
9
64
```

`[start:stop]`의 슬라이싱으로 `start`에서 `stop-1` 까지의 부분 배열이 반환된다.

```python
print(a[1:4])
print(a[-5:-1])
```
**출력:**
```
[1 4 9]
[25 36 49 64]
```

`[start:stop:step]`의 슬라이싱에서 `start > stop`이면 오른쪽에서 왼쪽으로 `step` 위치의 원소로 구성된 배열이 반환된다.

```python
print(a[8:2:-1])
print(a[-1:-7:-1])
```
**출력:**
```
[64 49 36 25 16  9]
[81 64 49 36 25 16]
```

슬라이싱 `[::-1]`의 결과는 역순의 배열이 반환된다.

```python
a[::-1]
```
**출력:**
```
array([81, 64, 49, 36, 25, 16,  9,  4,  1,  0], dtype=int32)
```

```python
a[::-2]
```
**출력:**
```
array([81, 49, 25,  9,  1], dtype=int32)
```

다음 코드로 `a[2]`, `a[3]`, `a[4]`에 모두 -100이 대입된다.

```python
a[2:5] = -100
a
```
**출력:**
```
array([   0,    1, -100, -100, -100,   25,   36,   49,   64,   81], dtype=int32)
```

슬라이싱의 대상이 원소가 3개이므로 이에 맞는 배열을 대입해도 가능하다.

```python
a[2:5] = [-5, -5, -5]
a
```
**출력:**
```
array([ 0,  1, -5, -5, -5, 25, 36, 49, 64, 81], dtype=int32)
```

그러므로 다음 코드처럼 2개 원소의 배열을 대입하면 오류가 발생한다.

```python
a[2:5] = [-5, -5]
a
```
**오류:**
```
ValueError: could not broadcast input array from shape (2,) into shape (3,)
```

다음 `b`는 10개의 모든 원소가 5인 배열이다.

```python
b = np.array([5] * 10)
b
```
**출력:**
```
array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
```

다음 코드로 첨자 0, 2, 4, 6, 8에 -10이 저장된다.

```python
b[::2] = -10
b
```
**출력:**
```
array([-10,   5, -10,   5, -10,   5, -10,   5, -10,   5])
```

다음 코드는 첨자 0, 2, 4, 6, 8에 각각 0, 1, 2, 3, 4가 저장된다.

```python
b[::2] = np.arange(5)
b
```
**출력:**
```
array([0, 5, 1, 5, 2, 5, 3, 5, 4, 5])
```
