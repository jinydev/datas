# 01_final_project_template.py
# 파이널 프로젝트 템플릿 코드
# 이 구조를 바탕으로 내용을 채워나가세요.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ==========================================
# 1. 데이터 로드
# ==========================================
DATA_PATH = 'data/my_dataset.csv' # 경로 수정 필요
print(f"Loading data from {DATA_PATH}...")
# df = pd.read_csv(DATA_PATH)
# 데모용 데이터 생성
df = pd.DataFrame({
    'age': np.random.randint(20, 60, 100),
    'salary': np.random.randint(3000, 8000, 100),
    'gender': np.random.choice(['M', 'F'], 100),
    'purchased': np.random.randint(0, 2, 100)
})

# ==========================================
# 2. EDA (탐색적 데이터 분석)
# ==========================================
print("\n=== 데이터 정보 ===")
print(df.info())
print("\n=== 기술 통계 ===")
print(df.describe())

# 시각화 예시
plt.figure(figsize=(6, 4))
sns.countplot(x='purchased', data=df)
plt.title('Target Distribution')
plt.show()

# ==========================================
# 3. 데이터 전처리 파이프라인
# ==========================================
X = df.drop('purchased', axis=1)
y = df['purchased']

# 수치형 변수와 범주형 변수 구분
numeric_features = ['age', 'salary']
categorical_features = ['gender']

# 수치형 변수 처리 (결측치 채우기 -> 스케일링)
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 범주형 변수 처리 (결측치 채우기 -> 원-핫 인코딩)
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 전처리기 통합
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# ==========================================
# 4. 모델 학습 파이프라인
# ==========================================
# 전처리 후 랜덤 포레스트 분류기 연결
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', RandomForestClassifier())])

# 학습/테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 5. 학습 및 하이퍼파라미터 튜닝
# ==========================================
print("\nTraining and Tuning...")
param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [None, 10, 20],
}

grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"최적 파라미터: {grid_search.best_params_}")
print(f"최고 교차 검증 점수: {grid_search.best_score_:.4f}")

# ==========================================
# 6. 최종 평가
# ==========================================
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

# 혼동 행렬 시각화
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
