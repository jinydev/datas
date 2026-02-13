# 01_env_setup.py
# 이 스크립트는 "01. 디지털 연구실 구축" 강의의 실습 코드입니다.

# 7. Python 문법 집중: print() 함수
# 화면에 텍스트를 출력합니다.
print("Hello, Data Science!")

# 11. print 내에서의 연산
# 함수 안에서 바로 계산이 가능합니다.
print(10 + 20)

# 12. 데이터 타입의 구분
# 문자열과 숫자의 차이를 확인해 보세요.
print("10 + 20") # 텍스트 그대로 출력
print(30)        # 계산된 숫자 출력

# 14. Python 문법 집중: import 문
import matplotlib.pyplot as plt

# 19. 응용 예제: 선형 추세 시각화
# 가장 기본적인 선 그래프를 그려봅니다.
# 수학적 해석: y = 10x (x는 0, 1, 2, 3으로 자동 지정됨)
data = [10, 20, 30, 40]

plt.figure(figsize=(6, 4))
plt.plot(data)
plt.title("My First Data Visualization")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
