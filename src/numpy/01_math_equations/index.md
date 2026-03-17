```
---
layout: numpy
title: "4.1 산술에서 대수학으로 (방정식)"
---

![산술에서 대수학으로 - 방정식의 세계](img/equations_intro.png)

<div style="text-align: center; margin: 30px 0;">
  <!-- SVG 양팔저울 애니메이션 -->
  <svg width="400" height="250" viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- 저울 받침대 그라데이션 -->
      <linearGradient id="baseGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#4a5568"/>
        <stop offset="50%" stop-color="#718096"/>
        <stop offset="100%" stop-color="#4a5568"/>
      </linearGradient>
      <!-- 보석 X 그라데이션 -->
      <radialGradient id="gemGrad" cx="30%" cy="30%" r="70%">
        <stop offset="0%" stop-color="#ebf8ff"/>
        <stop offset="50%" stop-color="#4299e1"/>
        <stop offset="100%" stop-color="#2b6cb0"/>
      </radialGradient>
      <!-- 드롭 섀도우 펄스 애니메이션 -->
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="4" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>

    <!-- 배경 그리드 (수학적 느낌) -->
    <g stroke="#e2e8f0" stroke-width="1" opacity="0.5">
      <path d="M0,50 L400,50 M0,100 L400,100 M0,150 L400,150 M0,200 L400,200" />
      <path d="M50,0 L50,250 M100,0 L100,250 M150,0 L150,250 M200,0 L200,250 M250,0 L250,250 M300,0 L300,250 M350,0 L350,250" />
    </g>

    <g transform="translate(200, 180)"> <!-- 중앙 기준점 (받침대 꼭대기) -->
      
      <!-- 중심 받침대 기둥 -->
      <path d="M-15,0 L15,0 L25,60 L-25,60 Z" fill="url(#baseGrad)"/>
      <circle cx="0" cy="0" r="8" fill="#2d3748"/>
      <circle cx="0" cy="0" r="4" fill="#cbd5e0"/>

      <!-- 저울 팔 (애니메이션 그룹) -->
      <g>
        <animateTransform 
          attributeName="transform" 
          type="rotate" 
          values="-15; 0; -15" 
          dur="4s" 
          repeatCount="indefinite" 
          calcMode="easeInOut"
        />
        
        <!-- 가로 바 -->
        <rect x="-140" y="-4" width="280" height="8" rx="4" fill="#a0aec0" stroke="#4a5568" stroke-width="2"/>
        
        <!-- 왼쪽 접시 (X의 자리) -->
        <g transform="translate(-130, 0)">
          <animateTransform 
            attributeName="transform" 
            type="rotate" 
            values="15; 0; 15" 
            dur="4s" 
            repeatCount="indefinite" 
            calcMode="easeInOut"
            additive="sum"
          />
          <line x1="0" y1="0" x2="-20" y2="40" stroke="#718096" stroke-width="2"/>
          <line x1="0" y1="0" x2="20" y2="40" stroke="#718096" stroke-width="2"/>
          <path d="M-30,40 Q0,55 30,40 L35,45 Q0,65 -35,45 Z" fill="#e2e8f0" stroke="#a0aec0"/>
          
          <!-- 미지의 보석 X -->
          <g transform="translate(0, 30)" filter="url(#glow)">
            <polygon points="0,-15 12,0 0,15 -12,0" fill="url(#gemGrad)"/>
            <text x="0" y="5" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="white" text-anchor="middle">X</text>
            <animate attributeName="opacity" values="0.7; 1; 0.7" dur="2s" repeatCount="indefinite"/>
          </g>
        </g>

        <!-- 오른쪽 접시 (숫자의 자리) -->
        <g transform="translate(130, 0)">
          <animateTransform 
            attributeName="transform" 
            type="rotate" 
            values="15; 0; 15" 
            dur="4s" 
            repeatCount="indefinite" 
            calcMode="easeInOut"
            additive="sum"
          />
          <line x1="0" y1="0" x2="-20" y2="40" stroke="#718096" stroke-width="2"/>
          <line x1="0" y1="0" x2="20" y2="40" stroke="#718096" stroke-width="2"/>
          <path d="M-30,40 Q0,55 30,40 L35,45 Q0,65 -35,45 Z" fill="#e2e8f0" stroke="#a0aec0"/>
          
          <!-- 무거운 숫자 추 -->
          <g transform="translate(0, 32)">
            <rect x="-15" y="-15" width="30" height="20" fill="#f6ad55" stroke="#dd6b20" stroke-width="2" rx="2"/>
            <path d="M-5,-15 C-5,-25 5,-25 5,-15" fill="none" stroke="#dd6b20" stroke-width="2"/>
            <text x="0" y="-1" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#7b341e" text-anchor="middle">10</text>
          </g>
        </g>
      </g>
    </g>

    <!-- 중앙 수식 텍스트 -->
    <text x="200" y="30" font-family="Georgia, serif" font-size="24" font-weight="bold" font-style="italic" fill="#2d3748" text-anchor="middle">
      2x + 4 = 24
    </text>
  </svg>
  <p style="color: #718096; font-size: 0.9em; margin-top: -10px;"><em>[그림] 평형을 이루기 위한 x의 비밀 찾기</em></p>
</div>

# 1. 산술에서 대수학으로: 방정식의 진화와 한계

초등학교 때까지 우리는 $$2 + 3 = ?$$ 처럼 정해진 숫자를 계산하는 '산술(Arithmetic)'의 세계에 살았습니다. 그런데 중학교에 올라오면서 갑자기 정체를 알 수 없는 알파벳 **$$x$$**(엑스)가 등장하며 수학이 어려워지기 시작합니다. 이처럼 미지의 문자(변수)를 사용해 숫자들의 규칙과 논리를 다루는 학문을 **'대수학(Algebra)'**이라고 합니다.

## 이 단원의 핵심 (Chapter Focus)
넘파이(Numpy)의 거대한 텐서 연산을 완전히 정복하기 위해서는, 그 근본이 되는 **방정식과 대수학(Algebra)의 탄생 기원**을 알아야 합니다. 
이번 단원에서는 수치 계산의 한계를 극복하기 위해 미지수 기호 '$$x$$'가 어떻게 도입되었는지부터 출발하여, 양팔 저울로 균형을 맞추는 일차방정식, 그래프에서 교차점을 찾는 연립방정식, 그리고 하늘을 수놓는 포물선 궤도(이차방정식)에 이르기까지 방정식의 위대한 여정을 학습합니다.
마지막으로, 방정식의 변수가 수십만 개로 폭발하는 인공지능 시대의 한계 상황을 조명하며 자연스럽게 차세대 도구인 **'행렬(Matrix)'**로 연결되는 브릿지 과정까지 함께 경험합니다.

## 목차 (Table of Contents)

* [00. 산술에서 대수학으로: 미지의 문자 x](./00_what_is_equation/)
  - 숫자 중심의 산술에서 기호를 사용하는 대수학으로의 전환과 코딩 '변수'의 기원을 알아봅니다.
* [01. 등식의 성질과 양팔 저울 (일차방정식)](./01_linear_equations_balance/)
  - 일차방정식을 기계적 공식이 아닌 수평을 유지하는 황금 양팔 저울의 원리로 직관적으로 풀어냅니다.
* [02. 교차점 스캐너 (연립방정식)](./02_system_of_equations/)
  - 변수가 늘어날 때 필요한 연립방정식의 원리와 그것이 2D 기하학의 두 직선이 충돌하는 하나의 유일한 교차점과 완벽히 동치임을 시각적으로 뚫어냅니다.
* [03. 거대한 무기, 포물선 곡선 (이차방정식)](./03_quadratic_parabola/)
  - 차수가 $$x^2$$로 상승하며 우주를 관통하는 포물선의 궤적이 만들어지는 이유와, 바닥 충돌점(해)을 수학적으로 스캔하는 의미를 탐구합니다.
* [04. 방정식이 폭발할 때, 행렬이 강림하다](./04_equation_to_matrix/)
  - 변수가 기하급수적으로 늘어나는 딥러닝 시대에서 방정식 체계가 무너지고, 그 돌파구로서 껍데기 기호들을 벗어난 타일 덩어리 '행렬(Matrix)'이 필연적으로 탄생하게 됨을 다룹니다.
