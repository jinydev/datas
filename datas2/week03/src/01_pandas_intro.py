# 01_pandas_intro.py
import pandas as pd

# 6. 데이터프레임 만들기 (Dictionary 방식)
# 실무에서는 파일을 읽어오지만, 학습용으로 직접 만들어봅니다.
data = {
    '이름': ['김철수', '이영희', '박민수', '최지우', '정우성'],
    '나이': [25, 30, 22, 28, 45],
    '직업': ['학생', '회사원', '학생', '디자이너', '배우'],
    '점수': [80, 95, 70, 85, 99]
}

# DataFrame 객체 생성
df = pd.DataFrame(data)

# 9. 데이터 확인하기: head()
print("=== 상위 3개 데이터 ===")
print(df.head(3))

# 11. 요약 정보 확인: info()
print("\n=== 데이터 정보 (Info) ===")
# info()는 None을 반환하고 출력은 바로 stdout으로 나옵니다.
df.info() 

# 12. 통계적 요약: describe()
print("\n=== 통계 요약 (Describe) ===")
# 숫자형 컬럼(나이, 점수)에 대해서만 통계가 계산됩니다.
print(df.describe())

# 13. 열 선택 (Series 추출)
print("\n=== '이름' 열만 선택 ===")
names = df['이름']
print(names)
print(f"변환된 타입: {type(names)}") # pandas.core.series.Series

# 18. 파일 저장하기
# 한글이 포함되어 있으므로 encoding='utf-8-sig' 권장
df.to_csv('example_data.csv', index=False, encoding='utf-8-sig')
print("\n'example_data.csv' 파일이 저장되었습니다.")
