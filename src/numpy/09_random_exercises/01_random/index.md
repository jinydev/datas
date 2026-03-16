---
layout: numpy
title: "4.7.1 난수 생성"
---

# 4.9.1 데이터 창조의 마법사: 난수(Random)와 확률 모형

![난수 생성 무작위 추출기](../img/random_exercises.png)

<div style="text-align: center; margin: 30px 0;">
  <!-- SVG 무작위 난수 생성(Random Generator) 애니메이션 -->
  <svg width="500" height="260" viewBox="0 0 500 260" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- 구형 뽑기 기계 유리 반사광 -->
      <radialGradient id="glassSphere" cx="40%" cy="30%" r="60%">
        <stop offset="0%" stop-color="rgba(255,255,255,0.8)"/>
        <stop offset="60%" stop-color="rgba(226,232,240,0.3)"/>
        <stop offset="100%" stop-color="rgba(113,128,150,0.6)"/>
      </radialGradient>
      
      <!-- 난수 공 색상들 -->
      <radialGradient id="ballRed" cx="30%" cy="30%" r="70%">
        <stop offset="0%" stop-color="#fc8181"/><stop offset="100%" stop-color="#c53030"/>
      </radialGradient>
      <radialGradient id="ballBlue" cx="30%" cy="30%" r="70%">
        <stop offset="0%" stop-color="#63b3ed"/><stop offset="100%" stop-color="#2b6cb0"/>
      </radialGradient>
      <radialGradient id="ballYellow" cx="30%" cy="30%" r="70%">
        <stop offset="0%" stop-color="#fbd38d"/><stop offset="100%" stop-color="#c05621"/>
      </radialGradient>
      <radialGradient id="ballGreen" cx="30%" cy="30%" r="70%">
        <stop offset="0%" stop-color="#68d391"/><stop offset="100%" stop-color="#2f855a"/>
      </radialGradient>
    </defs>

    <!-- 배경 둥근 사각형 -->
    <rect x="0" y="0" width="500" height="260" fill="#f7fafc" rx="8"/>
    <text x="250" y="30" font-family="Arial" font-size="16" font-weight="bold" fill="#4a5568" text-anchor="middle">
      Numpy Random: 예측 불가능한 운명의 주사위
    </text>

    <!-- 1. 제너레이터 본체 (디지털 뽑기 기계) -->
    <g transform="translate(150, 140)">
      <!-- 기계 스탠드 -->
      <path d="M-40,90 L40,90 L20,30 L-20,30 Z" fill="#2d3748"/>
      <rect x="-50" y="90" width="100" height="10" fill="#1a202c" rx="2"/>
      
      <!-- 기계 내부에 튀는 공들 (Random Bouncing) -->
      <g stroke="#fff" stroke-width="1">
        <!-- 공 1 (Yellow) -->
        <circle cx="0" cy="0" r="10" fill="url(#ballYellow)">
          <animateTransform attributeName="transform" type="translate" values="-20,20; 30,-30; -10,-40; 20,10; -20,20" dur="2s" repeatCount="indefinite" />
        </circle>
        <!-- 공 2 (Blue) -->
        <circle cx="0" cy="0" r="10" fill="url(#ballBlue)">
          <animateTransform attributeName="transform" type="translate" values="30,-10; -20,-30; 10,20; -30,0; 30,-10" dur="2.5s" repeatCount="indefinite" />
        </circle>
        <!-- 공 3 (Red) -->
        <circle cx="0" cy="0" r="10" fill="url(#ballRed)">
          <animateTransform attributeName="transform" type="translate" values="-10,-40; -30,10; 30,20; 10,-30; -10,-40" dur="1.8s" repeatCount="indefinite" />
        </circle>
        <!-- 공 4 (Green) -->
        <circle cx="0" cy="0" r="10" fill="url(#ballGreen)">
          <animateTransform attributeName="transform" type="translate" values="10,20; -10,-10; 30,-20; -20,30; 10,20" dur="2.2s" repeatCount="indefinite" />
        </circle>
      </g>
      
      <!-- 구형 통 (반투명) -->
      <circle cx="0" cy="-10" r="60" fill="url(#glassSphere)" stroke="#cbd5e0" stroke-width="3"/>
      
      <!-- 배출구 파이프 -->
      <path d="M60,-20 L90,-20 L100,20 L60,20 Z" fill="#718096" stroke="#4a5568" stroke-width="2"/>
    </g>

    <!-- 2. 생성 및 배출되어 나열되는 난수 배열 -->
    <g transform="translate(260, 130)">
       <!-- 코드 라벨 -->
       <text x="60" y="-30" font-family="monospace" font-size="14" font-weight="bold" fill="#dd6b20" text-anchor="middle">.random(3)</text>
       
       <!-- 배열 박스 -->
       <rect x="0" y="0" width="130" height="40" fill="#edf2f7" stroke="#cbd5e0" stroke-width="2" rx="4"/>
       
       <!-- 날아와서 꽂히는 공 애니메이션 -->
       <!-- 첫 번째 칸 슬롯 -->
       <circle cx="20" cy="20" r="12" fill="url(#ballBlue)">
          <!-- 무한 반복 사이클 중 특정 타이밍에만 날아오고 정착함 -->
          <animateTransform attributeName="transform" type="translate" values="-50,-30; 0,0; 0,0; -50,-30" dur="3s" repeatCount="indefinite" keyTimes="0; 0.2; 0.9; 1"/>
       </circle>
       <text x="21" y="24" font-family="monospace" font-size="12" fill="white" font-weight="bold" text-anchor="middle">
         <animate attributeName="opacity" values="0; 1; 1; 0" dur="3s" repeatCount="indefinite" keyTimes="0; 0.2; 0.9; 1"/>
         0.1
       </text>

       <!-- 두 번째 칸 슬롯 -->
       <circle cx="65" cy="20" r="12" fill="url(#ballRed)">
          <animateTransform attributeName="transform" type="translate" values="-95,-30; -20,-10; 0,0; 0,0; -95,-30" dur="3s" repeatCount="indefinite" keyTimes="0; 0.2; 0.4; 0.9; 1"/>
       </circle>
       <text x="66" y="24" font-family="monospace" font-size="12" fill="white" font-weight="bold" text-anchor="middle">
         <animate attributeName="opacity" values="0; 0; 1; 1; 0" dur="3s" repeatCount="indefinite" keyTimes="0; 0.2; 0.4; 0.9; 1"/>
         0.8
       </text>

       <!-- 세 번째 칸 슬롯 -->
       <circle cx="110" cy="20" r="12" fill="url(#ballGreen)">
          <animateTransform attributeName="transform" type="translate" values="-140,-30; -40,-20; 0,0; 0,0; -140,-30" dur="3s" repeatCount="indefinite" keyTimes="0; 0.3; 0.6; 0.9; 1"/>
       </circle>
       <text x="111" y="24" font-family="monospace" font-size="12" fill="white" font-weight="bold" text-anchor="middle">
         <animate attributeName="opacity" values="0; 0; 1; 1; 0" dur="3s" repeatCount="indefinite" keyTimes="0; 0.3; 0.6; 0.9; 1"/>
         0.4
       </text>
    </g>

    <!-- 하단 부연설명 -->
    <text x="250" y="240" font-family="Arial" font-size="12" fill="#718096" text-anchor="middle">
      아무것도 없는 무의 공간에서, 혼돈(기상 예보, 주식 등)을 모델링하기 위한 통계적 난수 구슬을 뽑아냅니다.
    </text>
  </svg>
  <p style="color: #718096; font-size: 0.9em; margin-top: -10px;"><em>[그림] 예측할 수 없는 무작위 값을 연속으로 뽑아내어 배열 통에 채우는 랜덤 제너레이터(Generator)</em></p>
