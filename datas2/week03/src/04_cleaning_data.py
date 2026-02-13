# 04_cleaning_data.py
import pandas as pd
import numpy as np

# 결측치가 포함된 샘플 데이터 생성
data = {
    '이름': ['김철수', '이영희', np.nan, '최지우', '김철수'], # 이름 누락, 중복 존재
    '나이': [25, np.nan, 22, 28, 25], # 나이 누락, 중복 존재
    '점수': [80, 95, 70, np.nan, 80]  # 점수 누락, 중복 존재
}
df = pd.DataFrame(data)

print("=== 원본 데이터 (결측/중복 포함) ===")
print(df)

# 4. 결측치 확인
print("\n=== 컬럼별 결측치 개수 ===")
print(df.isnull().sum())

# 9. 결측치 채우기 (나이는 평균으)
mean_age = df['나이'].mean()
print(f"\n나이 평균: {mean_age}")

# 원본 보존을 위해 copy
df_filled = df.copy()
df_filled['나이'] = df_filled['나이'].fillna(mean_age)

# 점수는 0점으로 채우기
df_filled['점수'] = df_filled['점수'].fillna(0)

# 이름이 없는 행은 삭제 (식별 불가하므로)
# subset=['이름']을 지정하여 이름이 NaN인 행만 삭제
df_final = df_filled.dropna(subset=['이름'])

print("\n=== 결측치 처리 후 ===")
print(df_final)

# 12. 중복 데이터 확인
print("\n=== 중복된 행 개수 ===")
print(df_final.duplicated().sum())

# 13. 중복 제거
df_clean = df_final.drop_duplicates()
print("\n=== 최종 정제된 데이터 ===")
print(df_clean)
