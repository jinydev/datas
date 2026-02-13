import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# [실기 문제 1] 막대 그래프
classes = ['A', 'B', 'C']
scores = [80, 75, 90]

plt.figure(figsize=(5, 3))
plt.bar(classes, scores, color='skyblue')
plt.title("Math Average")
plt.ylim(0, 100)
plt.show()

# [실기 문제 2] 필터링 (Numpy 활용)
nums = np.array([2, 5, 8, 12, 15, 18, 7])
# 조건: 짝수(nums % 2 == 0) AND(&) 10보다 큼(nums > 10)
result = nums[(nums % 2 == 0) & (nums > 10)]
print("문제 2 정답:", result)

# [실기 문제 3] 데이터프레임 조작
data = {
    'Name': ['Kim', 'Lee', 'Park', 'Choi'],
    'Age': [18, 22, 20, 15]
}
df = pd.DataFrame(data)

# Age >= 20 인 사람의 Name 열만
adults = df.loc[df['Age'] >= 20, 'Name']
print("문제 3 정답:\n", adults)
