# 10주차: Pandas 데이터 처리와 시각화

## 학습 목표 (Learning Objectives)
1.  **결측치 처리 (Handling Missing Data)**: 데이터에 비어있는 값(Null)을 찾아내고, 채우거나 삭제하는 전처리 방법을 익힙니다.
2.  **데이터 정렬 (Sorting)**: 값을 기준으로 데이터를 정렬하여 순위를 매기거나 패턴을 찾습니다.
3.  **데이터 시각화 (Visualization)**: Pandas 내장 시각화 기능과 Seaborn 라이브러리를 활용하여 데이터를 그래프로 표현합니다.

## 강의 내용 (Course Content)

### [01. 구멍 난 데이터 수리하기 (Missing Values)](./01_theory.md)
- `isnull()`: 결측치 탐지 레이더.
- `dropna()`: 깨진 데이터 버리기.
- `fillna()`: 평균값이나 특정 값으로 메우기.

### [02. 줄 세우기 (Sorting & Stats)](./02_practice.md)
- `sort_values()`: 오름차순/내림차순 정렬.
- `corr()`: 상관계수 (누구랑 친하니?).

### [03. 화려한 시각화 (Seaborn)](./03_advanced.md)
- Pandas `plot()`: 빠르고 간편하게 그리기.
- Seaborn: 통계적 시각화의 끝판왕.
- `heatmap`: 상관관계 시각화.
