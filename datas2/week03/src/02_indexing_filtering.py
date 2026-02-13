# 02_indexing_filtering.py
import pandas as pd

# 샘플 데이터 생성
data = {
    '이름': ['김철수', '이영희', '박민수', '최지우', '정우성'],
    '나이': [25, 30, 22, 28, 45],
    '직업': ['학생', '회사원', '학생', '디자이너', '배우'],
    '점수': [80, 95, 70, 85, 99]
}
df = pd.DataFrame(data)

print("=== 원본 데이터 ===")
print(df)

# 4. loc 인덱서 (이름으로 접근)
# 2번 인덱스(박민수)의 이름과 점수
print("\n=== loc[2, ['이름', '점수']] ===")
print(df.loc[2, ['이름', '점수']])

# 7. 불리언 인덱싱 (필터링)
# 점수가 80점 초과인 사람
print("\n=== 점수 > 80 필터링 ===")
high_score = df[df['점수'] > 80]
print(high_score)

# 10. 다중 조건 (AND)
# 점수가 80점 이상이면서 학생인 사람
cond = (df['점수'] >= 80) & (df['직업'] == '학생')
print("\n=== 점수 >= 80 AND 직업 == '학생' ===")
print(df[cond])

# 14. 문자열 필터링
# 이름에 '수'가 들어가는 사람
print("\n=== 이름에 '수'가 포함된 사람 ===")
print(df[df['이름'].str.contains('수')])

# 15. 정렬하기
# 나이 많은 순서대로(내림차순)
sorted_df = df.sort_values(by='나이', ascending=False)
print("\n=== 나이 내림차순 정렬 ===")
print(sorted_df)

# 16. 인덱스 리셋
# 정렬 후 인덱스가 4, 1, 3... 처럼 섞여있으므로 다시 0, 1, 2...로
print("\n=== 인덱스 리셋 후 ===")
print(sorted_df.reset_index(drop=True))
