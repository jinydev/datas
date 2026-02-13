import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 1. Barplot (평균 비교)
# 성별(sex)에 따른 생존율(survived) 평균
plt.figure(figsize=(6, 4))
sns.barplot(data=titanic, x='sex', y='survived')
plt.title("Survival Rate by Sex")
plt.ylabel("Survival Rate")
plt.show()

# 2. Countplot (개수 비교)
# 객실 등급(class)별 승객 수
plt.figure(figsize=(6, 4))
sns.countplot(data=titanic, x='class', palette='Set3')
plt.title("Passenger Count by Class")
plt.ylabel("Count")
plt.show()

# 3. [응용] 객실 등급별 생존율 (Barplot + Hue)
# 등급별로 나누고, 그 안에서 또 성별로 나누기
plt.figure(figsize=(8, 5))
sns.barplot(data=titanic, x='class', y='survived', hue='sex')
plt.title("Survival Rate by Class and Sex")
plt.show()
