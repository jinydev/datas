# 02_regression_lab.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import r2_score

# 1. 데이터 준비 (농어 데이터)
# 길이, 높이, 두께
df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy()
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

# 3. 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(perch_full, perch_weight, random_state=42)

# 7. 특성 공학 (다항 특성 만들기)
poly = PolynomialFeatures(degree=5, include_bias=False) # 5차항까지 생성
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
print(f"변환된 특성 개수: {X_train_poly.shape[1]}") # 55개

# 8. 정규화 (규제 적용 전 필수)
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)

# 4. 선형 회귀 (규제 없음)
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
print(f"\n[Linear] Train: {lr.score(X_train_scaled, y_train):.4f}")
print(f"[Linear] Test: {lr.score(X_test_scaled, y_test):.4f}")
# 특성이 너무 많아서 훈련 점수는 높은데 테스트 점수는 엉망임 (심각한 과대적합)

# 9. 릿지 회귀 (L2 규제)
ridge = Ridge(alpha=0.1)
ridge.fit(X_train_scaled, y_train)
print(f"\n[Ridge] Train: {ridge.score(X_train_scaled, y_train):.4f}")
print(f"[Ridge] Test: {ridge.score(X_test_scaled, y_test):.4f}")
# 과대적합이 해소됨

# 10. 라쏘 회귀 (L1 규제)
lasso = Lasso(alpha=10)
lasso.fit(X_train_scaled, y_train)
print(f"\n[Lasso] Train: {lasso.score(X_train_scaled, y_train):.4f}")
print(f"[Lasso] Test: {lasso.score(X_test_scaled, y_test):.4f}")
print(f"라쏘가 사용한 특성 개수: {np.sum(lasso.coef_ != 0)}") # 55개 중 몇 개만 사용했는지 확인

# 11. alpha값 튜닝 시각화
train_score = []
test_score = []
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]

for alpha in alpha_list:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train_scaled, y_train)
    train_score.append(ridge.score(X_train_scaled, y_train))
    test_score.append(ridge.score(X_test_scaled, y_test))

plt.figure(figsize=(8, 6))
plt.plot(np.log10(alpha_list), train_score, label='Train')
plt.plot(np.log10(alpha_list), test_score, label='Test')
plt.xlabel('log10(alpha)')
plt.ylabel('R^2 Score')
plt.title("Hyperparameter Tuning (Ridge)")
plt.legend()
plt.show()
