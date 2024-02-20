# 실습

# Series 생성
import pandas as pd
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

print("데이터 타입: ", s1.dtype)
print("전체 원소의 개수", s1.size)
print("차원별 개수", s1.shape)

s2 = pd.Series([1, 2, 300], dtype = 'int8')
print(s2.dtype)

print(s1[0])
# 없는 index 조회 시 Exception 발생

s3 = pd.Series([100, 80, 90, 60], index=['Python', 'Java', 'C', 'JS'])
print(s3)
print(s3.index)

print(s3.loc['Python'])
print(s3.iloc[0])
# print(s3.iloc['Python']) - Error
# print(s3.loc[0]) - Error

# 한번에 여러개 원소 조회
print(s1[0], s1[1]) # 리스트/튜플 방식
print(s1[[0, 1, 3]]) # 조회 결과를 Series로 묶어서 반환

# Series는 리스트같이 원소 변경 가능
s3[0] = 50
print(s3)

# index이름이 식별자 규칙에 맞으면 . 표기법으로 조회/변경가능
print(s3['JS'], s3.JS)

#Slicing
ss = pd.Series(range(100))
print(ss.dtype, ss.shape)
print(ss)

print(ss[10:20:5]) # index로 slicing. stop 포함안됨
print(ss.loc[10:20:5]) # index name으로 sclicing. stop index 포함

# 벡터화(연산)
s10 = pd.Series([10, -10, 5, 2])
print(s10 + 5)
print(s10 * 2)
print(s10 > 0)
print((s10 > -5) & (s10 < 5)) # Series 에서는 and 연산 불가능

s11 = pd.Series([-10, 2, 3, 7])
print(s10 + s11) # 같은 index 이름끼리 계산
print(s10 <= s11)

import numpy as np
s20 = pd.Series(np.random.randint(0, 1000, 100))

print(s20[s20 >= 900])
print(s20[(s20 >= 100) & (s20 <= 200)])
print(s20[s20.between(100, 200)])

print(np.where(s20.between(200, 250)))

# 주요 메소드
print(s20.dtype) # Series의 데이터 타입
print(s20.size) # 원소의 개수
print(s20.shape) # Series의 형태
print(s20.index) # index 이름을 조회

print(s20.head()) # 앞에 5개 조회
print(s20.tail()) # 뒤에 5개 조회

s30 = pd.Series(np.random.choice(['Python', 'Java', 'C', 'Go', 'Rust'], 100))
print(s30.value_counts()) # 범주값들의 개수
print(s30.value_counts(normalize=True)) # 비율로 알려줌

# 정렬
s40 = pd.Series([20, 6, -10, 100, 7], index = ['Z', 'R', 'A', 'B', 'S'])
print(s40.sort_index()) # index 오름차순 정렬, 원본 유지
print(s40.sort_index(ascending=False)) # 내림차순
print(s40.sort_index(inplace=True)) # 원본 정렬
print(s40.sort_values()) # 값 오름차순 정렬

# 기술 통계량
print(s40.max(), s40.min()) # 최대, 최소
print(s40.idxmax(), s40.idxmin()) # 최대, 최소의 index 
print(s40.sum(), s40.mean(), s40.median()) # 합계, 평균 중앙값
print(s40.std(), s40.var()) # 표준편차, 분산

# 범주형
print(s30.mode()) # 최빈값

# 분위수
s60 = pd.Series(np.random.randint(100, 1000, 100))
print(s60.quantile(q = [0.5])) # 중위수
print(s60.quantile(q = [0.25, 0.5, 0.75])) # 4분위

print(s60.describe()) # count(): 결측치 아닌 원소의 개수
# 원소들이 범주형 문자열일 때
print(s30.describe())
'''
count      100 # 결측치 아닌 원소들의 개수
unique       5 # 고유값(범주값)의 개수
top          C # 최빈값
freq        24 # 최빈값의 빈도수(개수)
'''

# 결측치
import pandas as pd
import numpy as np
s = pd.Series([10, 2, 40, 7, 20, np.nan, 50, np.nan, 10])
print(s)

# 결측치 확인 
print(s.isnull())
# print(s.isna())
# print(s.notnull()) # 결측치가 아닌지

# 결측치 처리
# 제거
print(s.dropna()) # 결측치 제거한 결과 원본은 변경 안됨

s2 = s.copy()
s2.dropna(inplace=True)
print(s2)

# 다른 값으로 대체
print(s.fillna(100000))

print(s.mean()) # pandas는 NaN을 빼고 평균 계산, Numpy는 포함해서 계산
print(s.mean(skipna=False)) # 결측치 포함 계산
print(s.sum(skipna=False))

print(s.fillna(round(s.mean(), 2))) # 평균값 대체
print(s.fillna(round(s.median(), 2))) # 중앙값 대체