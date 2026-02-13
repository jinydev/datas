import pandas as pd
import io

# 가상의 CSV 데이터 (한글 포함)
csv_data = """
연도,지역,인구수
2023,서울,9500000
2023,부산,3300000
2023,대구,2400000
"""

# 파일이 있다고 가정하고 읽는 코드
# 실제로는: df = pd.read_csv('filename.csv', encoding='cp949')
try:
    df = pd.read_csv(io.StringIO(csv_data))
    print("=== 데이터 로드 성공 ===")
    print(df)
except Exception as e:
    print("파일 읽기 실패:", e)

print("\nTip: 한글이 깨진다면 pd.read_csv(..., encoding='cp949')를 시도해보세요!")
