# 02_encoding.py
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 데이터 로드
df = sns.load_dataset('titanic')
# 실습용 데이터 추출
data = df[['sex', 'embarked', 'class']].dropna()

print("=== 원본 데이터 ===")
print(data.head())

# 2. 레이블 인코딩 (Label Encoding)
print("\n=== 레이블 인코딩 ===")
le = LabelEncoder()
encoded_sex = le.fit_transform(data['sex'])
print(f"변환된 클래스: {le.classes_}") # ['female' 'male'] -> 0, 1
# 데이터프레임에 적용
data_le = data.copy()
data_le['sex_encoded'] = encoded_sex
print(data_le.head())

# 5. Pandas Get Dummies (One-Hot)
print("\n=== Pandas Get Dummies ===")
# drop_first=True로 첫 번째 컬럼 제거 (다중공선성 방지)
data_dummies = pd.get_dummies(data, columns=['sex', 'embarked'], drop_first=True)
print(data_dummies.head())
# sex_male, embarked_Q, embarked_S 컬럼이 생성됨 (embarked_C는 제거됨)

# 6. Scikit-Lear OneHotEncoder
print("\n=== Sklearn OneHotEncoder (Sparse vs Dense) ===")
# 2차원 배열을 입력으로 받아야 함
ohe = OneHotEncoder(sparse=False) # sparse=False여야 눈으로 보이는 배열이 됨
encoded_embarked = ohe.fit_transform(data[['embarked']])
print(f"인코딩된 배열 형태: {encoded_embarked.shape}")
print(encoded_embarked[:5]) # 상위 5개 확인

# DataFrame으로 변환하여 합치기
embarked_df = pd.DataFrame(encoded_embarked, columns=ohe.get_feature_names_out(['embarked']))
# 인덱스 재설정이 필요할 수 있음 (concat시 인덱스 불일치 방지)
embarked_df.index = data.index

print(embarked_df.head())

# 9. 순서형 변수 수동 매핑 (Mapping)
print("\n=== 수동 매핑 (Class) ===")
class_map = {'First': 3, 'Second': 2, 'Third': 1} # 1등석의 가중치를 높게 줄지 낮게 줄지는 모델링 목적에 따라 다름
data['class_score'] = data['class'].map(class_map)
print(data[['class', 'class_score']].head())
