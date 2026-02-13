# 04_for_loops.py
import matplotlib.pyplot as plt
import random

# 13. 응용 예제: 제너레이티브 아트 (100개의 선)
plt.figure(figsize=(6, 6))

# 2. for 반복문 활용
for i in range(50):
    # 랜덤 좌표 생성
    x1 = random.randint(0, 10)
    y1 = random.randint(0, 10)
    x2 = random.randint(0, 10)
    y2 = random.randint(0, 10)
    
    # 5. i 변수 활용 (색상 그라데이션)
    # i가 커질수록 붉은색 강도가 높아짐
    red_intensity = i / 50.0 
    
    # 선 그리기
    plt.plot([x1, x2], [y1, y2], color=(red_intensity, 0, 0.5), alpha=0.5)

plt.title("Generative Net Art")
plt.axis('off') # 예술적 느낌을 위해 축 숨김
plt.show()

# 7. 누적 패턴 (합계 구하기)
scores = [80, 90, 95, 70, 60]
total = 0

print("=== 합계 구하기 로직 ===")
for s in scores:
    print(f"{s} 점을 더합니다. (현재 누적: {total})")
    total += s # 8. 복합 대입 연산자

print(f"최종 합계: {total}")
print(f"평균 점수: {total / len(scores)}")