</div>

## 4.9.1 numpy의 난수와 다양한 함수

**[수학적 의미: 통계학과 카오스 이론의 모방]**
지금까지 우리는 항상 정해진 답(결정론적 방정식)만 탐구해 왔습니다. 하지만 자연계 현상이나 주사위 던지기, 주식 시장의 그래프처럼 불확실성(Uncertainty)으로 가득 찬 데이터를 분석하려면 통계학과 확률 모형이 필요합니다. 

**[비유로 이해하기: 게임 속 강화 확률과 주사위 굴리기]**
게임에서 아이템 강화 성공이나 몬스터 드랍률 같은 "확률적 파라미터(Weight)"를 딥러닝 인공지능이 초기 학습할 때 필수로 뿌리게 됩니다. Numpy의 `random` 모듈 삼 형제가 이 무작위 배열 생성 역할을 완벽하게 수행합니다.

- **`random()`**: 0~1 사이의 치우침 없는 실수 난수를 뽑습니다 (균등 분포, 뽑기 확률 설정용).
- **`standard_normal()`**: 평균 0, 표준편차 1인 종 모양 그래프에서 진짜 자연스러운 오차 데이터를 뽑아냅니다 (표준정규분포, 딥러닝 가중치 초기화용).
- **`integers()`**: 특정 범위 안에서 정수형 주사위를 굴립니다 (보드게임이나 정수 인덱스 무작위 추출용).

