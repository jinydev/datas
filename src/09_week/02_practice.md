---
layout: default
title: "9주차 2강: 열과 행 선택하기 (Selection)"
---

# 9주차 2강: 열과 행 선택하기 (Selection)

## 9.2.1. 열(Column) 선택하기

데이터프레임에서 특정 속성(열)만 뽑아내고 싶을 때는 대괄호 `[]` 안에 이름을 넣습니다.

```python
# 데이터 생성
data = {'이름': ['철수', '영희', '민수'], '국어': [90, 80, 70], '영어': [100, 95, 90]}
df = pd.DataFrame(data)

# '이름' 열만 가져오기 (Series 반환)
names = df['이름']
print(names)

# 여러 열 가져오기 (리스트로 묶어서 전달 -> DataFrame 반환)
subjects = df[['국어', '영어']]
print(subjects)
```


<br>

---

<br>

## 9.2.2. 행(Row) 선택하기 (Slicing)

리스트 슬라이싱과 비슷하게 숫자로 범위를 지정할 수 있습니다.

```python
# 0번부터 1번까지 (2번 미만)
top2 = df[0:2]
print(top2)
```


<br>

---

<br>

## 9.2.3. 조건으로 선택하기 (Boolean Indexing)

Numpy에서 배운 것과 똑같습니다! "영어가 95점 이상인 학생"을 찾아봅시다.

```python
# 조건 마스크
mask = df['영어'] >= 95

# 마스크 적용
honor_students = df[mask]
print(honor_students)
#    이름  국어   영어
# 0  철수   90  100
# 1  영희   80   95
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: (내용 채우기)
*   **[핵심 2]**: (내용 채우기)
*   **[핵심 3]**: (내용 채우기)
