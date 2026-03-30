---
layout: numpy
title: "넘파이 (Numpy) 기초"
permalink: /numpy/
---

# 넘파이 (Numpy) 핵심 가이드

이 섹션에서는 데이터 과학과 수치 계산의 핵심 패키지인 **Numpy(넘파이)**에 대해 다룹니다.
데이터 구조를 극적으로 단순화시키는 '방정식과 행렬'의 수학적 원리부터 시작하여, 다차원 배열(ndarray) 객체의 생성, 슬라이싱, 형태 변경, 브로드캐스팅, 그리고 다양한 수학 연산 및 배열 결합/분할 함수까지 깊이 있는 내용을 9개의 논리적 섹션으로 그룹화하여 학습합니다.

## 학습목표 {#objectives}
* 대용량 데이터 연산의 기반이 되는 **선형대수(방정식과 행렬)의 기초 원리**를 수학적 직관으로 이해합니다.
* 다차원 배열 데이터 구조인 **`ndarray`의 특징과 메모리 구조**를 파악하고 형태를 자유자재로 다룰 수 있습니다.
* 데이터 분석의 필수 도구인 넘파이의 강력한 **배열 연산, 슬라이싱, 브로드캐스팅(Broadcasting)** 기술을 실무에 적용해 봅니다.

## 과목 핵심 목차 {#core-contents}

### [4.1 산술에서 대수학으로 (방정식)](01_math_equations/)
AI 딥러닝과 코딩을 관통하는 거대한 텐서 연산은 사실 구시대의 낡은 "방정식 $$x, y, z$$"의 세계에서 비롯되었습니다. 방정식을 통해 변수가 탄생하고, 기하 공간에서 해를 탐색하는 대수학의 본질적 기원을 배웁니다.
* [4.1.0 산술에서 대수학으로 (미지의 x 등장)](01_math_equations/00_what_is_equation/)
* [4.1.1 양팔 저울과 등식 (방정식 풀이)](01_math_equations/01_linear_equations_balance/)
* [4.1.2 교차점 스캐너 (연립방정식)](01_math_equations/02_system_of_equations/)
* [4.1.3 거대한 무기, 포물선 곡선 (이차방정식)](01_math_equations/03_quadratic_parabola/)
* [4.1.4 방정식이 폭발할 때, 행렬이 강림하다](01_math_equations/04_equation_to_matrix/)

### [4.2 데이터 블록과 시공간 왜곡 (행렬)](02_math_matrices/)
수만 개의 방정식 껍데기를 버리고, 오직 엑기스 숫자(계수)만 추출하여 2차원 평면에 늘어놓는 마법의 타일 덩어리, '행렬'의 탄생을 알아봅니다.
* [4.2.0 왜 갑자기 행렬인가? (방정식의 한계)](02_math_matrices/00_intro_equations_limit/)
* [4.2.1 행렬의 구조 (행과 열)](02_math_matrices/01_what_is_matrix/)
* [4.2.2 행렬의 덧셈과 뺄셈](02_math_matrices/02_addition_subtraction/)
* [4.2.3 스케일 폭주 (실수배)](02_math_matrices/03_scalar_multiplication/)
* [4.2.4 행과 열의 십자 충돌 (곱셈의 미스터리)](02_math_matrices/04_matrix_multiplication/)
* [4.2.5 선형 변환 마법진 (벡터의 왜곡)](02_math_matrices/05_linear_transformation/)
* [4.2.6 GPU 텐서 폭격과 파이썬 Numpy](02_math_matrices/06_intro_to_numpy_ai/)

### [4.3 넘파이 기초와 벡터/행렬의 이해](03_numpy_basics/)
본격적으로 파이썬 과학용 컴퓨팅 패키지 numpy를 개괄하고 다차원 배열의 대표적 자료형인 `ndarray`의 구조와 `shape`, `ndim`, `dtype` 등의 주요 속성을 다룹니다.
* [4.3.1 과학용 컴퓨팅 패키지 numpy 개요](03_numpy_basics/01_numpy_intro/)
* [4.3.2 다차원 배열 자료형 ndarray](03_numpy_basics/02_ndarray/)
* [4.3.3 넘파이의 다양한 기본 자료형 (dtype)](03_numpy_basics/03_dtype/)
* [4.3.4 배열의 차원수 감지기 (.ndim)](03_numpy_basics/04_ndim/)
* [4.3.5 이미지 배열의 크기 확인 (.size, .nbytes)](03_numpy_basics/05_size_nbytes/)

### [4.4 다차원 배열 생성과 초기화](04_array_creation/)
특정한 초깃값을 바탕으로 안전하고 신속하게 크기만 지정된 다차원 데이터 포맷을 찍어내는 `arange`, `zeros`, `ones`, `reshape` 등 다양한 배열 생성 내장 함수를 익힙니다.
* [4.4.1 내장함수 array()로 ndarray 생성](04_array_creation/01_array_creation/)
* [4.4.2 numpy의 내장함수 arange() 개요](04_array_creation/02_arange/)
* [4.4.3 배열의 모양을 바꾸는 reshape()](04_array_creation/03_reshape/)
* [4.4.4 일정한 간격의 값으로 배열을 만드는 linspace()](04_array_creation/04_linspace/)
* [4.4.5 내장함수 arange()와 linspace() 비교](04_array_creation/05_arange_vs_linspace/)
* [4.4.6 원소가 모두 0인 배열을 생성하는 zeros()](04_array_creation/06_zeros/)
* [4.4.7 원소가 모두 1인 배열을 생성하는 ones()](04_array_creation/07_ones/)
* [4.4.8 대각선 원소가 모두 1인 2차원 배열을 만드는 eye()](04_array_creation/08_eye/)
* [4.4.9 원소가 모두 특정 값인 배열을 만드는 full()](04_array_creation/09_full/)
* [4.4.10 초기화되지 않은 배열을 생성하는 empty()](04_array_creation/10_empty/)
* [4.4.11 내장함수 zeros_like()와 ones_like(), full_like()](04_array_creation/11_like_functions/)

