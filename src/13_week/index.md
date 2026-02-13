---
layout: default
title: "13주차: 군집 분석과 모델 튜닝"
---

# 13주차: 군집 분석과 모델 튜닝

## 학습 목표 (Learning Objectives)
1.  **군집화 (Clustering)**: 정답이 없는 데이터에서 비슷한 그룹을 묶어내는 K-Means 알고리즘을 배웁니다.
2.  **교차 검증 (Cross Validation)**: 데이터를 여러 번 나누어 검증함으로써 모델의 신뢰도를 높이는 방법을 익힙니다.
3.  **하이퍼파라미터 튜닝 (Tuning)**: 모델의 성능을 최대로 끌어올리기 위한 최적의 설정값을 찾는 법을 배웁니다.

## 강의 내용 (Course Content)

### [01. 끼리끼리 모여라 (K-Means Clustering)](./01_theory.html)
- 비지도 학습의 대표주자, K-Means.
- K값 설정의 중요성 (Elbow Method).
- 실루엣 계수(Silhouette Score)로 평가하기.

### [02. 모의고사는 여러 번 (Cross Validation)](./02_practice.html)
- K-Fold 교차 검증: 데이터를 K등분해서 돌아가며 시험 보기.
- 과대적합 방지와 일반화 성능 측정.

### [03. 최강의 모델 만들기 (Grid Search)](./03_advanced.html)
- 하이퍼파라미터(Hyperparameter)란? (모델의 설정값).
- Grid Search: 가능한 모든 조합을 다 시도해 보기 (완전 탐색).
