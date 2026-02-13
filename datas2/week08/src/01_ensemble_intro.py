# 01_ensemble_intro.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# 1. 와인 데이터 로드
# 0: Red, 1: White
wine = pd.read_csv('https://bit.ly/wine_csv_data')
X = wine.drop('class', axis=1)
y = wine['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. 개별 모델 정의
lr = LogisticRegression(max_iter=1000)
dt = DecisionTreeClassifier(random_state=42)

# 3. 투표 기반 앙상블 (Soft Voting)
voting = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='soft'
)
voting.fit(X_train, y_train)
pred_vote = voting.predict(X_test)
print(f"Voting Classifier Accuracy: {accuracy_score(y_test, pred_vote):.4f}")

# 4. 랜덤 포레스트 (배깅)
rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, X_train, y_train, return_train_score=True, n_jobs=-1)
print(f"\nRandom Forest Train Score: {np.mean(scores['train_score']):.4f}")
print(f"Random Forest Val Score: {np.mean(scores['test_score']):.4f}")

# OOB 점수 확인
rf.fit(X_train, y_train) # 재학습 필요 (oob_score_ 옵션을 켜야 함)
rf_oob = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
rf_oob.fit(X_train, y_train)
print(f"OOB Score: {rf_oob.oob_score_:.4f}")

# 5. 특성 중요도 (Random Forest)
print(f"\nRF Feature Importances: {rf_oob.feature_importances_}")
# [알코올, 당도, pH] 순서

# 6. 그래디언트 부스팅 (부스팅)
gb = GradientBoostingClassifier(random_state=42)
scores_gb = cross_validate(gb, X_train, y_train, return_train_score=True, n_jobs=-1)
print(f"\nGBM Val Score: {np.mean(scores_gb['test_score']):.4f}")

# 14. XGBoost 맛보기 (설치되어 있다고 가정)
try:
    from xgboost import XGBClassifier
    xgb = XGBClassifier(tree_method='hist', random_state=42)
    xgb.fit(X_train, y_train)
    print(f"\nXGBoost Accuracy: {xgb.score(X_test, y_test):.4f}")
except ImportError:
    print("\nXGBoost 라이브러리가 설치되지 않았습니다.")
