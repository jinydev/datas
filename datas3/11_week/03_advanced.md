# 11주차 3강: 얼마나 잘 맞췄을까? (Evaluation)

모델이 얼마나 똑똑한지 점수를 매겨봅시다. 회귀 모델(숫자 예측)의 평가지표는 다음과 같습니다.

## 11.3.1. MSE, RMSE, R2 Score

1.  **MSE (Mean Squared Error)**: 오차(정답 - 예측값)를 제곱해서 평균 낸 것. 작을수록 좋습니다.
2.  **RMSE (Root MSE)**: MSE에 루트를 씌운 것. 실제 오차 단위와 비슷해서 이해하기 쉽습니다.
3.  **R2 Score (결정 계수)**: 0 ~ 1 사이의 값. 1에 가까울수록 완벽하게 예측했다는 뜻입니다. (예: 0.9 = 90% 정확도 느낌)

```python
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 테스트 데이터에 대한 예측
y_pred = model.predict(X_test)

# 평가 수행
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse) # RMSE
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R2 Score: {r2}")
```

## 11.3.2. 과대적합 vs 과소적합 (Bias-Variance Tradeoff)

- **과대적합 (Overfitting)**: 모의고사(Train)는 100점인데 수능(Test)은 50점. (암기식 공부의 폐해)
- **과소적합 (Underfitting)**: 공부를 너무 안 해서 모의고사도, 수능도 둘 다 못 봄. (공부 부족)

> **목표**: "일반화(Generalization)"가 잘 된, 즉 처음 보는 문제(Test)도 잘 푸는 모델을 만드는 것입니다.
