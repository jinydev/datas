# 04_titanic_modeling_lab.py
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# 1. 데이터 준비
df = sns.load_dataset('titanic')
X = df.drop('survived', axis=1)
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. 전처리 파이프라인
numeric_features = ['age', 'fare', 'sibsp', 'parch']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_features = ['embarked', 'sex', 'pclass']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# 3. 모델 파이프라인 (Random Forest)
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 6. 교차 검증 (베이스라인 점수 확인)
cv_scores = cross_val_score(model_pipeline, X_train, y_train, cv=5)
print(f"Base Random Forest CV Score: {cv_scores.mean():.4f}")

# 7. 그리드 서치 (하이퍼파라미터 튜닝)
param_grid = {
    'classifier__n_estimators': [50, 100, 200], # 나무 개수
    'classifier__max_depth': [3, 5, 10, None],  # 나무 깊이
    'classifier__min_samples_split': [2, 5]
}

print("최적의 하이퍼파라미터를 찾는 중...")
grid_search = GridSearchCV(model_pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

print(f"\n최적 파라미터: {grid_search.best_params_}")
print(f"최고 CV 점수: {grid_search.best_score_:.4f}")

# 11. 최종 모델 평가
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test, y_test)
print(f"\n테스트 세트 정확도: {test_score:.4f}")

# 15. 피처 중요도 추출 (전처리된 컬럼명 매핑 필요)
# 파이프라인 내부 접근이 까다롭지만 시도해봅니다.
rf_model = best_model.named_steps['classifier']
feature_importances = rf_model.feature_importances_
print(f"\nTop 3 Feature Importance: {sorted(feature_importances, reverse=True)[:3]}") 
# (정확한 매핑은 복잡하므로 값만 확인)
