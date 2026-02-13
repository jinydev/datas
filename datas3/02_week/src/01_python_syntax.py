# 2주차 1강: 파이썬 기초 문법 정복하기
# 파일명: 01_python_syntax.py

# 1. 리스트와 딕셔너리 고급 기능
items = ["포션", "검"]
items.append("방패")  # 아이템 추가
items.remove("검")    # 아이템 삭제 (검을 잃어버렸다!)
print(f"현재 아이템: {items}")

profile = {"name": "Antigravity", "level": 99}
print(f"속성 목록: {list(profile.keys())}")
print(f"값 목록: {list(profile.values())}")

# 2. 제어문 (if-elif-else)
score = 85

if score >= 90:
    print("등급: A (전설)")
elif score >= 80:
    print("등급: B (영웅)")
elif score >= 70:
    print("등급: C (희귀)")
else:
    print("등급: D (일반)")

# 3. 반복문 (for range)
# 1부터 5까지 반복
for i in range(1, 6):
    print(f"{i}번째 몬스터 처치!")

# 4. 함수 (Function with Return)
def calculate_damage(base_damage, buff):
    total = base_damage * buff
    return total

my_damage = calculate_damage(100, 1.5)
print(f"최종 데미지: {my_damage}")
