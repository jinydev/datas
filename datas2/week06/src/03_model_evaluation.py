# 03_model_evaluation.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, 
                             confusion_matrix, classification_report, roc_curve, roc_auc_score)

# 데이터 준비
df = sns.load_dataset('titanic')
df = df.dropna(subset=['age', 'embarked'])
df['sex_code'] = df['sex'].map({'female': 1, 'male': 0})
X = df[['pclass', 'sex_code', 'age', 'fare']]
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_test)
pred_proba = model.predict_proba(X_test)[:, 1] # 1(생존)일 확률

# 2. 오차 행렬 (Confusion Matrix)
print("=== 오차 행렬 ===")
cm = confusion_matrix(y_test, pred)
print(cm)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# 3, 4, 6. 평가지표 상세
print("\n=== 상세 평가 지표 ===")
print(f"정확도 (Accuracy): {accuracy_score(y_test, pred):.4f}")
print(f"정밀도 (Precision): {precision_score(y_test, pred):.4f}")
print(f"재현율 (Recall): {recall_score(y_test, pred):.4f}")
print(f"F1 Score: {f1_score(y_test, pred):.4f}")

# 19. 분류 리포트
print("\n=== Classification Report ===")
print(classification_report(y_test, pred))

# 7. ROC 곡선
fpr, tpr, thresholds = roc_curve(y_test, pred_proba)
auc_score = roc_auc_score(y_test, pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc_score:.4f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random Guess')
plt.xlabel('False Positive Rate (Set Normal as Cancer)')
plt.ylabel('True Positive Rate (Catch Cancer)')
plt.title('ROC Curve')
plt.legend()
plt.show()

# 11. 교차 검증 (Cross Validation)
print("\n=== 5-Fold Cross Validation ===")
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"교차 검증 점수들: {scores}")
print(f"평균 정확도: {scores.mean():.4f}")
