# 01_ml_intro.py
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. 데이터 준비 (Iris)
# 붓꽃 데이터: 꽃잎/꽃받침의 길이/너비로 품종(Setosa, Versicolor, Virginica) 분류
iris = sns.load_dataset('iris')
print("=== Iris 데이터 확인 ===")
print(iris.head())

X = iris.drop('species', axis=1) # Features (꽃의 치수)
y = iris['species']              # Target (품종)

# 7. 훈련/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 모델 1: 의사결정나무 ---
print("\n=== 1. 의사결정나무 ===")
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train) # 학습
pred_tree = tree.predict(X_test) # 예측
print(f"정확도: {accuracy_score(y_test, pred_tree):.4f}")

# --- 모델 2: KNN (K-최근접 이웃) ---
print("\n=== 2. KNN (k=3) ===")
# 주의: KNN은 스케일링이 필요하지만 여기선 생략 (다음 챕터에서 다룸)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
pred_knn = knn.predict(X_test)
print(f"정확도: {accuracy_score(y_test, pred_knn):.4f}")

# --- 모델 3: 로지스틱 회귀 ---
print("\n=== 3. 로지스틱 회귀 ===")
# max_iter는 반복 횟수 제한 (수렴을 위해 늘려줌)
lr = LogisticRegression(max_iter=200) 
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)
print(f"정확도: {accuracy_score(y_test, pred_lr):.4f}")

# 17. 피처 중요도 확인 (트리 모델만 가능)
print("\n=== 트리의 피처 중요도 ===")
importance = pd.Series(tree.feature_importances_, index=X.columns)
print(importance.sort_values(ascending=False))
