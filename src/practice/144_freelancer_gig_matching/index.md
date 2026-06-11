---
layout: practice
title: "144. 프리랜서 마켓 매칭 속도 및 서비스 단가 실습"
permalink: /practice/144_freelancer_gig_matching/
---

# 144. 프리랜서 마켓 매칭 속도 및 서비스 단가 실습

> **📥 [실습 주피터 노트북(.ipynb) 다운로드](practice.ipynb)**
## 실전 데이터 분석 144: 긱 이코노미 중개 플랫폼 매칭 대기행렬 인자

![도입 만화](img/intro_comic.png)

### 📊 실습 개요 (Tutorial Overview)
본 실습은 실제 비즈니스 및 학계에서 자주 마주하는 프리랜서 마켓 매칭 속도 및 서비스 단가를 주제로 다룹니다.
수집된 실제 통계 데이터셋을 바탕으로 Pandas 라이브러리를 통해 결측치를 과학적으로 정제하고, Seaborn 시각화를 통해 다중 요인의 입체적인 상관 경향을 진단합니다.

---

### 🛠️ 핵심 분석 실습 역량 (Core Skills)
* **결측치 median 대치 (\`fillna\`):** 설문 평가 응답 거부 또는 사내 HR 데이터 연동 누락으로 발생한 매칭소요시간 변수의 빈칸을 안전하게 채웁니다.
* **상관 시너지 데이터 분석 및 해석:** 단변수 빈도 분포 점검 및 독립/종속 다변수 결합 시각화를 통해 실무 가설을 증명합니다.

---

## 🧐 실무 도메인 지식 가이드 (Domain Knowledge Guide)

> **👥 인사 및 조직 문화 (HR & Workplace Analysis)**
> 인적 자원 관리(HR Analytics)는 핵심 인재의 이탈(Attrition) 방지, 사내 직무 이동 성과, 복지 리텐션을 다루는 과학적 기업 운영 분야입니다.
>
> * **직원 자발적 퇴사(Attrition)**: 야근 빈도, 직무 몰입도(Engagement), 급여 대비 승진 연한 격차 등을 통해 조기 이탈 리스크 직원을 경보합니다.
> * **채용 채널 성과 분석**: 직무 코딩테스트 및 전형 결과와 입사 사후 실제 성과 데이터 간의 타당성(상관) 관계를 실증 분석합니다.
> * **원격 근무 효율성**: 원격/사무실 하이브리드 근무자의 생산성 점수와 근무 만족도 분산 차이를 통계 검증(T-test 등)합니다.

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
df = pd.read_csv('./freelancer_gig_matching.csv')
print(df.info())
print(df.head())
```

> **💻 [실행 결과]**
> ```text
> <class 'pandas.DataFrame'>
> RangeIndex: 1000 entries, 0 to 999
> Data columns (total 6 columns):
>  #   Column               Non-Null Count  Dtype  
> ---  ------               --------------  -----  
>  0   ProjectID            1000 non-null   int64  
>  1   ProjectBudget_K      1000 non-null   float64
>  2   RequiredSkillsCount  1000 non-null   float64
>  3   FreelancerRating     1000 non-null   float64
>  4   MatchingTimeHours    985 non-null    float64
>  5   CompletionOnTime     1000 non-null   int64  
> dtypes: float64(4), int64(2)
> memory usage: 47.0 KB
> None
>    ProjectID  ProjectBudget_K  ...  MatchingTimeHours  CompletionOnTime
> 0    1440001             49.0  ...               23.6                 0
> 1    1440002             73.1  ...               33.5                 0
> 2    1440003             76.4  ...                4.2                 1
> 3    1440004            112.1  ...                9.5                 0
> 4    1440005            102.4  ...               30.1                 0
> 
> [5 rows x 6 columns]
> ```


RangeIndex: 1000 entries, 0 to 999
Data columns (total 6 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   ProjectID            1000 non-null   int64  
 1   ProjectBudget_K      1000 non-null   float64
 2   RequiredSkillsCount  1000 non-null   float64
 3   FreelancerRating     1000 non-null   float64
 4   MatchingTimeHours    985 non-null    float64
 5   CompletionOnTime     1000 non-null   int64  
dtypes: float64(4), int64(2)
memory usage: 47.0 KB
> 
>    ProjectID  ProjectBudget_K  RequiredSkillsCount  FreelancerRating  MatchingTimeHours  CompletionOnTime
0    1440001             49.0                117.1             115.3               23.6                 0
1    1440002             73.1                 67.8              83.4               33.5                 0
2    1440003             76.4                107.2              79.3                4.2                 1
3    1440004            112.1                 96.5             130.2                9.5                 0
4    1440005            102.4                 84.8              82.0               30.1                 0
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
median_val = df['MatchingTimeHours'].median().round(1)
df['MatchingTimeHours'] = df['MatchingTimeHours'].fillna(median_val)
print(df.isnull().sum())
```

> **💻 [실행 결과]**
> ```text
> --- 정제 전 결측치 확인 ---
> ProjectID               0
> ProjectBudget_K         0
> RequiredSkillsCount     0
> FreelancerRating        0
> MatchingTimeHours      15
> CompletionOnTime        0
> dtype: int64
> ProjectID              0
> ProjectBudget_K        0
> RequiredSkillsCount    0
> FreelancerRating       0
> MatchingTimeHours      0
> CompletionOnTime       0
> dtype: int64
> ```


ProjectBudget_K                0
RequiredSkillsCount            0
FreelancerRating               0
MatchingTimeHours              15
CompletionOnTime               0
> 
> --- 정제 후 결측치 확인 ---
> ProjectID                      0
ProjectBudget_K                0
RequiredSkillsCount            0
FreelancerRating               0
MatchingTimeHours              0
CompletionOnTime               0
> ```

### 💡 분석가의 통찰 (Analyst's Insight)
* **중앙값 대입 적용의 비즈니스 및 통계적 근거:** 매칭소요시간 정보는 긴 꼬리 분포나 일부 특이 이상치에 의해 평균이 한쪽으로 치우치기 쉬우므로 통계적 안정성이 강한 중앙값으로 결측을 대치합니다.

---

## Step 3: 단변수 분포 분석 (Univariate EDA)

![Step 3 시각화 개념도](img/step3_visualization.svg)

가장 먼저 핵심 변수가 전체 데이터에서 어떤 빈도와 분포를 가졌는지 단일 변수 시각화를 통해 파악해 봅니다.

```python
plt.figure(figsize=(8, 5))

# 단변수 분석 그래프 생성
sns.histplot(data=df, x='MatchingTimeHours', kde=True, color='teal')
plt.title('프리랜서 마켓 매칭 속도 및 서비스 단가 빈도 분포', fontsize=14, fontweight='bold')
plt.show()
```

> **💻 [실행 결과]**
> ![실행 결과 시각화](img/exec_step_3.svg)


### 💡 시각화 차트 읽는 법 & 인사이트
* **밀도 집중 대역 확인:** MatchingTimeHours 변수의 종형 곡선 또는 비대칭 스케일을 관찰하여, 다수가 모여 있는 주류 대역과 이상 극단치 구간을 감별합니다.

---

## Step 4: 다변수 상관관계 및 이상치 분석 (Multivariate EDA)

![Step 4 상관관계 분석 개념도](img/step4_multivariate.svg)

두 개 이상의 변수를 동시에 결합하여, 조건에 따른 수치 차이나 독립 변수와 종속 변수 간의 통계적 경향을 분석합니다.

```python
plt.figure(figsize=(9, 6))

# 다변수 분석 그래프 생성
sns.scatterplot(data=df, x='FreelancerRating', y='MatchingTimeHours', hue='CompletionOnTime', palette='coolwarm', alpha=0.8)
plt.title('FreelancerRating와 MatchingTimeHours 상관성 및 CompletionOnTime 대조', fontsize=14, fontweight='bold')
plt.show()
```

> **💻 [실행 결과]**
> ![실행 결과 시각화](img/exec_step_4.svg)


### 💡 코드 딥다이브 & 비즈니스 통찰 (Analyst's Insight)
* **분산 경향과 위험 타겟 집중 진단:** X축과 Y축 간의 선형 양/음의 관계선 흐름 속에서, CompletionOnTime 색상 점들이 특정한 영역에 쏠려 있는지 판독하여 다중 요인의 연계 시너지를 증명합니다.

---

## Step 5: 통계적 직관과 해석 (Statistical Logic)

> 💡 **[분석 도메인 통계 지식 한눈에 보기]**
> 본 실습은 프리랜서 마켓 매칭 속도 및 서비스 단가를 판독하기 위한 의사결정 프레임워크를 제공합니다.
> * 단순 평균(Mean) 비교의 함정을 방어하기 위해 집단 간의 표준편차(Standard Deviation) 분산을 대조하고, 다변수 회귀 검증을 통해 우연의 일치가 아님을 유의 수준(p-value)을 통해 입증하는 의사결정 습관이 중요합니다.

---

## 🎯 30분 강의 마무리 및 심화 과제

오늘 우리는 실전 데이터셋을 분석하여 판다스로 데이터를 가공 및 정제하고, 시각화를 활용하여 핵심 변수 간의 통계적 유의성을 검증했습니다. 데이터 속에서 숨겨진 패턴을 올바른 시각으로 탐색하는 능력이 데이터 사이언티스트의 가장 강력한 무기입니다.

### 📝 심화 과제 (Advanced Challenge)
* **결측치를 채우기 전과 후의 통계량 변화 대조:** 전후의 평균값 및 분산 격차를 코드로 구해 설명력을 확인하세요.
* **타겟 변수 기준 그룹화 비교:** 타겟 레이블값 유무에 따른 핵심 피처들의 중간값 테이블 요약을 출력해 분석해 보세요.
