# 14주차 1강: 후반기 총정리 (Review)

## 14.1.1. Pandas 데이터 분석 (Week 8~10)
- **DataFrame**: 행과 열로 된 2차원 데이터 표.
- **I/O**: `read_csv`로 읽고 `to_csv`로 저장.
- **Selection**: `df['Column']`, `df.loc[이름]`, `df.iloc[번호]`.
- **Preprocessing**: 
    - 결측치 처리 (`dropna`, `fillna`).
    - 정렬 (`sort_values`).
- **Visualization**: `df.plot()`, Seaborn(`heatmap`, `lmplot`).

## 14.1.2. 머신러닝 기초 (Week 11)
- **지도학습**: 정답(Target)이 있는 공부. (회귀, 분류)
- **Train/Test Split**: 학습용과 검증용 데이터를 나누는 이유.
- **Linear Regression**: 숫자를 예측하는 가장 기초적인 선형 모델.
- **평가**: MSE, RMSE, R2 Score.

## 14.1.3. 분류와 튜닝 (Week 12~13)
- **Classification**: 범주(Class)를 맞추는 문제.
    - Logistic Regression, Decision Tree.
- **평가**: 정확도의 함정, 정밀도, 재현율, F1-Score.
- **Preprocessing**: 문자를 숫자로 (Label Encoding, One-Hot Encoding).
- **Clustering**: 정답 없는 데이터 묶기 (K-Means).
- **Tuning**: Grid Search로 최적의 파라미터 찾기.
