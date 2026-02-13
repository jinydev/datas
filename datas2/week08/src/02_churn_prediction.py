# 02_churn_prediction.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

# 1. 데이터 준비 (Telco Customer Churn 샘플)
# 실제 파일이 없으므로 가상의 데이터 생성 로직으로 대체하거나 URL 사용
# 여기서는 편의상 colab sample_data 대신 와인 데이터 등으로 구조만 실습하거나, 
# 직접 생성합니다. 
# (실제 강의엔 kaggle URL 사용 권장: https://www.kaggle.com/blastchar/telco-customer-churn)

# 데모를 위해 붓꽃 데이터를 이진 분류(Churn/Not Churn) 상황으로 가정하고 진행
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target 
# 0: Malignant(악성) -> Churn(이탈)로 가정
# 1: Benign(양성) -> Stay(유지)로 가정
# 타겟을 1(이탈)로 맞추기 위해 반전 (Breast Cancer 데이터는 0이 악성)
y = 1 - y 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. 랜덤 포레스트 모델링
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 예측
y_pred = rf.predict(X_test)
y_proba = rf.predict_proba(X_test)[:, 1]

# 9. 평가
print("=== 분류 리포트 ===")
print(classification_report(y_test, y_pred))
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.4f}")

# 10. 피처 중요도 시각화
importances = pd.Series(rf.feature_importances_, index=X.columns)
top_20 = importances.sort_values(ascending=False)[:20]

plt.figure(figsize=(10, 8))
sns.barplot(x=top_20.values, y=top_20.index, palette='viridis')
plt.title('Top 20 Feature Imnportances (Churn Factors)')
plt.show()

# 12. 이탈 고위험군 추출
result_df = X_test.copy()
result_df['Churn_Prob'] = y_proba
result_df['Real_Churn'] = y_test

# 위험도 상위 10명
high_risk = result_df.sort_values(by='Churn_Prob', ascending=False).head(10)
print("\n=== 이탈 위험도 Top 10 고객 ===")
print(high_risk[['Churn_Prob', 'Real_Churn']])
