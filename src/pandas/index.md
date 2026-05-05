---
layout: pandas
title: 판다스 (Pandas)
permalink: /pandas/
description: "파이썬 기반의 강력한 데이터 분석 및 조작 라이브러리인 Pandas(판다스)를 학습합니다."
---

# 판다스 (Pandas) 핵심 가이드

파이썬 기반의 강력한 데이터 분석 및 조작 라이브러리인 **Pandas(판다스)**를 학습합니다. 

주요 자료구조인 Series와 DataFrame의 생성부터 데이터 선택, 수정, 연산, 파일 입출력까지 실무에 필요한 데이터 정제 기술을 5개의 논리적인 섹션으로 나누어 살펴봅니다.

![Pandas Concept Illustration](./img/pandas_illustration.png)



## 6.1 판다스 기초 {#section-01}
판다스의 핵심 개념과 설치 방법을 배우고, 기본 자료구조인 Series와 DataFrame의 특징을 이해합니다. 데이터 분석 환경을 구축하고 기본기를 다지는 첫 단계입니다.

- [6.1.1 판다스 소개](/pandas/01_pandas_basics/01_pandas_intro/)
- [6.1.2 판다스 설치 및 기초 실습](/pandas/01_pandas_basics/02_pandas_practice/)
- [6.1.3 Series(시리즈) 개요](/pandas/01_pandas_basics/02_series_intro/)
- [6.1.4 DataFrame(데이터프레임) 개요](/pandas/01_pandas_basics/03_dataframe_intro/)

## 6.2 자료구조 생성 (Series & DataFrame) {#section-02}
리스트, 딕셔너리, 2차원 행렬 등 다양한 형태의 데이터를 활용하여 Series와 DataFrame을 직접 생성합니다. 시계열 데이터를 위한 날짜 데이터 생성 및 자료형 검사 방법도 익힙니다.

- [6.2.1 Series(시리즈) 생성과 데이터 추출](/pandas/02_series_dataframe_creation/01_series_creation/)
- [6.2.2 Series(시리즈) 필수 함수와 통계 요약](/pandas/02_series_dataframe_creation/02_series_functions/)
- [6.2.3 DataFrame 생성자(Constructor) 개요](/pandas/02_series_dataframe_creation/03_dataframe_constructor/)
- [6.2.4 2차원 행렬(Matrix)로 데이터프레임 만들기](/pandas/02_series_dataframe_creation/04_df_from_matrix/)
- [6.2.5 딕셔너리(Dict)를 이용한 데이터프레임 구조화](/pandas/02_series_dataframe_creation/05_df_from_dict/)
- [6.2.6 여러 개의 Series(시리즈)를 조립해 DataFrame 만들기](/pandas/02_series_dataframe_creation/06_df_from_series/)
- [6.2.7 리스트 속 딕셔너리(List of Dicts)로 DataFrame 만들기](/pandas/02_series_dataframe_creation/07_df_from_dict_list/)
- [6.2.8 딕셔너리의 값(Value)으로 Series(시리즈) 사용하기](/pandas/02_series_dataframe_creation/08_df_from_series_dict/)
- [6.2.9 데이터프레임의 자료형 검사와 변경 (dtypes)](/pandas/02_series_dataframe_creation/09_df_dtypes/)
- [6.2.10 시계열 데이터의 꽃: date_range()로 자동 날짜 생성하기](/pandas/02_series_dataframe_creation/10_date_range/)
- [6.2.11 완전체 시계열 데이터프레임 만들기](/pandas/02_series_dataframe_creation/11_df_with_dates/)

## 6.3 데이터 참조 및 인덱싱 {#section-03}
방대한 데이터 중에서 원하는 행과 열을 정확하고 빠르게 추출하는 방법을 학습합니다. 이름 기반의 `loc`, 번호 기반의 `iloc` 및 조건식을 활용한 논리 검색 기법을 다룹니다.

- [6.3.1 DataFrame 열(Column) 추출의 마법](/pandas/03_data_selection/01_column_selection/)
- [6.3.2 데이터프레임 논리식 검색 (Conditional Selection)](/pandas/03_data_selection/02_conditional_selection/)
- [6.3.3 loc[이름] 속성으로 행(Row) 참조 구하기](/pandas/03_data_selection/03_row_selection_loc/)
- [6.3.4 loc[index[i]]를 활용한 우회적 행 참조](/pandas/03_data_selection/04_row_selection_loc_i/)
- [6.3.5 loc[ : , 열이름] 으로 열(Column) 참조하기](/pandas/03_data_selection/05_col_selection_loc/)
- [6.3.6 loc[:, columns[i]]를 활용한 우회적 열 참조](/pandas/03_data_selection/06_col_selection_loc_i/)
- [6.3.7 loc[행, 열] 십자선 동시 참조](/pandas/03_data_selection/07_row_col_selection/)
- [6.3.8 df.iloc[위치] 로 번호 기반 참조](/pandas/03_data_selection/08_iloc_selection/)

## 6.4 데이터프레임 정보 확인 및 수정 {#section-04}
데이터프레임의 통계 정보와 구조를 점검하고, 새로운 열(Column)이나 행(Row)을 추가하며 데이터를 수정합니다. 정렬과 고급 조건 검색을 통한 실무적인 데이터 전처리 과정을 배웁니다.

- [6.4.1 데이터프레임 종합 건강검진](/pandas/04_data_modification/01_df_info_modify/)
- [6.4.2 축(Axis) 기준 데이터 압축 연산](/pandas/04_data_modification/02_df_extract_assign/)
- [6.4.3 파생 열(Column)과 요약 행(Row) 추가하기](/pandas/04_data_modification/03_df_modify_assign/)
- [6.4.4 데이터프레임 고급 조건 검색 (isin, contains)](/pandas/04_data_modification/04_df_conditional_search/)
- [6.4.5 데이터프레임 쌍끌이 정렬](/pandas/04_data_modification/05_df_sorting/)
- [6.4.6 데이터프레임 전처리 공방](/pandas/04_data_modification/06_df_various_modifications/)

## 6.5 데이터 입출력 및 수집 {#section-05}
CSV, Excel 파일 등 외부 데이터를 판다스로 불러오고 처리한 데이터를 다시 파일로 저장하는 방법을 배웁니다. 실제 공공데이터를 예제로 하여 데이터를 정제하고 불러오는 실전을 경험합니다.

- [6.5.1 CSV와 Excel 파일 입출력](/pandas/05_file_io/01_csv_excel_io/)
- [6.5.2 실전! 지저분한 공공데이터 정제하기](/pandas/05_file_io/02_internet_data/)

## 6.6 데이터 셋 (Datasets) {#section-06}
다양한 데이터 분석 기법과 머신러닝 알고리즘 실습에 즉시 활용할 수 있는 Pandas와 Seaborn의 주요 내장 데이터 셋들을 소개합니다.

- [6.6.1 Pandas/Seaborn 기본 제공 데이터 셋](/pandas/datasets/)

