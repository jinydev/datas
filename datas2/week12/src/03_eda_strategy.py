import seaborn as sns
import pandas as pd

# 펭귄 데이터 로드
df = sns.load_dataset('penguins')

def simple_eda(dataframe):
    print("=== 1. 데이터 크기 (Shape) ===")
    print(dataframe.shape)
    
    print("\n=== 2. 결측치 확인 (NaN Count) ===")
    print(dataframe.isnull().sum())
    
    print("\n=== 3. 기초 통계 (Describe) ===")
    print(dataframe.describe())
    
    print("\n=== 4. 데이터 샘플 (Head) ===")
    print(dataframe.head(3))

# 함수 실행
simple_eda(df)
