# 01. 머신러닝의 세계로 (개념과 분류)

## 1. 머신러닝(Machine Learning)이란?
"데이터를 통해 컴퓨터가 스스로 학습하게 하는 기술"입니다.
전통적인 프로그래밍은 규칙(Rule)을 입력하면 정답을 내놓지만, 머신러닝은 데이터(Data)와 정답(Answer)을 주면 규칙(Rule)을 찾아냅니다.

## 2. 지도 학습 (Supervised Learning)
정답지(Label)가 있는 데이터를 학습합니다.
*   **분류(Classification)**: 생존/사망, 스팸/정상 메일처럼 범주를 예측.
*   **회귀(Regression)**: 집값, 주식 가격처럼 연속적인 숫자를 예측.

## 3. 비지도 학습 (Unsupervised Learning)
정답지 없이 데이터의 패턴을 찾습니다.
*   **군집화(Clustering)**: 비슷한 고객끼리 그룹 묶기.
*   **차원 축소(Dimensionality Reduction)**: 데이터의 복잡도 줄이기.

## 4. 강화 학습 (Reinforcement Learning)
시행착오를 통해 보상(Reward)을 최대화하는 행동을 학습합니다. (예: 알파고, 자율주행)

## 5. 사이킷런(Scikit-Learn)의 워크플로우
1.  **데이터 준비**: $X$ (Features)와 $y$ (Target) 분리.
2.  **모델 선택**: `from sklearn.tree import DecisionTreeClassifier`
3.  **학습(Training)**: `model.fit(X_train, y_train)`
4.  **예측(Prediction)**: `model.predict(X_test)`
5.  **평가(Evaluation)**: `accuracy_score(y_test, y_pred)`

## 6. 과대적합(Overfitting)과 과소적합(Underfitting)
*   **과대적합**: 모델이 훈련 데이터를 너무 달달 외워서, 새로운 데이터에는 엉망인 상태. (응용력 부족)
*   **과소적합**: 모델이 너무 단순해서 학습조차 제대로 안 된 상태. (공부 부족)

## 7. 훈련(Train) 세트와 테스트(Test) 세트
수능(Test)을 보기 전에 모의고사(Train)로 공부해야 합니다. 수능 문제까지 미리 보고 공부하면(Data Leakage) 100점은 맞겠지만 실력이 아닙니다.
`train_test_split`으로 데이터를 8:2 또는 7:3으로 나눕니다.

## 8. K-최근접 이웃 (KNN: K-Nearest Neighbors)
가장 직관적인 알고리즘입니다. "유유상종".
새로운 데이터가 들어오면 가장 가까운 $k$개의 이웃을 보고 다수결로 판정합니다.
스케일링이 필수적입니다.

## 9. 로지스틱 회귀 (Logistic Regression)
이름은 회귀지만 실제로는 **분류** 알고리즘입니다.
활성화 함수(Sigmoid)를 이용해 확률(0~1)을 출력하고, 임계값(0.5)을 기준으로 0 또는 1로 분류합니다. 선형 적인 경계선을 가집니다.

## 10. 서포트 벡터 머신 (SVM)
데이터를 갈라놓는 가장 넓은 도로(Margin)를 찾는 알고리즘입니다. 데이터가 적을 때 강력합니다.

## 11. 의사결정나무 (Decision Tree)
스무고개와 같습니다. "남자인가? (Yes/No)" -> "나이가 10세 이하인가? (Yes/No)" 식으로 질문을 이어가며 분류합니다. 설명력(Interpretability)이 가장 좋습니다.

## 12. 앙상블 (Ensemble)
여러 명의 바보(약한 모델)가 모여 천재(강한 모델)를 이깁니다.
*   **배깅(Bagging)**: 랜덤 포레스트가 대표적.
*   **부스팅(Boosting)**: XGBoost, LightGBM이 대표적.

## 13. 하이퍼파라미터 (Hyperparameter)
모델이 스스로 학습하지 못해서 사람이 직접 설정해줘야 하는 설정값입니다.
KNN의 $k$, 트리의 최대 깊이(max_depth) 등이 있습니다.

## 14. 실습: 붓꽃(Iris) 데이터 분류
머신러닝의 "Hello World"인 붓꽃 데이터를 로드하고, 품종을 분류하는 간단한 모델을 만들어 봅니다.

## 15. 모델 저장과 불러오기 (`joblib`)
학습된 모델은 파일(`.pkl`)로 저장했다가 나중에 다시 로드해서 쓸 수 있습니다. 웹 서비스나 앱에 탑재할 때 필요합니다.

## 16. 시드 고정 (`random_state`)
머신러닝에는 무작위성(데이터 섞기, 초기 가중치 등)이 많이 개입됩니다. 실험의 재현성을 위해 `random_state=42`처럼 시드를 고정해야 합니다.

## 17. 피처 중요도 (Feature Importance)
어떤 변수가 예측에 가장 큰 영향을 미쳤는지 모델에게 물어볼 수 있습니다. `model.feature_importances_`.

## 18. Python 문법 집중: 클래스 인스턴스
`model = DecisionTreeClassifier()`
붕어빵 틀(클래스)에서 붕어빵(인스턴스)을 찍어내야 학습을 시킬 수 있습니다.

## 19. 혼동 행렬 (Confusion Matrix) 맛보기
맞춘 건지 틀린 건지, 어떻게 틀렸는지 표로 확인하는 방법입니다. 다음 시간에 자세히 배웁니다.

## 20. 결론
머신러닝은 마법이 아니라 수학과 통계의 결합입니다. 오늘 배운 워크플로우(준비-선택-학습-평가)는 앞으로 배울 모든 딥러닝까지 통용되는 공식입니다.