#### ① 난수 제너레이터

넘파이에서 제공하는 `numpy.random.default_rng`는 난수를 만드는 생성기(generator)의 생성자(constructor)이며, 여기서 마지막 이름 `rng`는 난수 생성기 RNG(Random Number Generator)이다. 난수 생성기는 PCG64로 O'Neill의 순열 합동 생성기를 128비트로 구현한 것이다. PCG64는 double 형의 난수와 부호 없는 32비트 및 64비트 정수를 생성하는 함수이다.

다음 코드로 실수 난수를 만드는 제너레이터를 하나 생성할 수 있다. 인자 12345는 비트제너레이터(BitGenerator)를 초기화하는 시드(seed) 값이다. 시드 값이 같으면 순서에 따라 난수가 발생하는 값이 동일하다.

```python
import numpy as np

rg = np.random.default_rng(12345)
rg
```
**출력:**
```
Generator(PCG64) at 0x...
```

#### ② 난수 제너레이터의 함수 random(), integers()

위 코드로 만든 제너레이터 변수 `rg`의 함수 `random()`을 호출하면 [0, 1) 사이의 실수(0에서 1 미만) 난수를 하나 생성할 수 있다.

```python
# 4.7.1 Generate one random float uniformly distributed over the range [0, 1)
r = rg.random()
r
```
**출력:**
```
0.22733602246716966
```

다음 코드로 난수 5개를 생성한다.

```python
rg.random(5)
```
**출력:**
```
array([0.94888115, 0.66723745, 0.09589794, 0.44183967, 0.88647992])
```

다음 코드로 [0, 1) 사이의 실수 난수 모양 (4, 3)의 2차원 배열이 생성된다.

```python
rg.random((4, 3))
```
**출력:**
```
array([[0.6974535 , 0.32647286, 0.73392816],
       [0.22013496, 0.08159457, 0.1598956 ],
       [0.34010018, 0.46519315, 0.26642103],
       [0.8157764 , 0.19329439, 0.12946908]])
```

함수 `rg.integers(low=0, high=10, size=3)`의 호출로 0에서 9까지의 정수 난수를 3개 만든다.

```python
import numpy as np

rg = np.random.default_rng(12345)

r = rg.integers(low=0, high=10, size=3)
r
```
**출력:**
```
array([0, 2, 4], dtype=int64)
```

키워드 인자가 아닌 위치 인자로 `rg.integers(1, 7, (3, 4))` 코드로도 생성할 수 있다.

```python
rg.integers(1, 7, (3, 4))
```
**출력:**
```
array([[5, 6, 4, 4],
       [2, 6, 4, 5]])
```

#### ③ 난수 제너레이터의 함수 standard_normal()

제너레이터 변수 `rg`의 함수 `standard_normal(10)`을 호출하면 표준정규분포(standard normal distribution)의 실수 난수를 10개 생성한다.

```python
import numpy as np

rg = np.random.default_rng(seed=42)

rg.standard_normal(10)
```
**출력:**
```
array([ 0.30471708, -1.03998411,  0.7504512 ,  0.94056472, -1.95103519,
       -1.30217951,  0.1278404 , -0.31624259, -0.01680116, -0.85304393])
```

다음 코드의 인자 `(4, 3)`은 배열의 모양`(shape)`으로 표준정규분포 난수 4행 3열의 2차원 배열을 생성한다.

```python
rg.standard_normal((4, 3))
```
**출력:**
```
array([[ 0.87939797,  0.77779194,  0.0660307 ],
       [ 1.12724121,  0.46750934, -0.85929246],
       [ 0.36875078, -0.9588826 ,  0.8784503 ],
       [-0.04992591, -0.18486236, -0.68092954]])
```
