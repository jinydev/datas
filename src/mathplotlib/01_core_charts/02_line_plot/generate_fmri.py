import seaborn as sns
import matplotlib.pyplot as plt
import os

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic' # Mac OS
plt.rcParams['axes.unicode_minus'] = False

try:
    fmri = sns.load_dataset("fmri")
except Exception as e:
    print(f"Failed to load dataset from seaborn: {e}")
    # 대체 방법 모색
    import pandas as pd
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/fmri.csv"
    fmri = pd.read_csv(url)

# 1. fmri_line_basic.svg 생성
plt.figure(figsize=(8, 5))
sns.set_theme(style="darkgrid")
# set_theme이 폰트 설정을 덮어쓰므로 다시 적용
plt.rcParams['font.family'] = 'AppleGothic' 
plt.rcParams['axes.unicode_minus'] = False

sns.lineplot(data=fmri, x="timepoint", y="signal")
plt.title("시간에 따른 환자들의 뇌파 신호 (평균과 신뢰 구간)")

output_path_1 = "/Users/hojin9/jinysite/datas/src/mathplotlib/01_core_charts/02_line_plot/img/fmri_line_basic.svg"
os.makedirs(os.path.dirname(output_path_1), exist_ok=True)
plt.savefig(output_path_1, format="svg", bbox_inches="tight")
print(f"Saved correctly: {output_path_1}")

plt.clf()

# 2. fmri_line_hue.svg 생성 (이것도 이상할 수 있으므로 함께 새로 생성)
plt.figure(figsize=(8, 5))
sns.set_theme(style="darkgrid")
plt.rcParams['font.family'] = 'AppleGothic' 
plt.rcParams['axes.unicode_minus'] = False

sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", style="event")
plt.title("자극(stim) vs 비자극(cue) 환자 그룹별 뇌파 흐름 비교")

output_path_2 = "/Users/hojin9/jinysite/datas/src/mathplotlib/01_core_charts/02_line_plot/img/fmri_line_hue.svg"
plt.savefig(output_path_2, format="svg", bbox_inches="tight")
print(f"Saved correctly: {output_path_2}")
