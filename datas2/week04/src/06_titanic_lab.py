# 06_titanic_lab.py
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 11. 자동화 함수 작성 (전처리 파이프라인)
def preprocess_titanic(df):
    # 1. Deck 컬럼 삭제
    df = df.drop(['deck', 'embark_town'], axis=1)
    
    # 2. Embarked 최빈값 대치
    df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
    
    # 3. 나이 결측치 - 성별/등급별 평균 대치
    df['age'] = df['age'].fillna(df.groupby(['pclass', 'sex'])['age'].transform('mean'))
    
    # 4. 파생변수 생성 (FamilySize)
    df['family_size'] = df['sibsp'] + df['parch'] + 1
    
    return df

# 데이터 로드 및 전처리
raw_df = sns.load_dataset('titanic')
df = preprocess_titanic(raw_df.copy())

# 12. 시각화 대시보드 (3개의 주요 관점)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# [Insight 1] 성별과 등급 (계급과 성별의 교차)
sns.barplot(ax=axes[0], x='pclass', y='survived', hue='sex', data=df)
axes[0].set_title('Survival Rate by Pclass & Sex')
axes[0].set_ylabel('Survival Probability')

# [Insight 2] 나이 분포 (어린이 생존)
sns.kdeplot(ax=axes[1], data=df[df['survived']==1]['age'], label='Survived', shade=True, color='blue')
sns.kdeplot(ax=axes[1], data=df[df['survived']==0]['age'], label='Died', shade=True, color='red')
axes[1].set_title('Age Distribution by Survival')
axes[1].legend()

# [Insight 3] 가족 규모 (대가족의 비극)
sns.pointplot(ax=axes[2], x='family_size', y='survived', data=df, color='purple')
axes[2].set_title('Survival Rate by Family Size')
axes[2].axhline(df['survived'].mean(), color='gray', linestyle='--', label='Average Survival')

plt.tight_layout()
plt.show()

# 19. 챌린지: 최적의 생존 조건 확인
# 생존율 1위 그룹 필터링
print("=== 생존율이 가장 높은 그룹 (1등석 여성) ===")
best_group = df[(df['pclass'] == 1) & (df['sex'] == 'female')]
print(f"생존율: {best_group['survived'].mean() * 100:.2f}%")
