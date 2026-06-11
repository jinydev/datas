---
layout: practice
title: "197. 뷔페 레스토랑 미끼 메뉴별 잔반 음식 쓰레기 실습"
permalink: /practice/197_restaurant_food_waste/
---

# 197. 뷔페 레스토랑 미끼 메뉴별 잔반 음식 쓰레기 실습

> **📥 [실습 주피터 노트북(.ipynb) 다운로드](practice.ipynb)**
## 실전 데이터 분석 197: 외식 프랜차이즈 미끼 고단가 메뉴 비중과 식재료 낭비

![도입 만화](img/intro_comic.png)

### 📊 실습 개요 (Tutorial Overview)
본 실습은 실제 비즈니스 및 학계에서 자주 마주하는 뷔페 레스토랑 미끼 메뉴별 잔반 음식 쓰레기를 주제로 다룹니다.
수집된 실제 통계 데이터셋을 바탕으로 Pandas 라이브러리를 통해 결측치를 과학적으로 정제하고, Seaborn 시각화를 통해 다중 요인의 입체적인 상관 경향을 진단합니다.

---

### 🛠️ 핵심 분석 실습 역량 (Core Skills)
* **결측치 median 대치 (\`fillna\`):** 야외 IoT 센서 배터리 방전 또는 트래커 계측 불량으로 발생한 음식쓰레기무게 변수의 빈칸을 안전하게 채웁니다.
* **상관 시너지 데이터 분석 및 해석:** 단변수 빈도 분포 점검 및 독립/종속 다변수 결합 시각화를 통해 실무 가설을 증명합니다.

---

## 🧐 실무 도메인 지식 가이드 (Domain Knowledge Guide)

> **🍽️ 식음료 및 식당 운영 (Food & Beverage)**
> 식음료 품질 보전, 매장 잔반(음식 쓰레기) 유발 원인 식별, 고객 평판 및 팁 분산 분석을 다루는 식음료 비즈니스 운영 분야입니다.
>
> * **음식 쓰레기(Food Waste) 절감**: 뷔페 미끼 메뉴 배치 및 계절별 선호 식자재 데이터를 통해 낭비되는 식자재 손실 원가를 예측합니다.
> * **와인 품질 및 보관 숙성**: 오크통 저장 보관 가스 농도 분석 등을 통하여 최적의 에이징 타이밍과 화학적 보전 임계치를 판별합니다.
> * **고객 대접 서비스(Tips)**: 팁 액수와 테이블 체류 시간, 성별/그룹 변수를 군집하여 고효율 고객 서비스 패턴을 발굴합니다.

---

## Step 1: 데이터 불러오기 및 기본 정보 확인 (Data Load)

![Step 1 데이터 수집 개념도](img/step1_dataset.svg)

제공된 CSV 파일을 분석 컴퓨터로 불러와 로드하고, 컬럼의 타입 및 데이터 구조를 확인합니다.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
import koreanize_matplotlib
sns.set_theme(style="whitegrid")

# 데이터 로드
df = pd.read_csv('./restaurant_food_waste.csv')
print(df.info())
print(df.head())
```

> **💻 [실행 결과]**
> ```text
> <class 'pandas.DataFrame'>
> RangeIndex: 1000 entries, 0 to 999
> Data columns (total 6 columns):
>  #   Column                  Non-Null Count  Dtype  
> ---  ------                  --------------  -----  
>  0   TableID                 1000 non-null   int64  
>  1   MenuPrice               1000 non-null   float64
>  2   MeatItemsRatio_Percent  1000 non-null   float64
>  3   TotalCustomerCount      1000 non-null   float64
>  4   FoodWasteWeight_g       985 non-null    float64
>  5   WasteLevel              1000 non-null   str    
> dtypes: float64(4), int64(1), str(1)
> memory usage: 52.9 KB
> None
>    TableID  MenuPrice  ...  FoodWasteWeight_g  WasteLevel
> 0  1970001    70918.0  ...               96.0      Type_B
> 1  1970002    72647.0  ...               64.2      Type_C
> 2  1970003    48717.0  ...              112.1      Type_A
> 3  1970004    82198.0  ...               98.3      Type_A
> 4  1970005    81262.0  ...              110.3      Type_A
> 
> [5 rows x 6 columns]
> ```


RangeIndex: 1000 entries, 0 to 999
Data columns (total 6 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   TableID                 1000 non-null   int64  
 1   MenuPrice               1000 non-null   float64
 2   MeatItemsRatio_Percent  1000 non-null   float64
 3   TotalCustomerCount      1000 non-null   float64
 4   FoodWasteWeight_g       985 non-null    float64
 5   WasteLevel              1000 non-null   str    
dtypes: float64(4), int64(1), str(1)
memory usage: 47.0 KB
> 
>    TableID  MenuPrice  MeatItemsRatio_Percent  TotalCustomerCount  FoodWasteWeight_g WasteLevel
0  1970001    70918.0                    51.9                74.7               96.0     Type_B
1  1970002    72647.0                    59.5               135.3               64.2     Type_C
2  1970003    48717.0                    62.8                74.8              112.1     Type_A
3  1970004    82198.0                    48.5                78.2               98.3     Type_A
4  1970005    81262.0                    21.2               102.5              110.3     Type_A
> ```

---

## Step 2: 결측치 및 데이터 정제 (Data Cleaning)

![Step 2 데이터 정제 개념도](img/step2_missing_values.svg)

수집 과정에서 빈칸으로 기록된 결측값(NaN)의 존재 여부를 진단하고, 데이터 도메인 성격에 부합하는 통계 수치 대입 기법으로 정제합니다.

```python
# 1. 컬럼별 결측치 개수 확인
print("--- 정제 전 결측치 확인 ---")
print(df.isnull().sum())

# 2. 결측치 전처리 및 대치 수행
median_val = df['FoodWasteWeight_g'].median().round(1)
df['FoodWasteWeight_g'] = df['FoodWasteWeight_g'].fillna(median_val)
print(df.isnull().sum())
```

> **💻 [실행 결과]**
> ```text
> --- 정제 전 결측치 확인 ---
> TableID                    0
> MenuPrice                  0
> MeatItemsRatio_Percent     0
> TotalCustomerCount         0
> FoodWasteWeight_g         15
> WasteLevel                 0
> dtype: int64
> TableID                   0
> MenuPrice                 0
> MeatItemsRatio_Percent    0
> TotalCustomerCount        0
> FoodWasteWeight_g         0
> WasteLevel                0
> dtype: int64
> ```


MenuPrice                      0
MeatItemsRatio_Percent         0
TotalCustomerCount             0
FoodWasteWeight_g              15
WasteLevel                     0
> 
> --- 정제 후 결측치 확인 ---
> TableID                        0
MenuPrice                      0
MeatItemsRatio_Percent         0
TotalCustomerCount             0
FoodWasteWeight_g              0
WasteLevel                     0
> ```

### 💡 분석가의 통찰 (Analyst's Insight)
* **중앙값 대입 적용의 비즈니스 및 통계적 근거:** 음식쓰레기무게 정보는 긴 꼬리 분포나 일부 특이 이상치에 의해 평균이 한쪽으로 치우치기 쉬우므로 통계적 안정성이 강한 중앙값으로 결측을 대치합니다.

---

## Step 3: 단변수 분포 분석 (Univariate EDA)

![Step 3 시각화 개념도](img/step3_visualization.svg)

가장 먼저 핵심 변수가 전체 데이터에서 어떤 빈도와 분포를 가졌는지 단일 변수 시각화를 통해 파악해 봅니다.

```python
plt.figure(figsize=(8, 5))

# 단변수 분석 그래프 생성
sns.histplot(data=df, x='FoodWasteWeight_g', kde=True, color='teal')
plt.title('뷔페 레스토랑 미끼 메뉴별 잔반 음식 쓰레기 빈도 분포', fontsize=14, fontweight='bold')
plt.show()
```

> **💻 [실행 결과]**
> ![실행 결과 시각화](img/exec_step_3.svg)


### 💡 시각화 차트 읽는 법 & 인사이트
* **밀도 집중 대역 확인:** FoodWasteWeight_g 변수의 종형 곡선 또는 비대칭 스케일을 관찰하여, 다수가 모여 있는 주류 대역과 이상 극단치 구간을 감별합니다.

---

## Step 4: 다변수 상관관계 및 이상치 분석 (Multivariate EDA)

![Step 4 상관관계 분석 개념도](img/step4_multivariate.svg)

두 개 이상의 변수를 동시에 결합하여, 조건에 따른 수치 차이나 독립 변수와 종속 변수 간의 통계적 경향을 분석합니다.

```python
plt.figure(figsize=(9, 6))

# 다변수 분석 그래프 생성
sns.scatterplot(data=df, x='MeatItemsRatio_Percent', y='FoodWasteWeight_g', hue='WasteLevel', palette='coolwarm', alpha=0.8)
plt.title('MeatItemsRatio_Percent와 FoodWasteWeight_g 상관성 및 WasteLevel 대조', fontsize=14, fontweight='bold')
plt.show()
```

> **💻 [실행 결과]**
> ![실행 결과 시각화](img/exec_step_4.svg)


### 💡 코드 딥다이브 & 비즈니스 통찰 (Analyst's Insight)
* **분산 경향과 위험 타겟 집중 진단:** X축과 Y축 간의 선형 양/음의 관계선 흐름 속에서, WasteLevel 색상 점들이 특정한 영역에 쏠려 있는지 판독하여 다중 요인의 연계 시너지를 증명합니다.

---

## Step 5: 통계적 직관과 해석 (Statistical Logic)

> 💡 **[분석 도메인 통계 지식 한눈에 보기]**
> 본 실습은 뷔페 레스토랑 미끼 메뉴별 잔반 음식 쓰레기를 판독하기 위한 의사결정 프레임워크를 제공합니다.
> * 단순 평균(Mean) 비교의 함정을 방어하기 위해 집단 간의 표준편차(Standard Deviation) 분산을 대조하고, 다변수 회귀 검증을 통해 우연의 일치가 아님을 유의 수준(p-value)을 통해 입증하는 의사결정 습관이 중요합니다.

---

## 🎯 30분 강의 마무리 및 심화 과제

오늘 우리는 실전 데이터셋을 분석하여 판다스로 데이터를 가공 및 정제하고, 시각화를 활용하여 핵심 변수 간의 통계적 유의성을 검증했습니다. 데이터 속에서 숨겨진 패턴을 올바른 시각으로 탐색하는 능력이 데이터 사이언티스트의 가장 강력한 무기입니다.

### 📝 심화 과제 (Advanced Challenge)
* **결측치를 채우기 전과 후의 통계량 변화 대조:** 전후의 평균값 및 분산 격차를 코드로 구해 설명력을 확인하세요.
* **타겟 변수 기준 그룹화 비교:** 타겟 레이블값 유무에 따른 핵심 피처들의 중간값 테이블 요약을 출력해 분석해 보세요.
