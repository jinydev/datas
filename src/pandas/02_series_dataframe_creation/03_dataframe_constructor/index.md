---
layout: pandas
title: "6.2.3 클래스 DataFrame 생성자 개요"
---

# 6.2.3 데이터프레임 생성

## 6.2.3 클래스 DataFrame 생성자 개요

데이터프레임은 2차원 데이터로 크기 변경이 가능, 잠재적으로 이질적인 자료가 저장된 테이블 형태의 데이터이다. 데이터프레임을 만들 때 사용하는 클래스 `DataFrame` 생성자는 다음과 같다.

```python
class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
```

*   **data**: ndarray(구조화 또는 동종), Iterable, dict 또는 DataFrame
*   **index**: 인덱스 또는 배열과 유사한 자료. 결과 프레임에 사용할 인덱스로 입력 데이터의 인덱싱 정보 부분이 없고 제공된 인덱스가 없는 경우 기본적으로 `RangeIndex`가 사용됨.
*   **columns**: 인덱스 또는 배열과 유사한 자료. 데이터에 열 레이블이 없을 때 결과 프레임에 사용할 열 레이블이며 기본값은 `RangeIndex(0, 1, 2, ..., n)`임.
*   **dtype**: 기본값 없음. 강제할 데이터 유형으로 단일 dtype만 허용됨. None의 경우, 추론함.
*   **copy**: bool 또는 없음, 기본값 없음. 입력에서 데이터를 복사하며 dict 데이터의 경우 기본값 `copy=True`.