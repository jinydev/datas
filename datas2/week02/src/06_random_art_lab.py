# 06_random_art_lab.py
import matplotlib.pyplot as plt
import random

# 18. 함수화: 랜덤 워크 생성기
def generate_random_walk(steps):
    """
    0에서 시작하여 steps만큼 랜덤하게 위(+1) 또는 아래(-1)로 이동하는 
    궤적 리스트를 반환합니다.
    """
    y = [0] # 5. 초기화
    for _ in range(steps): # 6. 루프
        # 7. 스텝 결정 (-1 또는 1)
        step = 1 if random.random() > 0.5 else -1
        
        # 8. 누적 계산 (현재 마지막 값 + 스텝)
        next_val = y[-1] + step
        
        # 9. 기록
        y.append(next_val)
    return y

# 1. 캔버스 설정
plt.figure(figsize=(10, 6))

# 11. 다중 워커 시뮬레이션 (10명의 워커)
walker_count = 10
total_steps = 1000

colors = plt.cm.viridis(range(0, 256, 25)) # 컬러맵에서 색 추출

for i in range(walker_count):
    # 궤적 생성
    path = generate_random_walk(total_steps)
    
    # 10. 시각화 & 12. 스타일링
    # 끝점 강조를 위해 마크 추가
    plt.plot(path, alpha=0.6, linewidth=1, label=f'Walker {i+1}')
    plt.plot(len(path)-1, path[-1], marker='o', color='black', alpha=0.5)

# 17. 문맥 추가
plt.title(f"Random Walk Simulation ({walker_count} Walkers)", fontsize=16)
plt.xlabel("Time (Steps)")
plt.ylabel("Position")
plt.axhline(0, color='red', linestyle='--', linewidth=2, label='Start Line') # 시작선
plt.legend(loc='upper left', fontsize='small', ncol=2)
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()

# 15. 추가 실험: 2D 랜덤 워크 (보너스)
print("2D 랜덤 워크를 생성합니다...")
x_path = generate_random_walk(500)
y_path = generate_random_walk(500)

plt.figure(figsize=(6, 6))
plt.plot(x_path, y_path, color='purple', alpha=0.7)
plt.scatter(0, 0, color='red', s=100, label='Origin') # 시작점
plt.scatter(x_path[-1], y_path[-1], color='blue', s=100, label='End') # 끝점
plt.title("2D Motion Trace")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
