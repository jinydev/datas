import numpy as np

# 1. 여러가지 랜덤
print("=== 랜덤 실수 (0~1) ===")
print(np.random.rand(3))

print("\n=== 랜덤 정수 (1~10) ===")
print(np.random.randint(1, 11, size=5)) # 5개 뽑기

# 2. [응용 예제] 메뉴 추천기
menus = ['짜장면', '김치찌개', '돈까스', '초밥', '햄버거']

# 확률 조정 (가중치) - 햄버거를 좋아해서 확률을 높임
probs = [0.1, 0.2, 0.1, 0.1, 0.5] 

today_menu = np.random.choice(menus, p=probs)
print(f"\n오늘의 추천 메뉴: {today_menu}")
