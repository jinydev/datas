---
layout: numpy
title: "4.6.1 배열 결합 개요"
---

# 4.6.1 배열 결합 개요와 유용한 함수

## 4.6.1 배열 결합 개요

**[비유] Axis(축)의 방향 잡기**
- **Axis 0 (수직/행 방향)**: 아파트 층을 위로 차곡차곡 쌓아 올리듯 결합합니다.
- **Axis 1 (수평/열 방향)**: 기차를 연결하듯 옆으로 나란히 결합하여 길이를 늘입니다.

배열을 결합하는 방법 중에서 가장 많이 사용하는 `numpy.vstack()`과 `numpy.hstack()`을 먼저 알아보자.

배열을 수직(vertically)으로 결합하는 `numpy.vstack()`과 수평(horizontally)으로 결합하는 `numpy.hstack()` 함수이다. 이 `numpy.vstack()`과 `numpy.hstack()`은 다음 그림으로 이해하면 매우 쉽다.

![배열 결합을 위한 np.vstack()과 np.hstack()](img/page_002.png)

위 그림에서도 알 수 있듯이 2차원 배열에서의 수직으로 합치는 `vstack`은 열 수가 같아야 하며 수평으로 합치는 `hstack`은 행 수가 같아야 한다.
