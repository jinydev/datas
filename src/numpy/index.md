---
layout: numpy
title: 넘파이 (Numpy) 기초
permalink: /numpy/
---

# 넘파이 (Numpy) 핵심 가이드

이 섹션에서는 데이터 과학과 수치 계산의 핵심 패키지인 **Numpy(넘파이)**에 대해 다룹니다.
행렬의 수학적 원리부터 다차원 배열(ndarray) 객체의 생성, 슬라이싱, 형태 변경, 브로드캐스팅, 그리고 다양한 수학 연산 및 배열 결합/분할 함수까지 깊이 있는 내용을 7개의 논리적 섹션으로 그룹화하여 학습합니다.

---

## 01. 넘파이 기초와 벡터/행렬의 이해
- [01. 과학용 컴퓨팅 패키지 numpy 개요](/numpy/01_numpy_basics/01_numpy_intro/)  
  넘파이(numpy)는 파이썬에서 고성능 다차원 배열 및 행렬 연산을 지원하는 핵심 라이브러리입니다. 행렬의 수학적 의미, 점과 방향을 아우르는 벡터의 기하학적 원리, 그리고 실생활에서의 행렬 활용 비유를 통해 선형대수학적 배경지식을 익힙니다.
- [02. 다차원 배열 자료형 ndarray](/numpy/01_numpy_basics/02_ndarray/)  
  numpy의 대표적인 자료형인 ndarray의 구조와 `shape`, `ndim`, `dtype` 등의 주요 속성을 다룹니다. 또한 리스트와의 차이점 및 고차원 텐서(Tensor)의 기초를 학습합니다.

## 02. 다차원 배열 생성과 초기화
- [03. 내장함수 array()로 ndarray 생성](/numpy/02_array_creation/03_array_creation/)  
  기본 파이썬의 리스트나 튜플을 인자로 받아 ndarray 객체로 변환하는 기본적인 배열 생성 방법을 학습합니다.
- [04. numpy의 내장함수 arange() 개요](/numpy/02_array_creation/04_arange/)  
  정수뿐만 아니라 실수 간격의 범위 값 생성도 가능한 빠르고 강력한 `arange()` 함수에 대해 알아봅니다.
- [05. 배열의 모양을 바꾸는 reshape()](/numpy/02_array_creation/05_reshape/)  
  배열의 원소 개수는 그대로 둔 채 행과 열 구조를 변경하는 방법 및 `reshape(-1, ..)` 등 형태 추론의 원리를 배웁니다.
- [06. 일정 간격의 값으로 배열 생성 linspace()](/numpy/02_array_creation/06_linspace/)  
  구간 양끝을 포함하면서, 지정된 개수(num)만큼 균등하게 분할된 데이터를 얻기 위해 빈번히 쓰이는 `linspace()`를 학습합니다.
- [07. 내장함수 arange()와 linspace() 비교](/numpy/02_array_creation/07_arange_vs_linspace/)  
  `stop` 조건을 미포함하며 `step`을 지정하는 `arange`와, `stop`을 기본 포함하며 요소의 수(`num`)를 지정하는 `linspace`를 대조해 봅니다.
- [08 ~ 13. zeros(), ones(), eye(), full(), empty() 등 특수 배열 생성](/numpy/02_array_creation/08_zeros/)
  특정 초깃값을 바탕으로 안전하고 신속하게 크기만 지정된 다차원 데이터 포맷을 찍어내는 `zeros`, `ones`, 대각 단위행렬 `eye`, 임의 스칼라 할당 `full`, 쓰레기값 생성기 `empty`, 기존 형태 모방 `_like` 시리즈의 용법을 아우릅니다.  
  *(자세한 단원 목차는 사이드바의 하위 메뉴를 클릭해 확인하세요)*

## 03. 배열 연산과 브로드캐스팅(Broadcasting)
Numpy 배열간의 사칙연산과 마법 같은 확대 기능인 브로드캐스팅, 그리고 다양한 통계 요약 정보를 한 방에 처리하는 범용 함수를 배웁니다.
- [14. 배열과 스칼라와의 연산](/numpy/03_array_operations/14_scalar_operations/)  
- [15. 배열과 배열의 연산](/numpy/03_array_operations/15_array_operations/)  
- [16. 배열 함수와 범용 함수 (ufunc)](/numpy/03_array_operations/16_ufunc/)  
  `sum`, `mean`, `max`, `argmax`, `astype`, `sort`, 논리 필터 함수 등 필수적인 넘파이 내장 메서드 19선의 원리와 결측치(nan, None) 처리 전략을 심도 있게 포괄합니다.
- [22. 브로드캐스팅 개요](/numpy/03_array_operations/22_broadcasting_intro/)  
- [23. 스칼라 또는 단일 값과 배열의 연산](/numpy/03_array_operations/23_scalar_broadcasting/)  
- [24. 2차원 배열의 브로드캐스팅](/numpy/03_array_operations/24_2d_broadcasting/)  
- [25. 상수 np.newaxis 활용해 두 배열의 브로드캐스팅](/numpy/03_array_operations/25_newaxis/)  

## 04. 인덱싱과 슬라이싱 기법
원하는 데이터만을 가장 빠르고 세련되게 추출하는 다양한 데이터 슬라이싱 방법을 배웁니다. 조건 검색과 고급 색인이 포함됩니다.
- [17 ~ 19. 다차원 배열의 첨자와 슬라이싱 (`1차원` / `2차원` / `3차원`)](/numpy/04_indexing_slicing/17_1d_slicing/)  
- [26 ~ 27. 배열 고급 색인 기술 (`1차원` / `2차원`)](/numpy/04_indexing_slicing/26_1d_indexing/)
- [28. 다양한 슬라이싱과 배열 색인 (`np.where` 등)](/numpy/04_indexing_slicing/28_advanced_indexing/)

## 05. 배열 형태 변환과 메모리 시점
배열의 생김새를 뒤집거나, 원본 배치를 전혀 변형하지 않은 채 새로운 `View`만을 생성하여 다차원을 훑는 메모리 지식을 배웁니다.
- [20. 배열 형태 수정 (`transpose()`와 차원 축소)](/numpy/05_shape_memory/20_reshape_advanced/)  
- [21. 데이터 복사본(copy)과 보기(뷰, view) 참조 구조](/numpy/05_shape_memory/21_copy_view/)

## 06. 배열 결합과 분할
작은 모듈 단위의 데이터 군락들을 가로/세로로 덧붙여 강력한 통합 데이터셋을 구축하거나, 특정 축(axis) 단위로 부수는 방법입니다.
- [29 ~ 37. 배열 결합 개요 및 각종 Stack/Concat 계열 연산](/numpy/06_concat_split/29_array_concat_intro/)
- [38 ~ 39. 1차원 배열/벡터의 다양한 결합 방법 종합 리뷰](/numpy/06_concat_split/38_1d_concat_methods/)
- [40 ~ 42. 유용한 분할 계열 함수들 (`split`, `vsplit/hsplit`, `array_split`)](/numpy/06_concat_split/40_split/)

## 07. 난수 생성 및 연습문제
데이터 과학에서 시뮬레이션 및 데이터 테스트용으로 필수로 사용되는 임의 규칙 샘플링 기법입니다.
- [43. 난수 생성 모듈 (`np.random`)](/numpy/07_random_exercises/43_random/)
- [44. 넘파이 종합 실전 연습문제](/numpy/07_random_exercises/44_exercises/)
