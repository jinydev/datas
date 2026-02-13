---
layout: default
title: "8주차: 판다스 기초 (Pandas Basics)"
---

# 8주차: 판다스 기초 (Pandas Basics)

> **학습목표**:
> *   파이썬 데이터 분석의 핵심 라이브러리인 **판다스(Pandas)**의 개념과 역할을 이해합니다.
> *   기본 데이터 구조인 **시리즈(Series)**와 **데이터프레임(DataFrame)**을 생성하고 조작하는 방법을 익힙니다.
> *   데이터의 생김새를 파악하고 기초적인 정보를 확인하는 기술을 습득합니다.

## 8.1. 판다스 소개 (Introduction)
*   **[01. 판다스란 무엇인가?](01_pandas_intro.html)**
    *   파이썬의 엑셀, 판다스 소개
    *   데이터베이스(RDBMS)와의 차이점 (Memory vs Disk)
    *   설치 및 불러오기

## 8.2. 데이터 구조 (Data Structures)
*   **[02. 시리즈 (Series)](02_pandas_series.html)**
    *   1차원 데이터의 이해 (Index + Value)
    *   리스트, 딕셔너리로 시리즈 만들기
    *   라벨 인덱싱과 위치 인덱싱

*   **[03. 데이터프레임 (DataFrame)](03_pandas_dataframe.html)**
    *   2차원 표 데이터의 이해 (Row + Column)
    *   딕셔너리로 데이터프레임 만들기
    *   데이터 뜯어보기 3총사: `head()`, `info()`, `describe()`

## 8.3. 심화 과정 (Advanced Process)
*   **[04. 시리즈 심화 (Advanced Series)](04_series_advanced.html)**
    *   데이터 파악: `value_counts()`, `unique()`
    *   함수 적용: `map()`, `apply()`
    *   시각화: 빈도수 막대 그래프 (Bar Plot)

*   **[05. 데이터프레임 심화 (Advanced DataFrame)](05_dataframe_advanced.html)**
    *   정렬과 수정: `sort_values()`, `drop()`, `rename()`
    *   상관관계 분석: `corr()`
    *   시각화: 산점도 (Scatter Plot)

## 8.4. 파이썬 기본기 (Python Basics)
*   **[06. 파이썬 파일 입출력](06_python_file_io.html)**
    *   파일 열고 닫기: `open`, `close`, `with`
    *   파일 읽고 쓰기: `read`, `write`, `readline`

<br>

---

<br>

## 정리 (Summary)

이번 주차에서는 데이터 분석의 가장 강력한 도구인 판다스의 기초를 다졌습니다.
또한 파이썬의 기본 파일 입출력 기능도 함께 익혀, 데이터 핸들링의 기초 체력을 길렀습니다.
이제 우리는 데이터를 엑셀처럼 자유자재로 다룰 준비가 되었습니다.
다음 주에는 판다스를 이용해 데이터를 자르고, 붙이고, 변형하는 **데이터 조작(Manipulation)** 기술을 본격적으로 배워보겠습니다.
