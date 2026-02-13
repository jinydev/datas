# 간단한 퀴즈 프로그램
score = 0

print("=== 중간고사 대비 퀴즈 ===")

# 문제 1
answer1 = input("1. 빅데이터의 3V가 아닌 것은? (1: Volume, 2: Velocity, 3: Variety, 4: Vitamin) ")
if answer1 == "4":
    print("정답입니다! (+50점)")
    score += 50
else:
    print("틀렸습니다. 정답은 4번입니다.")

# 문제 2
answer2 = input("2. 판다스에서 빈 값을 의미하는 단어는? (대문자로) ")
if answer2.upper() == "NAN":
    print("정답입니다! (+50점)")
    score += 50
else:
    print("틀렸습니다. 정답은 NaN입니다.")

print(f"=== 최종 점수: {score}점 ===")
if score == 100:
    print("완벽합니다 준비 완료!")
else:
    print("조금 더 복습해봅시다.")
