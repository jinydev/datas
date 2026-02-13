---
layout: default
title: "9주차: 데이터프레임 조작 (Data Manipulation)"
---

# 9주차: 데이터프레임 조작 (Data Manipulation)

> **학습목표**:
> *   외부 파일(CSV, Excel)을 불러오고 저장하는 입출력(I/O) 과정을 마스터합니다.
> *   데이터의 정보를 확인하고 통계량을 계산하여 데이터의 특성을 파악합니다.
> *   복잡한 조건으로 데이터를 필터링하고(Query), 원하는 형태로 가공(Modification)하는 능력을 기릅니다.

## 9.1. 입출력 (Input/Output)
*   **[01. 데이터 불러오기/저장하기](01_pandas_io.html)** (구: 이론)
    *   `read_csv`, `read_excel`: 파일 읽기
    *   `to_csv`: 파일 저장하기

## 9.2. 정보 확인 및 통계 (Info & Statistics)
*   **[02. 데이터 확인 및 통계](02_pandas_info_stats.html)**
    *   구조 파악: `info()`, `dtypes`
    *   기초 통계: `sum`, `mean`, `max`, `min`
    *   축(Axis)의 이해

## 9.3. 검색과 필터링 (Query)
*   **[03. 데이터 검색과 필터링](03_pandas_query.html)**
    *   불리언 인덱싱 (Boolean Indexing)
    *   SQL처럼 쓰는 `query()` 함수
    *   포함 여부 확인: `isin()`

## 9.4. 수정과 정렬 (Modification)
*   **[04. 데이터 수정 및 정렬](04_pandas_modification.html)**
    *   열 추가 및 수정 (`assign`)
    *   데이터 삭제 (`drop`)
    *   값 정렬 (`sort_values`) 및 인덱스 정렬 (`sort_index`)

<br>

---

<br>

## 정리 (Summary)

이번 주에는 판다스를 이용해 데이터를 자유자재로 주무르는 방법을 배웠습니다.
데이터를 불러오고(I/O), 훑어보고(Info), 필요한 것만 뽑고(Query), 고치는(Mod) 과정은 데이터 분석가의 일상입니다.
다음 주에는 이렇게 잘 차려진 데이터를 가지고 본격적인 **전처리(Preprocessing)**와 **시각화(Visualization)**를 진행해 보겠습니다.
