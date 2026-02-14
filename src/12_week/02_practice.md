---
layout: home
title: "12주차 2강: 시험 점수가 다가 아니다 (Performance Metrics)"
---

# 12주차 2강: 시험 점수가 다가 아니다 (Performance Metrics)

## 12.2.1. 정확도(Accuracy)의 함정

암 환자를 찾는 모델을 만들었습니다. 전체 환자의 99%는 정상이고, 1%만 암 환자입니다.
모델이 **"조건 없이 무조건 정상이라고 예측해!"**라고 한다면?
-> **정확도는 99%**가 나옵니다. 하지만 암 환자는 **단 한 명도 못 찾습니다**.
그래서 정확도만 믿으면 위험합니다.

## 12.2.2. 혼동 행렬 (Confusion Matrix)

예측 결과와 실제 정답을 네 가지 경우로 나눕니다.

| 실제 \ 예측 | Positive (암 환자 O) | Negative (암 환자 X) |
|:---:|:---:|:---:|
| **Positive (암 O)** | **TP** (진짜 잘 맞춤) | **FN** (놓침! 위험!) |
| **Negative (암 X)** | **FP** (오진! 생사람 잡음) | **TN** (정상 잘 맞춤) |

## 12.2.3. 정밀도, 재현율, F1-Score

1.  **정밀도 (Precision)**: 모델이 "암"이라고 한 것 중에 진짜 암 환자 비율. (오진 줄이기)
2.  **재현율 (Recall)**: 실제 암 환자 중에 모델이 찾은 비율. (놓친 환자 줄이기) -> **보통 이게 더 중요함!**
3.  **F1-Score**: 정밀도와 재현율의 조화 평균. (둘 다 적당히 중요할 때)

```python
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

print("정확도:", accuracy_score(y_test, y_pred))
print("재현율:", recall_score(y_test, y_pred))
print("정밀도:", precision_score(y_test, y_pred))
print("F1 점수:", f1_score(y_test, y_pred))
```
