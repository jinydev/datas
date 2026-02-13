# 04_titanic_prep_lab.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 1. 데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

# 2. 초기 전처리 (함수화)
def feature_engineering(df):
    # Title 추출
    df['Title'] = df['sex'] # 임시 (실제로는 정규표현식 써야 함)
    # Family Size
    df['FamilySize'] = df['sibsp'] + df['parch'] + 1
    # IsSolo
    df['IsSolo'] = (df['FamilySize'] == 1).astype(int)
    return df

df = feature_engineering(df)

# features와 target 분리
X = df.drop('survived', axis=1)
y = df['survived']

# 학습/테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. 수치형 변수 파이프라인
numeric_features = ['age', 'fare', 'FamilySize']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 8. 범주형 변수 파이프라인
categorical_features = ['embarked', 'sex', 'pclass', 'IsSolo']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# 9. Preprocessor 합치기 (ColumnTransformer)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# 10. 전체 파이프라인 실행
# fit은 X_train 만으로!
print("전처리를 시작합니다...")
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print(f"변환된 데이터 형태(Shape): {X_train_processed.shape}")
# 원-핫 인코딩으로 인해 컬럼 수가 늘어남

# 12. 컬럼명 복원 (시각적 확인용)
# OneHotEncoder가 만든 컬럼명 가져오기
ohe_feature_names = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical_features)
new_columns = numeric_features + list(ohe_feature_names)

X_train_df = pd.DataFrame(X_train_processed, columns=new_columns)
print("\n=== 전처리 완료된 데이터 (상위 5개) ===")
print(X_train_df.head())

# 14. 저장
X_train_df.to_csv('titanic_train_prep.csv', index=False)
print("전처리된 데이터가 저장되었습니다.")
