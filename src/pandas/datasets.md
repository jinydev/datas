---
layout: pandas
title: "Pandas/Seaborn 기본 제공 데이터 셋"
permalink: /pandas/datasets/
---

# Pandas / Seaborn 실습용 기본 데이터 셋 개요

데이터 분석 및 시각화를 학습할 때 가장 먼저 마주하는 것이 바로 "어떤 데이터로 연습할 것인가?" 입니다. 매번 공공데이터포털 등에서 CSV 파일을 다운로드 받는 것은 매우 번거로운 일입니다. 

따라서 `seaborn` 라이브러리나 `pydataset` 패키지는 코드 한 줄로 바로 불러올 수 있는 **기본 제공 데이터 셋(Built-in Datasets)**을 제공합니다. 이 데이터들은 이미 전 세계 데이터 분석가들이 튜토리얼에서 사용하는 "표준 예제 데이터"로 자리 잡았습니다.

---

## 주요 데이터 셋 목록

### 🚢 1. 타이타닉 (Titanic) 데이터 셋 {#titanic}

머신러닝과 데이터 분석 입문자라면 누구나 한 번쯤 거쳐가는 전설적인 데이터 셋입니다. 1912년 타이타닉호 침몰 사고 당시 탑승객들의 생존 여부와 인적 사항을 담고 있습니다.

- **데이터 불러오기**:
  ```python
  import seaborn as sns
  titanic_df = sns.load_dataset('titanic')
  ```
- **주요 컬럼**:
  - `survived`: 생존 여부 (0 = 사망, 1 = 생존)
  - `pclass`: 객실 등급 (1, 2, 3등석)
  - `sex`, `age`: 성별, 나이
  - `fare`: 지불한 요금
- **분석 포인트**: 성별, 나이, 객실 등급이 생존율에 어떤 영향을 미쳤는지 분석하고 시각화하기 좋습니다.

---

### 🌸 2. 붓꽃 (Iris) 데이터 셋 {#iris}

영국의 통계학자 로널드 피셔(Ronald Fisher)가 1936년에 공개한 데이터로, 통계학과 분류(Classification) 모델 실습의 교과서입니다. 세 가지 붓꽃 품종의 꽃받침과 꽃잎 길이를 측정했습니다.

- **데이터 불러오기**:
  ```python
  import seaborn as sns
  iris_df = sns.load_dataset('iris')
  ```
- **주요 컬럼**:
  - `sepal_length`, `sepal_width`: 꽃받침의 길이와 너비
  - `petal_length`, `petal_width`: 꽃잎의 길이와 너비
  - `species`: 붓꽃의 품종 (`setosa`, `versicolor`, `virginica`)
- **분석 포인트**: 군집화(Clustering)나 산점도(Scatter plot)를 통해 각 품종이 데이터 공간에서 어떻게 나뉘는지 시각화하기 좋습니다.

---

### 🍽️ 3. 팁 (Tips) 데이터 셋 {#tips}

레스토랑 서버가 받은 팁 데이터입니다. 손님의 성별, 흡연 여부, 요일, 방문 시간대 등에 따라 팁을 얼마나 주는지 파악할 수 있습니다.

- **데이터 불러오기**:
  ```python
  import seaborn as sns
  tips_df = sns.load_dataset('tips')
  ```
- **주요 컬럼**:
  - `total_bill`: 총 결제 금액
  - `tip`: 지불한 팁
  - `sex`: 결제자의 성별
  - `smoker`: 흡연자 포함 여부
  - `day`, `time`: 요일 및 식사 시간대 (Lunch, Dinner)
  - `size`: 일행의 수
- **분석 포인트**: 총 결제 금액(`total_bill`)과 팁(`tip`) 간의 상관관계, 요일 및 시간대별 팁의 변화를 막대그래프나 박스플롯으로 그리기 좋습니다.

---

### 🐧 4. 펭귄 (Penguins) 데이터 셋 {#penguins}

남극 팔머 연구소에서 수집한 펭귄 데이터로, 붓꽃(Iris) 데이터 셋의 훌륭한 대안으로 최근 각광받고 있습니다. 결측치(NaN)가 일부 포함되어 있어 데이터 전처리 실습용으로도 매우 좋습니다.

- **데이터 불러오기**:
  ```python
  import seaborn as sns
  penguins_df = sns.load_dataset('penguins')
  ```
- **주요 컬럼**:
  - `species`: 펭귄 종 (`Adelie`, `Chinstrap`, `Gentoo`)
  - `island`: 서식하는 섬
  - `bill_length_mm`, `bill_depth_mm`: 부리의 길이와 깊이
  - `flipper_length_mm`: 날개 길이
  - `body_mass_g`: 체중
- **분석 포인트**: 종별 체중 분포, 서식지별 펭귄 종 분포를 다양한 색상의 히스토그램이나 바이올린 플롯으로 표현하기 좋습니다.