### [4.5 배열 연산과 브로드캐스팅(Broadcasting)](05_array_operations/)
Numpy 배열간의 사칙연산과 마법 같은 차원 확대 기능인 브로드캐스팅, 그리고 다양한 통계 요약 정보를 한 방에 처리하는 범용 함수(ufunc)를 배웁니다.
* [4.5.1 배열과 스칼라와의 연산](05_array_operations/01_scalar_operations/)
* [4.5.2 배열과 배열의 연산](05_array_operations/02_array_operations/)
* [4.5.3 배열 함수와 범용 함수](05_array_operations/03_ufunc/)
* [4.5.4 브로드캐스팅 개요](05_array_operations/04_broadcasting_intro/)
* [4.5.5 스칼라 또는 단일 값과 배열의 연산](05_array_operations/05_scalar_broadcasting/)
* [4.5.6 2차원 배열의 브로드캐스팅](05_array_operations/06_d_broadcasting/)
* [4.5.7 상수 np.newaxis 활용해 두 배열의 브로드캐스팅](05_array_operations/07_newaxis/)

### [4.6 인덱싱과 슬라이싱 기법](06_indexing_slicing/)
초대용량 빅데이터에서 원하는 부분만 가장 빠르고 세련되게 추출해내는 조건 검색 및 다차원 배열 고급 색인 기술을 훈련합니다.
* [4.6.1 1차원 배열의 첨자와 슬라이싱](06_indexing_slicing/01_d_slicing/)
* [4.6.2 2차원 배열의 첨자와 슬라이싱](06_indexing_slicing/02_d_slicing/)
* [4.6.3 3차원 배열의 첨자와 슬라이싱](06_indexing_slicing/03_d_slicing/)
* [4.6.4 1차원 배열의 색인](06_indexing_slicing/04_d_indexing/)
* [4.6.5 2차원 배열의 색인](06_indexing_slicing/05_d_indexing/)
* [4.6.6 다양한 슬라이싱과 배열 색인](06_indexing_slicing/06_advanced_indexing/)

### [4.7 배열 형태 변환과 메모리 시점](07_shape_memory/)
배열의 생김새를 뒤집거나, 원본을 보존한 채 참조 복사(View)만으로 새로운 각도에서 다차원 데이터를 바라보는 고급 메모리 관리 지식을 배웁니다.
* [4.7.1 배열 형태 수정](07_shape_memory/01_reshape_advanced/)
* [4.7.2 복사(copy)와 보기(뷰, view)](07_shape_memory/02_copy_view/)

### [4.8 배열 결합과 분할](08_concat_split/)
작은 데이터 블록 조각들을 가로/세로 축을 기준으로 결합해 병합 데이터셋을 조립하거나 쪼개 분할하는 방법을 배웁니다.
* [4.8.1 배열 결합 개요](08_concat_split/01_array_concat_intro/)
* [4.8.2 numpy.vstack()](08_concat_split/02_vstack/)
* [4.8.3 numpy.hstack()](08_concat_split/03_hstack/)
* [4.8.4 배열 결합 연산 column_stack()과 row_stack()](08_concat_split/04_column_row_stack/)
* [4.8.5 배열 결합 연산 concatenate()와 stack()](08_concat_split/05_concatenate_stack/)
* [4.8.6 column_stack()과 hstack()](08_concat_split/06_column_stack_vs_hstack/)
* [4.8.7 row_stack()과 vstack()](08_concat_split/07_row_stack_vs_vstack/)
* [4.8.8 np.c_[](08_concat_split/08_npc_column_stack/)
* [4.8.9 np.r_[](08_concat_split/09_npr/)
* [4.8.10 1차원 배열, 벡터의 다양한 결합 방법](08_concat_split/10_d_concat_methods/)
* [4.8.11 1차원 배열의 다양한 결합 방법 정리](08_concat_split/11_d_concat_summary/)
* [4.8.12 유용한 함수 split()](08_concat_split/12_split/)
* [4.8.13 분할 함수 hsplit()과 vsplit()](08_concat_split/13_hsplit_vsplit/)
* [4.8.14 분할 함수 array_split()](08_concat_split/14_array_split/)

### [4.9 난수 생성 및 연습문제](09_random_exercises/)
데이터 분석 시뮬레이션 및 무작위 샘플링을 위한 난수 발생 모듈(`np.random`) 기법을 익히고 파이썬 프로그래밍 실전 능력을 점검합니다.
* [4.9.1 난수 생성](09_random_exercises/01_random/)
* [4.9.2 넘파이 종합 연습문제](09_random_exercises/02_exercises/)

## 정리 {#summary}
이번 Numpy 과목을 통해 우리는 복잡하고 구불구불한 2차원 표와 다차원 텐서 구조를 넘파이라는 강력한 라이브러리로 압축하여 효율적인 코드로 통제할 수 있게 되었습니다. 벡터화 연산 최적화, 그리고 브로드캐스팅의 힘은 이어지는 데이터프레임 도구 Pandas와 딥러닝 응용 과정에서 든든한 수학적/프로그래머적 무기가 되어줄 것입니다.
