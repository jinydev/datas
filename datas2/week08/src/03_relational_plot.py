import seaborn as sns
import matplotlib.pyplot as plt

# 1. 붓꽃 데이터 불러오기
iris = sns.load_dataset('iris')
print(iris.head())

# 2. 산점도 행렬 (Pairplot) 그리기
# hue='species'를 주면 품종별로 색깔을 다르게 칠해줍니다.
# 이 그래프 하나면 4가지 변수의 관계를 한 눈에 파악할 수 있습니다.
sns.pairplot(iris, hue='species', height=2.5)
plt.show()

# 3. 특정 두 변수만 자세히 보기
# 꽃잎의 길이(petal_length)와 너비(petal_width)의 관계
plt.figure(figsize=(6, 4))
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', s=100)
plt.title("Petal Length vs Width")
plt.show()
