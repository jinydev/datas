import pandas as pd

# 가상의 성적 데이터
data = {
    'Korean': [90, 80, 70, 60, 95],
    'English': [85, 90, 75, 50, 90],
    'Math': [100, 60, 50, 40, 95],
    'Music': [70, 70, 80, 90, 60]
}
df = pd.DataFrame(data)

# 1. 상관계수 행렬 계산
corr_matrix = df.corr()
print("=== 상관계수 행렬 ===")
print(corr_matrix)

# 2. 해석해보기
# Korean과 English의 관계는?
r_kor_eng = corr_matrix.loc['Korean', 'English']
print(f"\n국어와 영어의 상관계수: {r_kor_eng:.2f}")

# Korean과 Music의 관계는? (음수일 수도 있음)
r_kor_mus = corr_matrix.loc['Korean', 'Music']
print(f"국어와 음악의 상관계수: {r_kor_mus:.2f}") 
# 공부를 잘하면 음악 점수는 낮은 경향? (가상 데이터입니다)
