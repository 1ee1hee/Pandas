# 실습
import datetime

# 날짜 시간 객체 생성
d = datetime.date(year=2024, month=2, day=21) # 날짜
t = datetime.time(hour=22, minute=27, second=43, microsecond=999999) # 시간
dt = datetime.datetime(year=2023, month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)

print(f"date:{d}\ntime:{t}\ndatetime:{dt}")
print(dt.year, dt.month, dt.second)


from datetime import datetime, time, date
# 실행시점에 날짜, 일시 조회
print("현재 날짜:", date.today())
print("현재 일시:", datetime.now())

# timedelta를 이용한 계산
from datetime import timedelta
tdelta = timedelta(days=1) # 1일차
tdelta = timedelta(weeks=1) # 1주일 차
tdelta = timedelta(weeks=2, days=3, hours=5, minutes=10, seconds=30, milliseconds=100, microseconds=100000)

c = datetime.now()
print(c)
print(c-tdelta)
print(c+tdelta)

print(date(2024, 2, 17) - date(2023, 12, 12))
print(datetime.now() - datetime(2022, 1, 1, 10, 20, 22))

# datetime과 문자열간 변환
today = date.today()
dow = list('월화수목금토일')
print(dow[today.weekday()])
print(today)
print(today.strftime(f"%Y년 %m월 %d일 %a {dow[today.weekday()]}요일"))
curr = datetime.now()
print(curr)
print(curr.strftime("%Y/%m/%d %H, %I %p"))

s = "2000년 10월 30일"
print(datetime.strptime(s, "%Y년 %m월 %d일"))

# Pandas Timestamp
import pandas as pd
print(pd.Timestamp(year = 2020, month = 11, day = 21, hour = 17, minute = 30, second = 10, microsecond = 1, nanosecond = 1))

# 문자열 생성
# 날짜 : '/'나 '-'로 구분자를 사용, 시간 : ':'을 구분자로 사용
print(pd.Timestamp('2024/1/2 12:23:30.1211'))
print(pd.Timestamp('2024-1-2T12:23:30.1211'))

# 유닉스 타입을 기준으로 경과한 날짜
print(pd.Timestamp(100), # 100나노초 경과한 일시
      pd.Timestamp(10, unit = 'Y'), # 10년
      pd.Timestamp(10, unit = 'M'), # 10개월
      pd.Timestamp(10, unit = 'W') # 10주
     )

# to_datetime()
s1 = pd.Series([10, 100, 1000, 10000])
print(pd.to_datetime(s1, unit= "D"))

s2 = pd.Series(['2000-01-01', '2001-03-10', '2023-01-12', 'sgssssss']) 
result = pd.to_datetime(s2, errors = 'coerce')
# errors : 변환 못하는 문자열일 경우 어떻게 처리할지 지정. ignore : 무시, coerce : NaT결측치 처리, raise: Exception발생 - 기본값
print(result)

df = pd.read_csv('data/walmart_stock.csv')
print(df.info())

df2 = df.copy()

# Date : object -> datetime 타입의 컬럼으로 변환
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

df2['Date'] = df2['Date'].astype('datetime64')
print(df2.info())

# 0번째 컬럼은 datetime 타입으로 변환
df3 = pd.read_csv('data/walmart_stock.csv', parse_dates=[0])
print(df3.info())

# Timestamp 간 연산 및 Time Delta
s1 = pd.to_datetime(pd.Series(['2010-01-01', '2010-03-01', '2010-06-01']))
s2 = pd.to_datetime(pd.Series(['2012-01-01', '2012-03-01', '2012-06-01']))
result = s2 - s1
print(result)

t_delta = pd.Timedelta(weeks=2, days=3)
print(s1 + t_delta)
print(s1 - t_delta)

# 시계열 데이터셋
from datetime import datetime
import pandas as pd
import numpy as np
dates = [
    datetime(2022, 1, 1), datetime(2022, 1, 2),
    datetime(2022, 1, 3), datetime(2022, 1, 4),
    datetime(2022, 2, 1), datetime(2022, 2, 2),
    datetime(2022, 2, 3), datetime(2022, 2, 4),
    datetime(2022, 3, 1), datetime(2022, 3, 2),
    datetime(2022, 3, 3), datetime(2022, 3, 4),
    datetime(2023, 1, 1), datetime(2023, 1, 2),
    datetime(2023, 1, 3), datetime(2023, 1, 4),
    datetime(2023, 2, 1), datetime(2023, 2, 2),
    datetime(2023, 2, 3), datetime(2023, 2, 4),
    datetime(2023, 3, 1), datetime(2023, 3, 2),
    datetime(2023, 3, 3), datetime(2023, 3, 4),
]
np.random.seed(0)
values = np.random.standard_normal(size = 24) # 표준정규분포

