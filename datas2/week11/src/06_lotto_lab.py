import numpy as np

# 1. 로또 번호 생성 함수
def generate_lotto():
    return np.random.choice(range(1, 46), size=6, replace=False)

# 내 번호 (정렬해둠)
my_nums = np.sort([1, 10, 23, 30, 35, 40])
print(f"내 번호: {my_nums}")

# 2. 당첨 시뮬레이션 (10만장 사보기)
try_count = 100000
prizes = {3: 0, 4: 0, 5: 0, 6: 0} # 5등(3개), 4등(4개), 3등(5개), 1등(6개)

print(f"=== {try_count}장 구매 시작! ===")

for i in range(try_count):
    # 번호 뽑기
    lucky_nums = np.sort(generate_lotto())
    
    # 맞춘 개수 세기 (교집합)
    matched = np.intersect1d(my_nums, lucky_nums)
    count = len(matched)
    
    if count >= 3:
        prizes[count] += 1

print("=== 결과 집계 ===")
print(f"5등 (3개 일치): {prizes[3]}번 (당첨금 5천원)")
print(f"4등 (4개 일치): {prizes[4]}번 (당첨금 5만원)")
print(f"3등 (5개 일치): {prizes[5]}번 (당첨금 150만원)")
print(f"1등 (6개 일치): {prizes[6]}번 (당첨금 20억)")

cost = try_count * 1000
earn = (prizes[3]*5000) + (prizes[4]*50000) + (prizes[5]*1500000) + (prizes[6]*2000000000)
print(f"\n쓴 돈: {cost:,}원")
print(f"번 돈: {earn:,}원")
print(f"수익률: {(earn-cost)/cost*100:.2f}%")
