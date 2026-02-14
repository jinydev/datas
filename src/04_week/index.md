---
layout: home
title: "4주차: Numpy 배열 형태 다루기 (Shape Manipulation)"
---

# 4주차: Numpy 배열 형태 다루기 (Shape Manipulation)

## 학습 목표 (Learning Objectives)
1.  **파이썬 함수 (Functions)**: 코드의 재사용성을 높이는 블록 조립법.
2.  **형태 변환 (Reshape)**: 1차원과 2차원을 자유자재로 오가는 변신 기술.
3.  **배열 합치기 (Concatenation)**: 여러 데이터를 하나로 묶는 조립 기술.
4.  **배열 나누기 (Splitting)**: 데이터를 훈련용/테스트용으로 나누는 분해 기술.
5.  **슬라이싱 (Slicing)**: 원하는 부분만 잘라내는 정교한 칼질.
6.  **인덱싱 (Indexing)**: 특정 위치의 데이터를 콕 집어내는 좌표 읽기.

## 강의 내용 (Course Content)

### [01. 파이썬 함수 (Python Functions)](./01_python_functions.html)
- 함수 정의와 호출.
- 입력(Parameter)과 출력(Return).

### [02. 모양 바꾸기 (Reshape & Flatten)](./02_numpy_reshape.html)
- `reshape()`: 행렬 모양 변경.
- `flatten()`: 1차원으로 펴기.

### [03. 배열 합치기 (Concatenation)](./03_numpy_concatenation.html)
- `concatenate()`: 만능 결합.
- `vstack`, `hstack`: 수직/수평 결합.

### [04. 배열 나누기 (Splitting)](./04_numpy_splitting.html)
- `split()`: 등분하기.
- `vsplit`, `hsplit`: 행/열 자르기.

### [05. 데이터 자르기 (Slicing)](./05_numpy_slicing.html)
- 범위 지정(`:`)을 통한 데이터 추출.
- 다차원 배열 슬라이싱.

### [06. 데이터 콕 집기 (Indexing)](./06_numpy_indexing.html)
- 좌표(`[row, col]`)로 접근하기.
- 마이너스 인덱싱.

---

## 4.7. 정리 (Summary)

이번 주차에는 **Numpy 배열의 '물리적인 형태'를 다루는 모든 기술**을 마스터했습니다.

1.  **모양 바꾸기**: `reshape`로 차원을 넘나들고,
2.  **합치고 나누기**: `concat`, `split`으로 데이터를 조립/분해하며,
3.  **잘라내고 집어내기**: `slice`, `index`로 원하는 데이터를 정확히 포착했습니다.

다음 주차(**Week 5**)에는 이렇게 준비된 데이터를 가지고 논리적인 계산과 필터링을 수행하는 **'데이터의 내용'을 다루는 법**을 배웁니다. 🧠
