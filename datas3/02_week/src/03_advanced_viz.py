# 2주차 3강: 그래프 스타일링 (한글 폰트 & 저장)
# 파일명: 03_advanced_viz.py

import matplotlib.pyplot as plt
import platform

# 1. 한글 폰트 설정
system_name = platform.system()
if system_name == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
elif system_name == 'Windows': # Windows
    plt.rc('font', family='Malgun Gothic')
else: # Linux/Colab (NanumGothic 설치 필요)
    # Colab에서는 별도의 폰트 설치 과정이 필요합니다.
    print("Colab이나 Linux 환경에서는 나눔고딕 폰트 설치가 필요합니다.")

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 2. 데이터 준비
level = [1, 2, 3, 4, 5]
hero_hp = [100, 120, 150, 190, 240]    # 용사 체력
monster_hp = [80, 130, 200, 300, 450]  # 몬스터 체력

# 3. 그래프 그리기
plt.figure(figsize=(10, 6))

plt.plot(level, hero_hp, label='용사(Hero)', color='blue', marker='o', linestyle='-')
plt.plot(level, monster_hp, label='몬스터(Monster)', color='red', marker='x', linestyle='--')

# 4. 꾸미기
plt.title("레벨별 체력 변화 (용사 vs 몬스터)", fontsize=16)
plt.xlabel("레벨 (Level)", fontsize=12)
plt.ylabel("체력 (HP)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)

# 5. 저장하기 (Save)
# 반드시 show() 전에 호출해야 합니다.
plt.savefig('hero_vs_monster.png', dpi=300)
print("그래프가 'hero_vs_monster.png'로 저장되었습니다.")

plt.show()
