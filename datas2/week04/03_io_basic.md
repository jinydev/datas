# 4-3. 파일 읽고 쓰기 (CSV, Excel)

## 1. 데이터를 언제 다 타이핑 하나요?
직접 `pd.DataFrame({...})` 이렇게 타이핑 할 일은 잘 없습니다.
대부분 파일로 저장된 데이터를 **불러와서(Load)** 씁니다.

## 2. CSV 파일 불러오기
CSV(Comma Separated Values)는 콤마로 구분된 텍스트 파일로, 데이터 분석에서 가장 많이 쓰입니다.

```python
# sample.csv 파일이 있다고 가정
# df = pd.read_csv('sample.csv')

# 없으면 인터넷 주소를 바로 넣어도 됩니다!
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)

# 앞부분 5줄만 살짝 보기
print(df.head())
```

## 3. 엑셀 파일 불러오기
```python
# 엑셀은 read_excel
# df = pd.read_excel('score.xlsx')
```

## 4. 파일로 저장하기
열심히 분석한 결과를 파일로 내보낼 수도 있습니다.

```python
# 분석 결과 저장
df.to_csv('my_result.csv', index=False)
```

## 5. 핵심 정리
*   `pd.read_csv()`: CSV 읽기.
*   `df.head()`: 데이터가 잘 읽혔는지 상위 5개 확인 (습관처럼 써야 합니다!).
*   `df.to_csv()`: CSV 저장.
