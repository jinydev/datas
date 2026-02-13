import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
print(penguins.head())

# 미션 1: Pairplot으로 관계 파악
# Gentoo 펭귄이 파란색으로 표시될텐데, 다른 펭귄보다 덩치(몸무게, 날개)가 큰 것을 볼 수 있습니다.
sns.pairplot(penguins, hue='species')
plt.show()

# 미션 2: 섬 별 펭귄 서식 확인 (Countplot)
plt.figure(figsize=(6, 4))
sns.countplot(data=penguins, x='island', hue='species')
plt.title("Penguin Species by Island")
plt.show()

# 미션 3: 종류별 몸무게 분포 (Boxplot)
plt.figure(figsize=(6, 4))
sns.boxplot(data=penguins, x='species', y='body_mass_g')
plt.title("Body Mass Distribution by Species")
plt.show()

# 추가 분석: 부리 길이 vs 깊이
# 종별로 확실하게 구분되는 특징이 있습니다.
plt.figure(figsize=(6, 4))
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.title("Bill Length vs Depth")
plt.show()
