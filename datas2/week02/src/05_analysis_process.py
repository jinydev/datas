# 05_analysis_process.py
import random
import matplotlib.pyplot as plt

# 9. Python 문법 집중: 함수
# 데이터 분석 파이프라인을 함수로 구현해 봅니다.

# 1단계: 수집
def get_sensor_data(n):
    """
    가상의 센서로부터 데이터를 수집하는 척을 하는 함수입니다.
    n개의 랜덤 정수(0~100)를 반환합니다.
    일부러 에러 데이터(-1)를 섞어서 보냅니다.
    """
    data = []
    for _ in range(n):
        # 10% 확률로 에러 발생 (-1)
        if random.random() < 0.1:
            data.append(-1)
        else:
            data.append(random.randint(0, 100))
    return data

# 2단계: 전처리
def clean_data(raw_data):
    """
    리스트에서 에러 값(-1)을 제거하여 깨끗한 데이터를 반환합니다.
    """
    clean = []
    for x in raw_data:
        if x != -1:
            clean.append(x)
    return clean

# 3단계: 시각화
def plot_data(data, title="Data"):
    plt.figure(figsize=(8, 4))
    plt.plot(data, marker='o', label='Sensor Value')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

# 18. 응용 예제: 파이프라인 실행
print("1. 데이터를 수집 중입니다...")
raw = get_sensor_data(50)
print(f"원본 데이터 샘플: {raw[:10]}")

print("\n2. 데이터를 정제 중입니다...")
processed = clean_data(raw)
print(f"정제된 데이터 샘플: {processed[:10]}")
print(f"(제거된 에러 데이터 개수: {len(raw) - len(processed)}개)")

print("\n3. 시각화 결과를 출력합니다...")
plot_data(processed, "Cleaned Sensor Stream")
