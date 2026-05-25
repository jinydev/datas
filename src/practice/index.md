---
layout: practice
title: "데이터 분석 실습 (PyData)"
permalink: /practice/
---

# PyData 실전 데이터 분석 커리큘럼

Pandas와 Seaborn을 활용하여 40개의 인기 있는 데이터 셋을 직접 분석하고 시각화하는 실무 중심의 실습 공간입니다. 
데이터 사이언스 역량은 **코드(Pandas)**, **시각화(Seaborn)**, 그리고 **통계적 직관(Statistics)**이라는 3가지 축이 맞물려야 완성됩니다. 아래의 커리큘럼 맵을 통해 단계별 학습 목표를 확인하세요.

---

## 🗺️ 파이데이터 40개 모듈 커리큘럼 맵

| 모듈 번호 & 데이터 셋 | 데이터 분석 테마 | Pandas / 분석 스킬 | 시각화 (Seaborn) | 핵심 통계 개념 (수학적 직관) |
| :--- | :--- | :--- | :--- | :--- |
| **00. [intro](/practice/00_pydata_intro/)** | **오리엔테이션** | PyData 생태계 개요 | 데이터 시각화의 목적 | 통계 분석 워크플로우 기초 |
| **01. [titanic](/practice/01_titanic/)** | **생존자 예측** | 결측치 처리 (`fillna`) | `barplot`, `countplot` | 확률과 생존율 (Probability) |
| **02. [iris](/practice/02_iris/)** | **품종 분류** | 기술통계 (`describe`) | `pairplot`, `scatterplot` | 다차원 데이터와 클래스 분류 |
| **03. [tips](/practice/03_tips/)** | **팁 분석** | 그룹화 (`groupby`) | `lmplot`, `boxplot` | **선형 회귀 (Linear Regression)** |
| **04. [penguins](/practice/04_penguins/)** | **생물학적 특징** | 결측치 제거 (`dropna`) | `histplot`, `kdeplot` | **정규 분포와 확률 밀도** |
| **05. [flights](/practice/05_flights/)** | **시계열 기초** | 피벗 테이블 (`pivot`) | `lineplot`, `heatmap` | 시계열 데이터의 계절성(Seasonality) |
| **06. [diamonds](/practice/06_diamonds/)** | **가격 예측** | 범주형 데이터 변환 | `violinplot`, `boxenplot` | 데이터 분포와 중앙값(Median) |
| **07. [mpg](/practice/07_mpg/)** | **연비 분석** | 불리언 인덱싱 | `regplot`, `jointplot` | 다중 회귀 분석 기초 |
| **08. [anscombe](/practice/08_anscombe/)** | **통계의 함정** | 통계 함수 (`mean`, `var`) | 서브플롯 (`FacetGrid`) | **평균, 분산, 표준편차의 직관** |
| **09~11. 기타** | **우주/뇌과학/택시** | 데이터 병합 (`merge`) | 다차원 시각화 | 샘플링과 모집단 |
| **12. [geyser](/practice/12_geyser/)** | **지구과학 분석** | 밀도 추정 | `kdeplot` 2D | 바이모달(이항) 분포 |
| **13. [car_crashes](/practice/13_car_crashes/)** | **사고 요인 분석** | 상관 행렬 (`corr`) | `heatmap` | **피어슨 상관계수 (Correlation)** |
| **14~20. 기타** | **금융/환경/시계열** | 이동 평균 (`rolling`) | 시계열 트렌드 뷰 | 시계열의 노이즈와 트렌드 |
| **21. [wine](/practice/21_wine/)** | **품질 예측** | 외부 파일 로드 (`read_csv`) | 다중 `boxplot` | 타겟 변수와의 상관관계 |
| **22. [bike](/practice/22_bike/)** | **수요 예측** | 시계열 추출 (`dt.month`) | `pointplot` | 독립변수와 종속변수 |
| **23. [housing](/practice/23_housing/)** | **집값 지리 분석** | 필터링 (`loc`) | 지리적 산점도 (`hue`, `size`)| **IQR과 이상치(Outlier) 울타리** |
| **24. [cancer](/practice/24_cancer/)** | **유방암 진단** | 데이터 정규화 (`scale`) | `violinplot` 밀도 | **Z-Score 표준화와 분별력** |
| **25. [student](/practice/25_student/)** | **성적 예측** | 데이터 누수(Leakage) 인지| 오버레이 플롯 | 요인별 가중치와 랭킹 |
| **26. [heart](/practice/26_heart/)** | **심장 질환** | 비닝/범주화 (`pd.cut`) | 클래스 불균형 비교 | 다중 변수의 상호작용 |
| **27. [adult](/practice/27_adult/)** | **소득 예측** | 위장 결측치(`?`) 필터링 | 교차 분석 (`hue`) | **정규 분포와 왜도(Skewness)** |
| **28. [marketing](/practice/28_marketing/)** | **영업 전환율** | 비율 계산 (`value_counts`)| `stripplot`, `pie` | 극단적 불균형(Imbalance) 통계 |
| **29. [ecommerce](/practice/29_ecommerce/)** | **매출 트렌드** | 피처 엔지니어링 (파생 변수)| `pivot_table`, `heatmap`| 코호트 분석 기초 |
| **30. [superstore](/practice/30_superstore/)**| **마트 KPI** | 부서별 요약 통계 | `scatterplot`, `barplot`| 손익분기점과 미끼상품(Loss Leader) |
| **31. [netflix](/practice/31_netflix/)** | **넷플릭스 콘텐츠** | 결측치 및 빈도 요약 | `countplot`, `histplot` | **범주 데이터와 롱테일 분포** |
| **32. [spotify](/practice/32_spotify/)** | **음악 인기도** | 다중 컬럼 정렬 & 필터링 | `histplot`, `scatterplot` | **오디오 특성 간 피어슨 상관관계** |
| **33. [airbnb](/practice/33_airbnb/)** | **숙소 가격** | 이상치 필터링 & `groupby` | `boxplot`, `countplot` | **중앙값과 왜도(Skewness)** |
| **34. [customer_segmentation](/practice/34_customer_segmentation/)** | **고객 군집화** | 파생 변수 & 기술 통계 | `scatterplot`, `histplot` | **군집 내 분산과 K-Means 직관** |
| **35. [retail_sales](/practice/35_retail_sales/)** | **매출 분석** | 시계열 변환 & `groupby` | `lineplot`, `barplot` | **매출 트렌드와 이동 평균** |
| **36. [fifa_world_cup](/practice/36_fifa_world_cup/)** | **월드컵 역사** | 데이터 병합 & 필터링 | `barplot`, `lineplot` | **역사적 이상치와 장기 트렌드** |
| **37. [covid19](/practice/37_covid19/)** | **코로나 트렌드** | 누적 합계 & 비율 계산 | `lineplot`, `scatterplot` | **성장률과 상관관계 분석** |
| **38. [employee_attrition](/practice/38_employee_attrition/)** | **퇴사 원인** | 그룹별 평균 & 비율 계산 | `countplot`, `boxplot` | **오즈비(Odds Ratio)와 로지스틱 회귀** |
| **39. [food_delivery](/practice/39_food_delivery/)** | **배달 서비스** | 시간대별 구간화 (`pd.cut`) | `histplot`, `boxplot` | **평균 배달 시간과 표준 편차** |
| **40. [pokemon](/practice/40_pokemon/)** | **포켓몬 능력치** | 여러 컬럼의 통계 계산 | `scatterplot`, `countplot` | **다차원 분포와 상관 관계** |

---

## 🎯 학습 가이드 (어떻게 공부해야 하나요?)

1. **초급자:** 1번 `titanic`부터 10번 모듈까지 순서대로 진행하며 Pandas 코딩과 Seaborn 그래프 그리기에 익숙해집니다.
2. **중급자:** 21번 `wine`부터 시작하는 **Phase 3 (실전 CSV)** 파트를 집중적으로 공략하여, 실제 기업에서 다루는 실무 분석 워크플로우를 체화합니다.
3. **통계 집중:** 표의 맨 우측 열인 **'핵심 통계 개념'**이 굵은 글씨로 표시된 모듈(`tips`, `anscombe`, `car_crashes`, `housing`, `cancer`, `adult`)을 중점적으로 학습하세요. 수포자를 위한 친절한 비유와 수식이 포함되어 있습니다.
