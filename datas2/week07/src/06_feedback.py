import pandas as pd
import matplotlib.pyplot as plt

# 가상의 시험 결과 데이터 (1: 정답, 0: 오답)
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Q1': [1, 1, 1, 0, 1],
    'Q2': [0, 1, 0, 0, 1], # 어려운 문제였나봄
    'Q3': [1, 1, 1, 1, 1]  # 쉬운 문제
}

df = pd.DataFrame(data)
print("=== 학생별 답안 ===")
print(df)

# 문제별 정답률 계산 (평균을 구하면 됨)
# Student 열은 문자니까 제외하고 계산
accuracy = df.drop('Student', axis=1).mean() * 100 
print("\n=== 문제별 정답률 (%) ===")
print(accuracy)

# 시각화
plt.figure(figsize=(5, 3))
plt.bar(accuracy.index, accuracy.values, color='lightgreen')
plt.axhline(50, color='red', linestyle='--', label='Warning (50%)')
plt.title("Question Accuracy")
plt.ylabel("Accuracy (%)")
plt.legend()
plt.show()
