# 06_pokemon_lab.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. 가상의 포켓몬 데이터 생성
data = {
    'Name': ['Charizard', 'Blastoise', 'Venusaur', 'Mewtwo', 'Pikachu', 'Gengar', 'Dragonite'],
    'Type 1': ['Fire', 'Water', 'Grass', 'Psychic', 'Electric', 'Ghost', 'Dragon'],
    'Type 2': ['Flying', np.nan, 'Poison', np.nan, np.nan, 'Poison', 'Flying'],
    'Total': [534, 530, 525, 680, 320, 500, 600],
    'HP': [78, 79, 80, 106, 35, 60, 91],
    'Attack': [84, 83, 82, 110, 55, 65, 134],
    'Defense': [78, 100, 83, 90, 40, 60, 95],
    'Legendary': [False, False, False, True, False, False, False]
}
df = pd.DataFrame(data)

print("=== 데이터 개요 ===")
df.info()

# 4. 결측치 처리 (Type 2가 없으면 'None'으로)
df['Type 2'] = df['Type 2'].fillna('None')

# 5. 전설의 포켓몬 찾기
print("\n=== 전설의 포켓몬 ===")
legendary = df[df['Legendary'] == True]
print(legendary[['Name', 'Total']])

# 6. 공격력 Top 3
print("\n=== 공격력 Top 3 ===")
top_attack = df.sort_values(by='Attack', ascending=False).head(3)
print(top_attack[['Name', 'Attack']])

# 8. 그룹별 분석 (Type 1 별 평균 공격력)
print("\n=== 타입별 평균 공격력 ===")
type_avg = df.groupby('Type 1')['Attack'].mean()
print(type_avg)

# 10. 시각화
plt.figure(figsize=(8, 5))
type_avg.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Average Attack by Type")
plt.ylabel("Attack Point")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()

# 15. 데이터 저장
legendary.to_csv('legendary_list.csv', index=False)
print("\n전설의 포켓몬 리스트가 저장되었습니다.")
