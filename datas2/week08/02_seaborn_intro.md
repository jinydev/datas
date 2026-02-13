# 8-2. Matplotlib보다 쉬운 Seaborn

## 1. Seaborn의 특징
*   Pandas 데이터프레임과 찰떡궁합입니다. (`data=df` 라고만 써주면 됨)
*   복잡한 통계 연산(평균, 신뢰구간)을 알아서 그려줍니다.

## 2. 산점도와 선 그래프
*   `sns.scatterplot`: 점 찍기
*   `sns.lineplot`: 선 긋기
*   `hue` 옵션: 색상으로 그룹 나누기 (이게 진짜 강력합니다!)

## 3. [응용 예제] 팁 데이터 분석 (Tips Dataset)
Seaborn에 내장된 식당 팁 데이터를 사용해봅시다.
"식사 금액(total_bill)이 많으면 팁(tip)도 많이 줄까?"

[소스 코드 실행하기](src/02_seaborn_intro.py) | [Colab에서 열기](src/02_seaborn_intro.ipynb)
