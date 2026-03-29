---
layout: numpy
title: "02. 데이터 블록과 시공간 왜곡 (행렬 사전학습)"
---

# 2. 고대 암호판에서 GPU 텐서 파괴신으로: 행렬 이야기

## 4.2 데이터 블록과 시공간 왜곡 (행렬)

![선형대수학과 매트릭스의 세계](img/matrices_intro.png)

<div style="text-align: center; margin: 30px 0;">
  <!-- SVG 시공간 외곡(선형 변환) 애니메이션 -->
  <svg width="400" height="250" viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- 행렬 블록 필터 효과 -->
      <filter id="blockGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>

    <!-- 배경 십자 좌표계 -->
    <path d="M200,20 L200,230 M20,125 L380,125" stroke="#a0aec0" stroke-width="2" />
    
    <!-- 오리지널 베이직 그리드 (희미하게 배경 유지) -->
    <g stroke="#e2e8f0" stroke-width="1" opacity="0.4">
      <path d="M150,25 L150,225 M250,25 L250,225" />
      <path d="M50,75 L350,75 M50,175 L350,175" />
    </g>

    <g transform="translate(200, 125)">
      <!-- 변환 애니메이션을 받는 벡터 컴포넌트 -->
      <g>
        <!-- 행렬 선형 변환 스큐 애니메이션 (시공간 왜곡 효과) -->
        <animateTransform 
          attributeName="transform" 
          type="skewX" 
          values="0; 30; 0; -30; 0" 
          dur="6s" 
          repeatCount="indefinite" 
          calcMode="easeInOut"
        />
        <animateTransform 
          attributeName="transform" 
          type="scale" 
          values="1; 1.2; 1; 0.8; 1" 
          dur="6s" 
          repeatCount="indefinite" 
          calcMode="easeInOut"
          additive="sum"
        />

        <!-- 왜곡되는 그리드망 -->
        <g stroke="#4299e1" stroke-width="1.5" opacity="0.6" stroke-dasharray="4,4">
          <path d="M-50,-100 L-50,100 M50,-100 L50,100" />
          <path d="M-150,-50 L150,-50 M-150,50 L150,50" />
        </g>
        
        <!-- 중앙 행렬 [A] 큐브 시각화 -->
        <rect x="-30" y="-30" width="60" height="60" fill="#2b6cb0" opacity="0.8" rx="8" filter="url(#blockGlow)"/>
        
        <!-- 데이터 점들 -->
        <circle cx="50" cy="-50" r="5" fill="#f6ad55" />
        <circle cx="-50" cy="50" r="5" fill="#f6ad55" />
        <circle cx="50" cy="50" r="5" fill="#f6ad55" />
        <circle cx="-50" cy="-50" r="5" fill="#f6ad55" />
        
        <!-- 중앙에서 뻗어나가는 변환 벡터 선 -->
        <path d="M0,0 L50,-50" stroke="#fbd38d" stroke-width="2">
          <animate attributeName="stroke-dasharray" values="0,100; 100,0" dur="2s" repeatCount="indefinite"/>
        </path>
        <path d="M0,0 L-50,50" stroke="#fbd38d" stroke-width="2">
          <animate attributeName="stroke-dasharray" values="0,100; 100,0" dur="2s" repeatCount="indefinite"/>
        </path>
      </g>
    </g>

    <!-- 행렬 수식 디스플레이 -->
    <rect x="20" y="20" width="100" height="60" fill="white" stroke="#e2e8f0" stroke-width="2" rx="4" opacity="0.9"/>
    <text x="70" y="45" font-family="monospace" font-size="14" font-weight="bold" fill="#2d3748" text-anchor="middle">[ 1  2 ]</text>
    <text x="70" y="65" font-family="monospace" font-size="14" font-weight="bold" fill="#2d3748" text-anchor="middle">[ 0  1 ]</text>
    <text x="70" y="100" font-family="Georgia, serif" font-size="12" fill="#718096" text-anchor="middle" font-style="italic">Shear Matrix</text>
  </svg>
  <p style="color: #718096; font-size: 0.9em; margin-top: -10px;"><em>[그림] 행렬을 통한 평면 좌표계의 찌그러짐 (선형 변환)</em></p>
</div>

