---
layout: docs
title: "09. 패키지 matplotlib, seaborn, pydataset 개요와 설치"
---

## 09. 패키지 matplotlib, seaborn, pydataset 개요와 설치

간단히 `mpl`로도 부르는 패키지 `matplotlib`은 파이썬에서 2D 그래픽 그림을 생성하는 데 사용되는 데이터 시각화 라이브러리이다. `matplotlib`은 과학 및 엔지니어링 분야에서 데이터를 시각적으로 탐색하고 표현하는 데 널리 사용되며, 다양한 차트, 플롯, 히스토그램 등을 생성할 수 있다.

또한, 패키지 `seaborn`은 `matplotlib`에 기반한 고수준 인터페이스를 제공하는 시각화 라이브러리이다. 주로 통계적 그래픽 기능을 갖추고 있어 데이터 분석에 유용하게 활용된다. 시본은 다음의 특징을 갖는다.

- **간편한 사용**: 시본은 `matplotlib`와 함께 사용되며, `matplotlib`의 기능을 확장하여 간편하게 고급 시각화를 구현하며, `matplotlib`보다 간단한 코드로 다양한 그래프를 생성
- **통계적 그래픽**: 시본은 통계적 그래픽 기능을 제공하여 히스토그램, 박스 플롯, 회귀선, 히트맵 등 다양한 통계 그래픽을 생성
- **데이터 셋 제공**: 시본은 자체적으로 데이터 셋을 제공하여 실습과 테스트에 용이하며, 예를 들어, 타이타닉 데이터셋과 같은 유명한 데이터 셋을 포함

패키지 `pydataset`은 파이썬에서 사용할 수 있는 데이터셋(datasets)을 쉽게 메모리에 저장하고 활용할 수 있도록 제공되는 패키지이다. 이 패키지는 R 패키지인 `datasets`에 포함된 여러 데이터셋을 파이썬에서 바로 사용할 수 있도록 제공한다. 다양한 테스트용 데이터셋을 포함하고 있어, 데이터 분석이나 시각화 연습 등 다양한 용도로 활용될 수 있다. 이러한 데이터 셋을 장난감 데이터(toy data)라고도 부른다. `pydataset`의 주요 특징은 다음과 같다.

- **다양한 데이터셋 제공**: `pydataset` 패키지는 R 패키지인 `datasets`에 포함된 많은 데이터셋을 파이썬에서 사용할 수 있도록 변환한 것으로, 빠르게 샘플 데이터를 활용할 수 있음
- **간편한 데이터 로드**: 패키지를 설치하고 메모리에 로드(load)한 후, `data()` 함수를 사용하여 데이터셋을 쉽게 사용할 수 있음
- **표준화된 데이터 형태**: 메모리에 적재한 데이터셋은 판다스 데이터프레임 형태로 반환되어 데이터 분석 및 조작이 용이함

다음 명령 `pip show seaborn matplotlib pydataset`으로 한번에 모든 패키지의 설치 유무를 확인하자.

```bash
pip show seaborn matplotlib pydataset
```

![명령 프롬프트 pip show seaborn matplotlib pydataset](/Users/hojin8/docs/070.강의/c01.빅데이터분석/파이썬으로_배우는_데이터분석입문/파이썬으로_배우는_데이터분석입문2/temp_images/page_017.png)

이제, 다음 명령 `pip install seaborn pydataset`으로 한 번에 패키지 `seaborn`, `matplotlib`, `pydataset`을 설치한다. 명령 `pip`에서의 설치는 필요한 패키지의 종속성에 따라 설치한다. 패키지 `seaborn`은 `matplotlib`을 필요로 하므로 `seaborn`만 설치해도 알아서 `matplotlib`을 설치한다. 그러므로 `seaborn`과 `pydataset`을 명령에 기술한 것이다. 물론 패키지 3개를 모두 기술해도 상관없다.

```bash
pip install seaborn pydataset
# 또는
pip install seaborn matplotlib pydataset
```

![명령 프롬프트 pip install seaborn pydataset](/Users/hojin8/docs/070.강의/c01.빅데이터분석/파이썬으로_배우는_데이터분석입문/파이썬으로_배우는_데이터분석입문2/temp_images/page_018.png)
