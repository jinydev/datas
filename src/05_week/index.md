---
layout: default
title: "5주차: Numpy 연산과 논리 (Operations & Logic)"
---

# 5주차: Numpy 연산과 논리 (Operations & Logic)

## 학습 목표 (Learning Objectives)
1.  **배열 연산 (Operations)**: 반복문 없는 초고속 사칙연산.
2.  **브로드캐스팅 (Broadcasting)**: 크기가 다른 배열끼리의 똑똑한 연산.
3.  **집계 함수 (Aggregation)**: 데이터 전체를 요약하는 통계 기술.
4.  **불리언 인덱싱 (Boolean Indexing)**: 조건(`True/False`)에 맞는 데이터 필터링.
5.  **팬시 인덱싱 (Fancy Indexing)**: 원하는 순서대로 데이터를 추출하는 고급 기술.

## 강의 내용 (Course Content)

### [01. 배열끼리의 연산 (Element-wise)](./01_numpy_operation.html)
- 사칙연산(`+`, `-`, `*`, `/`).
- 반복문보다 빠른 이유 (벡터화).

### [02. 브로드캐스팅 (Broadcasting)](./02_numpy_broadcasting.html)
- 형상이 다른 배열 간의 연산 규칙.
- 자동 확장(Stretch) 원리.

### [03. 데이터 요약하기 (Aggregation)](./03_numpy_aggregation.html)
- `sum`, `mean`, `max`, `min`.
- 축(Axis) 기준 집계.

### [04. 조건으로 검색하기 (Boolean Indexing)](./04_numpy_boolean.html)
- 조건문(`arr > 50`)을 마스크로 활용하기.
- 필터링(Filtering)의 핵심 원리.

### [05. 원하는 것만 쏙쏙 (Fancy Indexing)](./05_numpy_fancy.html)
- 인덱스 리스트를 활용한 비연속적 선택.
- 데이터 재정렬(Reordering).

---

## 5.6. 정리 (Summary)

이번 주차에는 **데이터의 '내용'을 계산하고 논리적으로 걸러내는 기술**을 배웠습니다.

1.  **계산하기**: `Operation`과 `Broadcasting`으로 수치 데이터를 빠르게 처리하고, `Aggregation`으로 요약했습니다.
2.  **골라내기**: `Boolean Indexing`으로 조건에 맞는 데이터를 찾고, `Fancy Indexing`으로 복잡한 순서의 데이터를 추출했습니다.

다음 주차(**Week 6**)에는 데이터 분석을 돕는 **고급 도구(모듈, 예외 처리, 난수)**들을 배워 Numpy 과정을 마무리합니다. 🛠️
