# 12주차: 분류 모델과 성능 평가

## 학습 목표 (Learning Objectives)
1.  **분류 모델 (Classification Models)**: 데이터를 두 개 이상의 그룹으로 나누는 로지스틱 회귀와 의사결정나무 모델을 배웁니다.
2.  **성능 평가 (Metrics)**: 단순히 '정확도'만 믿으면 안 되는 이유와 정밀도, 재현율, F1-Score 등 다양한 평가지표를 익힙니다.
3.  **데이터 인코딩 (Encoding)**: 컴퓨터가 이해할 수 있도록 문자를 숫자로 변환하는 기술을 배웁니다.

## 강의 내용 (Course Content)

### [01. 이메일이 스팸인가요? (Classification Models)](./01_theory.md)
- **로지스틱 회귀 (Logistic Regression)**: 이름은 회귀지만 사실은 분류기입니다. (0과 1 사이의 확률).
- **의사결정나무 (Decision Tree)**: 스무고개 하듯이 질문을 던져 분류합니다.

### [02. 시험 점수가 다가 아니다 (Performance Metrics)](./02_practice.md)
- 정확도(Accuracy)의 함정: 찍어도 90점을 받는 시험이 있다면?
- 혼동 행렬(Confusion Matrix) 이해하기.
- 정밀도(Precision), 재현율(Recall), F1-Score.

### [03. 문자를 숫자로 (Feature Engineering)](./03_advanced.md)
- **Label Encoding**: 일렬로 번호 매기기 (S=0, M=1, L=2).
- **One-Hot Encoding**: 오직 하나만 1로 만들기 (Apple=[1,0,0]).
