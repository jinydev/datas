import random
import matplotlib.pyplot as plt

# 1. 동전 던지기 함수
def flip_coin(n):
    heads = 0
    tails = 0
    for i in range(n):
        if random.random() < 0.5: # 0.5보다 작으면 앞면이라고 가정
            heads += 1
        else:
            tails += 1
    return heads, tails

# 2. 실행
try_count = 100
h, t = flip_coin(try_count)

print(f"{try_count}번 던진 결과:")
print(f"앞면: {h}번 ({h/try_count*100}%)")
print(f"뒷면: {t}번 ({t/try_count*100}%)")

# 3. 시각화
plt.figure(figsize=(5, 5))
plt.pie([h, t], labels=['Heads', 'Tails'], autopct='%.1f%%', colors=['gold', 'silver'])
plt.title("Coin Flip Result")
plt.show()