s = pd.Series(values, index = dates)
print(s.info())
print(s.index)

# Datetime indexing 과 slicing
print(s[pd.Timestamp(2022, 1, 1)])
print(s['2022-01-02'])

# 부분일치 조회
print(s['2022'])
print(['2022-02'])
print(s[s.index.month == 2])
print(s.index.year.isin([2022, 2023]))
print([(s.index.month == 2) & s.index.year.isin([2022, 2023])])

# Slicing
print(s['2022-02-02':'2023-01-03':3])

# DateOffsets
# date_range
print(pd.date_range(start = '2022-01', end = '2022-02')) # default 간격: 날짜 기준
print(pd.date_range(start = '2022-01', end = '2022-02', periods = 3)) # 3등분한 분위의 날짜
print(pd.date_range(start = '2022-01', periods = 3))
print(pd.date_range(start = '2022-01', periods = 3, freq = 'y')) # y : YearEnd
print(pd.date_range(start = '2022-01', periods = 3, freq = 'ys')) # ys : YearStart
print(pd.date_range(start = '2022-01', periods = 3, freq = '3ys')) # 3ys : 3년
print(pd.date_range('2000', '2023', freq = 'm')) # 월
print(pd.date_range('2000', '2023', freq = 'MS')) # 대문자로, ms : milisecond
print(pd.date_range('2022-01-01', '2022-02', freq = 'H')) # 시간
print(pd.date_range('2023-01-01', '2023-01-12', freq = 'B')) # 주말은 빠짐 B:Business
print(pd.date_range('2000', '2023', freq = 'Q')) # 분기마다
print(pd.date_range('2000', '2023', freq = 'QS'))# s가 안붙으면 끝 날짜를 붙으면 시작날짜를 표현
print(pd.date_range('2020', '2023', freq = 'W-TUE')) # 'W' : 일요일 기준 'W-요일'

# first()
s = pd.Series(range(455), index = pd.date_range('2023/01/01', '2023/01/01 23:59:59', freq = '3T10S')) # T 분 (3분 10초)

print(s.first('900S')) # 900초 앞 데이터
print(s.first('20T')) # 20분 앞 데이터
print(s.first('3H')) # 3시간 앞 데이터

# 데이터 shift
s = pd.Series(range(10, 15), index = pd.date_range('2022/01/01', '2022/01/05'))
print(s)

print(s.shift(2))
print(s.shift(-2))
print(s.shift(freq='3M'))

# 전날 대비 값이 어떻게 변화했는지
print((s/s.shift(1) - 1) * 100)
# 기존 데이터와 비교하기 위해 shift 사용


# resample()을 이용한 집계
s = pd.Series(range(1, 21),
             index = pd.date_range('2000/01', periods = 20, freq = 'T')) # 분 단위로 20개 값
print(s)
print(s.resample('10T')) # 10분 기준으로 group을 나눈다.
print(s.resample('10T').mean()) # closed = left(기본) : [00:00 ~ 10:00), [10:00 ~ 20:00)
print(s.resample('10T', closed = 'right').mean()) # closed = right (50:00 ~ 00:00], (00:00 ~ 10:00], (10:00 ~ 20:00] # 둘다 시작을 index로 사용

df = pd.read_csv('data/walmart_stock.csv', parse_dates=[0], index_col=0)
print(df.head())

print(df.resample('Y')['Close'].mean())
print(df.resample('6M')['Close'].mean())
print(df.resample('Q')['Close'].mean())

# groupby 사용 방법
print(df.groupby(pd.Grouper(freq='Q'))['Close'].mean())
print(df.groupby([pd.Grouper(freq='Q'), 'Volume'])['Close'].mean())


# 기간 이동 집계
# 종가의 5일 이동 평균
moving_avg = df['Close'].rolling(window = 5).mean() # 자기포함 앞에 5개 평균
moving_avg2 = df['Close'].rolling(window = 20).mean() # 20일 이동 평균
print(moving_avg.head(60))
print(moving_avg2.head(60))

moving_avg3 = df['Close'].rolling(window = 20, min_periods = 3).mean()
print(moving_avg3)

print(df['Close'].rolling(window = 20, center = True).mean().head(60))

v = moving_avg2.first('Y') # 20일 이동 평균
v2 = df['Close'].first('Y') # 원래 데이터

import matplotlib.pyplot as plt
plt.figure(figsize=(20,6))
v.plot()
v2.plot()
plt.show()