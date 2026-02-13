import random

options = ['가위', '바위', '보']
win_count = 0
lose_count = 0

print("=== 가위바위보 게임 (3판 2선승) ===")

while win_count < 2 and lose_count < 2:
    user = input("가위/바위/보 중 하나 입력: ")
    computer = random.choice(options)
    
    if user not in options:
        print("잘못 입력했습니다.")
        continue
        
    print(f"컴퓨터: {computer}")
    
    if user == computer:
        print("비겼습니다!")
    elif (user == '가위' and computer == '보') or \
         (user == '바위' and computer == '가위') or \
         (user == '보' and computer == '바위'):
        print("이겼습니다!")
        win_count += 1
    else:
        print("졌습니다 ㅠㅠ")
        lose_count += 1

print(f"결과: {win_count}승 {lose_count}패")
if win_count == 2:
    print("축하합니다! 최종 승리!")
else:
    print("아쉽네요. 다음 기회에...")
