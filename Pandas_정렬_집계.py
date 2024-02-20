# 실습
import pandas as pd
import numpy as np

# 1. data/diamonds.csv를 읽어 DataFrame 생성
dia = pd.read_csv('data/diamonds.csv')
print(dia)

# 2. dataframe 정보 조회
print(dia.shape)
print(dia.info())

# 상/ 하위 5개 행 조회
print(dia.head())
print(dia.tail())

# 결측치 확인
print(dia.isna().sum())

print(dia.cut.value_counts())
print(dia.color.value_counts())
print(dia.clarity.value_counts())

# 3. carat, price, depth의 합계, 평균, 최대, 최소 조회
print(dia[['carat', 'price', 'depth']].agg(['sum', 'mean', 'max', 'min']))

# 4. price는 최대, 최소, color는 고유값의 개수를 조회
print(dia['price'].agg(['max', 'min']), dia['color'].nunique())

# 같은 코드
print(dia.agg({
    "price" : ['min', 'max'],
    'color' : 'nunique'
}))

# 5. cut의 고유값별 개수를 조회
print(dia['cut'].value_counts())

# 6. cut별 가격 평균 조회
print(dia.groupby('cut')['price'].mean().sort_values())

# 7. cut별 가격 평균중 4000이상만 조회
result = dia.groupby('cut')['price'].mean().sort_values()
print(result[result >= 4000])

# 8. clarity별 carat 평균과 표준편차 조회
print(dia.groupby('clarity')['carat'].agg(['mean', 'std']))

# 9. cut과 color 별로 가격은 평균을 carat은 최대값을 조회
d = {
    'price' : 'mean',
    'carat' : 'max'
}
print(dia.groupby(['cut', 'color']).agg(d))

# 10. 9번 문제의 결과에서 가격의 평균이 5000이상이고 carat의 최대값이 3이상인 결과만 조회
result = dia.groupby(['cut', 'color']).agg(d)
print(result[(result['price'] >= 5000) & (result['carat'] >= 3)])
# 같은 코드
print(result.query('price >= 5000 and carat >= 3'))