---
layout: mathplotlib
title: 데이터 시각화 (Matplotlib/Seaborn)
permalink: /mathplotlib/
description: "파이썬의 대표적인 시각화 라이브러리인 Matplotlib과 통계 기반 고급 시각화 라이브러리인 Seaborn을 활용하여 데이터를 한눈에 파악할 수 있는 그래프를 그리는 방법을 학습합니다."
---

# 데이터 시각화 (Matplotlib/Seaborn)

파이썬의 대표적인 시각화 라이브러리인 `Matplotlib`과 통계 기반 고급 시각화 라이브러리인 `Seaborn`을 활용하여 데이터를 한눈에 파악할 수 있는 그래프를 그리는 방법을 학습합니다.

![Matplotlib and Seaborn Illustration](./img/matplotlib_illustration.png)

---

## 5.0 시각화 개념과 기초 {#section-00}
판다스 내장 시각화와 Matplotlib, Seaborn 생태계를 비교하며 시각화의 본질을 이해합니다. 실습에 필요한 장난감(Toy) 데이터를 준비하고 시각화의 기본 원리를 다집니다.

- [5.0.1 판다스 내장 시각화와 한계](/mathplotlib/00_visualization_basics/01_pandas_visualization/)
- [5.0.2 시각화 생태계: Matplotlib과 Seaborn](/mathplotlib/00_visualization_basics/02_matplotlib_seaborn/)
- [5.0.3 장난감(Toy) 데이터를 활용한 실습 준비](/mathplotlib/00_visualization_basics/03_toy_data_dataframe/)
- [5.0.4 데이터 시각화의 목적과 본질](/mathplotlib/00_visualization_basics/04_visualization_intro/)

## 5.1 5대 기본 차트와 원리 {#section-01}
데이터 분석에서 가장 빈번하게 사용되는 선 그래프, 산점도, 막대 그래프, 히스토그램, 파이 차트의 원리를 배웁니다. 각 차트가 어떤 목적과 데이터 타입에 적합한지 학습합니다.

- [5.1.1 선 그래프 (Line Plot) 기초와 실습](/mathplotlib/01_core_charts/01_line_plot/)
- [5.1.2 Seaborn 선 그래프 (시계열 데이터)](/mathplotlib/01_core_charts/02_line_plot/)
- [5.1.3 산점도 (Scatter Plot)와 데이터 분포](/mathplotlib/01_core_charts/03_scatter_plot/)
- [5.1.4 막대 그래프 (Bar Plot)와 비교 분석](/mathplotlib/01_core_charts/04_bar_plot/)
- [5.1.5 히스토그램 (Histogram)과 구간 빈도](/mathplotlib/01_core_charts/05_histogram/)
- [5.1.6 파이 차트 (Pie Chart)와 비율 분석](/mathplotlib/01_core_charts/06_pie_chart/)

## 5.2 Seaborn과 데이터셋 {#section-02}
Seaborn 라이브러리의 샘플 데이터셋을 불러와 초기 탐색적 데이터 분석(EDA)을 경험합니다. 변수의 타입에 따라 Countplot, Histplot 등 적절한 그래프를 매칭하는 법을 익힙니다.

- [5.2.1 Seaborn과 장난감 데이터셋 개요](/mathplotlib/02_seaborn_dataset/01_pydataset_intro/)
- [5.2.2 초기 데이터 탐색 (EDA) 기법](/mathplotlib/02_seaborn_dataset/02_pydataset_install/)
- [5.2.3 시각화를 결정짓는 2가지 변수 타입](/mathplotlib/02_seaborn_dataset/03_pydataset_import/)
- [5.2.4 Seaborn 첫 그래프: Countplot과 Histplot](/mathplotlib/02_seaborn_dataset/04_seaborn_graph/)

## 5.3 시각화 고급 꾸미기 {#section-03}
Figure와 Axes의 계층 구조를 이해하고, GridSpec을 활용한 다중 레이아웃을 구성합니다. 색상, 테마, 격자 등 다양한 속성을 제어하여 그래프의 디자인과 가독성을 극대화합니다.

- [5.3.1 도화지(Figure)와 액자(Ax) 구조 완벽 해부](/mathplotlib/03_advanced_styling/01_figure_subplot/)
- [5.3.2 비대칭 테트리스 레이아웃 (GridSpec)](/mathplotlib/03_advanced_styling/02_gridspec_layout/)
- [5.3.3 스타일링 끝판왕 (색상, 속성, 격자)](/mathplotlib/03_advanced_styling/03_styling/)

## 5.4 분포 및 통계 차트 심화 {#section-04}
Box Plot과 Violin Plot을 통해 데이터의 통계적 분포와 이상치를 시각적으로 검출하는 기법을 배웁니다. Heatmap과 Pairplot을 이용하여 여러 변수 간의 복잡한 상관관계를 효과적으로 분석합니다.

- [5.4.1 상자그림 (Box Plot) 완벽 해부](/mathplotlib/04_advanced_statistics/01_box_plot/)
- [5.4.2 바이올린 플롯 (Violin Plot)과 데이터 대칭](/mathplotlib/04_advanced_statistics/02_violin_plot/)
- [5.4.3 상관관계 폭격기: Heatmap과 Pairplot](/mathplotlib/04_advanced_statistics/03_correlation_viz/)
