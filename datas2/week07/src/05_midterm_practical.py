import time

print("시험을 시작합니다! (5초 타이머 예시)")

# 5초 카운트다운
for i in range(5, 0, -1):
    print(f"{i}초 남았습니다...")
    time.sleep(1) # 1초 대기

print("시험 종료! 펜을 놓으세요.")

# time 모듈 응용: 코드 실행 시간 측정
start_time = time.time()

# 무거운 작업 (예: 100만번 더하기)
sum_val = 0
for i in range(1000000):
    sum_val += i

end_time = time.time()
print(f"계산하는데 걸린 시간: {end_time - start_time:.4f}초")
