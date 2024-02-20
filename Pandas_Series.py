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