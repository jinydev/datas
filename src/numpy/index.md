---
layout: numpy
title: 넘파이 (Numpy) 기초
permalink: /numpy/
---

# 넘파이 (Numpy) 핵심 가이드

이 섹션에서는 데이터 과학과 수치 계산의 핵심 패키지인 **Numpy(넘파이)**에 대해 다룹니다.
데이터 구조를 극적으로 단순화시키는 '방정식과 행렬'의 수학적 원리부터 시작하여, 다차원 배열(ndarray) 객체의 생성, 슬라이싱, 형태 변경, 브로드캐스팅, 그리고 다양한 수학 연산 및 배열 결합/분할 함수까지 깊이 있는 내용을 9개의 논리적 섹션으로 그룹화하여 학습합니다.

---

## 01. [사전학습 1] 산술에서 대수학으로 (방정식)
AI 딥러닝과 코딩을 관통하는 거대한 텐서 연산은 사실 구시대의 낡은 "방정식 $$x, y, z$$"의 한계에서 비롯되었습니다. 방정식을 통해 변수가 탄생하고, 기하 공간에서 해를 탐색하는 대수학의 본질적 기원을 배웁니다.
- [00. 산술에서 대수학으로: 미지의 문자 x](/numpy/01_math_equations/00_what_is_equation/)
- [01. 등식의 성질과 양팔 저울 (일차방정식)](/numpy/01_math_equations/01_linear_equations_balance/)
- [02. 교차점 스캐너 (연립방정식)](/numpy/01_math_equations/02_system_of_equations/)
- [03. 거대한 무기, 포물선 곡선 (이차방정식)](/numpy/01_math_equations/03_quadratic_parabola/)
- [04. 방정식이 폭발할 때, 행렬이 강림하다](/numpy/01_math_equations/04_equation_to_matrix/)

## 02. [사전학습 2] 데이터 블록과 시공간 왜곡 (행렬)
수만 개의 방정식 껍데기를 버리고, 오직 엑기스 숫자(계수)만 추출하여 아파트에 늘어놓는 마법의 타일 덩어리, '행렬'의 탄생을 리뷰합니다. 
- [00. 왜 갑자기 행렬인가? (방정식의 한계)](/numpy/02_math_matrices/00_intro_equations_limit/)
- [01. 데이터베이스 격자 타일링: 행렬의 구조](/numpy/02_math_matrices/01_what_is_matrix/)
- [02 ~ 04. 행렬의 덧셈, 실수배, 그리고 내적 곱셈의 미스터리](/numpy/02_math_matrices/04_matrix_multiplication/)
- [05. 시공간을 비틀어라! 선형 변환 마법진](/numpy/02_math_matrices/05_linear_transformation/)
- [06. 마지막 승부: GPU 텐서 폭격과 파이썬 Numpy 로의 접속](/numpy/02_math_matrices/06_intro_to_numpy_ai/)

## 03. 넘파이 기초와 벡터/행렬의 이해
- [01. 과학용 컴퓨팅 패키지 numpy 개요](/numpy/03_numpy_basics/01_numpy_intro/)  
  본격적으로 넘파이(numpy) 파이썬 모듈 사용을 시작합니다. 위에서 배운 행렬을 어떻게 파이썬으로 찍어내는지 학습합니다.
- [02. 다차원 배열 자료형 ndarray](/numpy/03_numpy_basics/02_ndarray/)  
  numpy의 대표적인 자료형인 ndarray의 구조와 `shape`, `ndim`, `dtype` 등의 주요 속성을 다룹니다.

## 04. 다차원 배열 생성과 초기화
- [03. 내장함수 array()로 ndarray 생성](/numpy/04_array_creation/01_array_creation/)  
  기본 파이썬 리스트를 인자로 받아 행렬 객체로 변환합니다.
- [04. numpy의 내장함수 arange() 개요](/numpy/04_array_creation/02_arange/)  
- [05. 배열의 모양을 바꾸는 reshape()](/numpy/04_array_creation/03_reshape/)  
- [06. 일정 간격 분할 배열 생성 linspace()](/numpy/04_array_creation/04_linspace/)
- [07 ~ 13. zeros(), ones(), eye(), full(), empty() 등 특수 배열 생성](/numpy/04_array_creation/06_zeros/)
  특정 초깃값을 바탕으로 안전하고 신속하게 크기만 지정된 다차원 데이터 포맷을 찍어내는 `zeros`, `ones`, 대각 행렬 `eye`, 임의 할당 `full` 등의 용법을 아우릅니다.  

## 05. 배열 연산과 브로드캐스팅(Broadcasting)
Numpy 배열간의 사칙연산과 마법 같은 확대 기능인 브로드캐스팅, 그리고 다양한 통계 요약 정보를 한 방에 처리하는 범용 함수를 배웁니다.
- [14 ~ 15. 배열과 스칼라, 배열과 배열의 연산](/numpy/05_array_operations/01_scalar_operations/)  
- [16. 배열 함수와 범용 함수 (ufunc)](/numpy/05_array_operations/03_ufunc/)  
  `sum`, `mean`, `max`, `argmax`, `astype`, `sort`, 논리 필터 함수 등 필수적인 넘파이 내장 메서드 19선의 원리를 포괄합니다.
- [22 ~ 25. 브로드캐스팅 코어 및 np.newaxis 축 활용](/numpy/05_array_operations/04_broadcasting_intro/)  

## 06. 인덱싱과 슬라이싱 기법
원하는 데이터만을 가장 빠르고 세련되게 추출하는 방법입니다. 조건 검색과 고급 색인이 포함됩니다.
- [17 ~ 19. 다차원 배열 첨자 및 슬라이싱](/numpy/06_indexing_slicing/01_d_slicing/)  
- [26 ~ 28. 배열 고급 색인 기술 및 np.where](/numpy/06_indexing_slicing/06_advanced_indexing/)

## 07. 배열 형태 변환과 메모리 시점
배열의 생김새를 뒤집거나, 원본 배치를 전혀 변형하지 않은 채 새로운 `View`만을 생성하여 다차원을 훑는 메모리 지식을 배웁니다.
- [20. 배열 형태 수정 (`transpose()`와 차원 축소)](/numpy/07_shape_memory/01_reshape_advanced/)  
- [21. 데이터 복사본(copy)과 보기(뷰, view) 참조 구조](/numpy/07_shape_memory/02_copy_view/)

## 08. 배열 결합과 분할
작은 모듈 단위의 데이터 군락들을 가로/세로로 덧붙여 강력한 통합 데이터셋을 구축하거나, 모듈 단위로 부수는 방법입니다.
- [29 ~ 39. 다양한 배열 결합 개요 (Stack, Concat 등)](/numpy/08_concat_split/01_array_concat_intro/)
- [40 ~ 42. 유용한 분할 계열 함수 (`split`, `vsplit`, `hsplit`)](/numpy/08_concat_split/12_split/)

## 09. 난수 생성 및 연습문제
데이터 과학에서 확률, 시뮬레이션용 데이터셋 생성을 위한 필살기입니다.
- [43. 난수 생성 모듈 (`np.random`)](/numpy/09_random_exercises/01_random/)
- [44. 넘파이 종합 실전 연습문제](/numpy/09_random_exercises/02_exercises/)
