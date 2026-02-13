# 01_regression_intro.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 생성 (키와 몸무게)
# 랜덤 시드 고정
np.random.seed(42)
# 키: 150 ~ 190 사이의 랜덤값 50개
height = 150 + np.random.rand(50) * 40
# 몸무게: 키 * 0.7 - 60 + 노이즈
weight = height * 0.7 - 60 + np.random.randn(50) * 2

# 2. 데이터 전처리 (Reshape)
X = height.reshape(-1, 1) # 2차원 배열로 변환 [[150.1], [162.3]...]
y = weight

# 3. 모델 생성 및 학습
lr = LinearRegression()
lr.fit(X, y)

# 4. 학습 결과 확인
w = lr.coef_[0]
b = lr.intercept_
print(f"회귀식: y = {w:.2f}x + {b:.2f}")
# 해석: 키가 1cm 클 때마다 몸무게는 w kg 늘어난다.

# 5. 예측 및 평가
y_pred = lr.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"MSE: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

# 6. 시각화
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Linear Model')
plt.title(f"Height vs Weight (R2={r2:.2f})")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.grid(True)
plt.show()

# 14. 다항 회귀 (곡선 데이터 실험)
print("\n=== 다항 회귀 실험 ===")
# 곡선 형태의 데이터 생성 (y = 0.5x^2 + ...)
X_poly = np.linspace(-3, 3, 100).reshape(-1, 1)
y_poly = 0.5 * X_poly**2 + X_poly + 2 + np.random.randn(100, 1)

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly_2 = poly.fit_transform(X_poly) # x -> [x, x^2]

lr_poly = LinearRegression()
lr_poly.fit(X_poly_2, y_poly)
y_poly_pred = lr_poly.predict(X_poly_2)

plt.figure(figsize=(8, 6))
plt.scatter(X_poly, y_poly, s=10, color='gray')
plt.plot(X_poly, y_poly_pred, 'r-', linewidth=2, label='Polynomial Model')
plt.title("Polynomial Regression (Degree=2)")
plt.show()