1단원인 방정식에서 수백 개의 미지수(x, y, z...)가 서로 얽혀 있을 때의 계산 한계를 돌파하기 위해, 선형대수학과 행렬(Matrix)이 등장했습니다. 숫자를 일직선으로만 배열하던 것에서 가로(행)와 세로(열)의 직사각형 체계(블록)로 정렬하면서 우리는 기하학 공간 자체를 조작할 수 있는 엄청난 힘을 얻게 되었습니다.
이번 단원에서는 수만 개의 방정식이 무너진 잔해 속에서 왜 행렬이 필연적으로 태어날 수밖에 없었는지 복습하며, 가로줄(행)과 세로줄(열)의 데이터베이스 통제 법칙을 알아봅니다.
나아가 행렬끼리 더하고, 스칼라를 곱하며, 가장 악명 높은 **내적(Dot Product) 충돌의 미스터리**를 셀로판지와 미사일 비유로 파헤칩니다. 마지막으로 단순해 보이는 숫자 배열이 어떻게 2차원 시공간을 찌그러뜨리고 돌리는 그래픽 **선형 변환 스펠**로 진화하며, 오늘날 AI 두뇌(GPU 텐서)의 핵심 모터로 폭주하게 되었는지 직관적으로 흡수합니다.

## 목차 (Table of Contents)

* [00. 왜 갑자기 행렬인가? (방정식의 한계)](./00_intro_equations_limit/)
  - 미지수가 늘어날 때 텍스트 기반 방정식이 겪는 연산 병목 현상과, 계수만 따로 뽑아내는 행렬 탄생의 아이디어를 확인합니다.
* [01. 데이터베이스 격자 타일링: 행렬의 구조](./01_what_is_matrix/)
  - 영화관 좌석표와 엑셀 배열을 통해, 행(Row)과 열(Column)이 데이터를 어떻게 압축하고 호출(Index)하는지 파악합니다.
* [02. 픽셀의 병합 (행렬의 덧셈과 뺄셈)](./02_addition_subtraction/)
  - 크기가 같은 직사각형 이미지(셀로판지) 두 장의 위치 픽셀값이 서로 어떻게 융합하는지 시각적인 덧셈 법칙을 관찰합니다.
* [03. 스케일 폭주 버프 (스칼라 실수배)](./03_scalar_multiplication/)
  - 하나의 외부 수치(스칼라)가 거대 행렬 내부의 모든 요소에게 동시다발적으로 침투해 배율을 증폭시키는 원리를 배웁니다.
* [04. 행과 열의 십자 충돌 (곱셈의 미스터리)](./04_matrix_multiplication/)
  - 얌전한 덧셈과 달리, 가로본능과 세로본능이 격돌하며(내적 충돌) 다항식의 대입 과정에서 발생했던 곱셈 규칙의 끔찍한(?) 진실을 폭로합니다.
* [05. 시공간 변환 마법진 (선형 변환)](./05_linear_transformation/)
  - 행렬을 화살표 벡터에 곱하는 순간, 화면 상의 물체들이 늘어나고 회전하며 평면 공간 자체가 왜곡되는 3D 그래픽 엔진의 비밀을 엿봅니다.
* [06. 마지막 승부: GPU 텐서 폭격과 파이썬 Numpy 로의 접속](./06_intro_to_numpy_ai/)
  - 순차 계산형 CPU로는 감당할 수 없는 수억 개의 병렬 충돌(행렬 폭격)을, 수만 개의 단순 로봇 GPU 공장과 파이썬 조종기 `Numpy`가 어떻게 제압하는지 총정리하며 본격적인 코딩 실습으로 넘어갑니다.

---

## 4.3 넘파이 기초 (배열과 차원) 목차

* [01. 넘파이 개요](../03_numpy_basics/01_numpy_intro/)
* [02. 다차원 배열 (ndarray)](../03_numpy_basics/02_ndarray/)
* [03. 넘파이의 다양한 기본 자료형 (dtype)](../03_numpy_basics/03_dtype/)
* [04. 배열의 차원수 감지기 (.ndim)](../03_numpy_basics/04_ndim/)
* [05. 이미지 배열의 크기 확인 (.size, .nbytes)](../03_numpy_basics/05_size_nbytes/)
