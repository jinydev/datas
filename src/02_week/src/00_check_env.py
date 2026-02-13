# 2주차 2강: 준비하기 (환경 점검)
# 파일명: 00_check_env.py

import matplotlib
import matplotlib.pyplot as plt
import platform

# 1. Matplotlib 버전 확인
print(f"Matplotlib Version: {matplotlib.__version__}")

# 2. 한글 폰트 설정
system_name = platform.system()

if system_name == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
    print("Mac 환경: AppleGothic 폰트 설정 완료")
elif system_name == 'Windows': # Windows
    plt.rc('font', family='Malgun Gothic')
    print("Windows 환경: Malgun Gothic 폰트 설정 완료")
else:
    print("기타 환경: 폰트 설정이 필요할 수 있습니다.")

plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
