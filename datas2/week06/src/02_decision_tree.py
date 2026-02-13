# 02_decision_tree.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. 데이터 로드 및 간단 전처리
df = sns.load_dataset('titanic')
df = df.dropna(subset=['age', 'embarked']) # 결측치 제거
df['sex_code'] = df['sex'].map({'female': 1, 'male': 0})
df['embarked_code'] = df['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

X = df[['pclass', 'sex_code', 'age', 'sibsp', 'parch', 'fare']]
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. 모델 학습 (규제 적용)
# max_depth=3으로 제한하여 시각화했을 때 보기 좋게 만듦
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# 3. 평가
pred = model.predict(X_test)
print(f"훈련 세트 정확도: {model.score(X_train, y_train):.4f}")
print(f"테스트 세트 정확도: {accuracy_score(y_test, pred):.4f}")

# 4. 트리 시각화
plt.figure(figsize=(20, 10))
plot_tree(model, 
          feature_names=X.columns,  
          class_names=['Dead', 'Survived'],
          filled=True, rounded=True, fontsize=12)
plt.title("Titanic Decision Tree (Depth=3)")
plt.show()

# 5. 피처 중요도
import numpy as np
importances = model.feature_importances_
indices = np.argsort(importances)[::-1] # 내림차순 정렬

print("\n=== Feature Ranking ===")
for f in range(X.shape[1]):
    print(f"{f+1}. {X.columns[indices[f]]} ({importances[indices[f]]:.4f})")

# 6. 결정 경계 시각화 실험 (변수 2개만 사용)
# Age와 Fare만 사용하여 2차원 평면에서의 분할 확인
X_2d = X[['age', 'fare']]
y_2d = y

model_2d = DecisionTreeClassifier(max_depth=4)
model_2d.fit(X_2d, y_2d)

# 그리드 생성
x_min, x_max = X_2d['age'].min() - 1, X_2d['age'].max() + 1
y_min, y_max = X_2d['fare'].min() - 1, X_2d['fare'].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 1),
                     np.arange(y_min, y_max, 10)) # fare는 범위가 커서 단위를 10으로

Z = model_2d.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.4, cmap='RdBu')
plt.scatter(X_2d['age'], X_2d['fare'], c=y_2d, s=20, edgecolor='k', cmap='RdBu')
plt.title("Decision Boundary (Age vs Fare)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
