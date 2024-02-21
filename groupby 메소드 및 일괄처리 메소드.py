# 실습
import pandas as pd
import numpy as np

# 1. data/diamonds.csv 조회
dia = pd.read_csv('data/diamonds.csv')
print(dia)

# 2. cut 별 평균 가격이 4000 이상인 diamond 데이터들을 조회
result = dia.groupby('cut')['price'].mean()
print(result[result>4000])

# 2-1.
result = dia.groupby('cut').filter(lambda x : x['price'].mean() >= 4000)
print(result['cut'].value_counts())

# 2-2.
def check_mean(x):
    return x['price'].mean() >= 4000
print(dia.groupby('cut').filter(check_mean)['cut'].value_counts())

# 3. color 별 carat의 최대값과 최소값의 차이가 2이상 3미만의 모든 diamond 데이터들 조회
result = dia.groupby('color')['carat'].agg(['min', 'max'])
print(result[(result['max'] - result['min'] >= 2) & (result['max'] - result['min'] < 3)])

# 3-1.
def carat_min_max_diff(x):
    diff = x['carat'].max() - x['carat'].min()
    return diff >= 2 and diff < 3

result = dia.groupby('color').filter(carat_min_max_diff)
print(result['color'].value_counts())

# 3-2.
print(dia.groupby('color')['carat'].agg(lambda x : x.max() - x.min()))

# 4. clarity 별 평균 가격 컬럼을 DataFrame에 추가
result = dia.groupby('clarity')['price'].transform('mean')
dia.insert(7, 'clarity별 평균가격', result)
print(dia)



#####################################################
# 1. data/diamonds.csv를 읽어 DataFrame으로 만든다
dia = pd.read_csv('data/diamonds.csv')
df = pd.DataFrame(dia)
print(df)

# 2. price 컬럼을 '고가', '중가', '저가' 세개의 범주값을 가지는 "price_cate" 컬럼을 생성한다.
price_cate = pd.cut(df['price'], bins=3,
                    labels=['저가', '중가', '고가'])
df['price_cate'] = price_cate
print(df['price_cate'])

# 3. 가격대(price_cate) 별 carat의 평균을 조회
print(df.groupby('price_cate')['carat'].mean())

# 4. 가격대(price_cate)와 cut 별 평균 가격(price)를 피봇테이블로 조회
print(df.pivot_table(index=['cut', 'color'], columns = 'price_cate', values = 'carat', aggfunc = 'mean'))