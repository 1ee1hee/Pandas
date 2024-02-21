# 실습
import pandas as pd
import numpy as np

# stack()
state_fruit = pd.read_csv('data/state_fruit.csv', index_col=0)
print(state_fruit)

# stack() : 컬럼명을 index명으로 내린다
s1 = state_fruit.stack()
print(s1)

# Series를 DataFrame으로 변환(한개 컬럼의 DF)
print(s1.to_frame(name = 'count')) # 컬럼명 지정

# 멀티 index 조회
print(s1['Texas'])
print(s1[('Florida', 'Orange')])

# xs() 메소드를 사용
print(s1.xs('Orange', level=-1))

s1 = state_fruit.stack()
s_df = s1.reset_index()
s_df.columns = ['state', 'fruit', 'count']
print(s_df)

# unstack()
print(s1.unstack()) # -1 level의 index를 컬럼으로 변경

s2 = s1.unstack(level=0)
print(s2)

# axis의 이름을 지정(변경) => axis 이름: 컬럼명 또는 index명 에 대한 이름
s3 = s2.rename_axis(columns='state', index='fruit')
print(s3)

# melt() : 컬럼명을 컬럼의 값으로 변환
state_fruit2 = pd.read_csv('data/state_fruit.csv')
state_fruit2.rename({state_fruit2.columns[0]:"State"}, axis=1, inplace=True)
print(state_fruit2)

# vars -> 컬럼들
s = state_fruit2.melt(id_vars=['State'], # 값으로 변경하지 않고 컬럼으로 유지할 컬럼이름들을 지정
                      value_vars=['Apple', 'Orange', 'Banana'], # 단일 컬럼의 값으로 변경할 컬럼 이름들을 지정
                      var_name="Fruits", # 컬럼명이 값으로 들어간 컬럼의 이름을 지정
                      value_name="Count" # value들이 값으로 들어간 컬럼의 이름을 지정
                      )
print(s)

# id_vars만 지정하면 지정되지 않은 나머지 컬럼들은 모두 값으로 변경된다
print(state_fruit2.melt(id_vars=['State'],
                  var_name="Fruits",
                  value_name="Count"
                  ))

# id_vars를 생략하면 value_vars의 컬럼들을 제외한 나머지는 drop
print(state_fruit2.melt(value_vars=['Apple', 'Orange']))

# pivot - index, column, value가 될 컬럼들을 지정해 재구조화
df = s.pivot(index='State', # index에 놓을 컬럼이름
             columns='Fruits', # column에 놓은 컬럼이름
             values='Count') # 값으로 사용할 컬럼 # index 값, 컬럼의 값이 교차하는 지점의 value가 값이 된다
print(df)

# crosstab()
np.random.seed(0)
d = {
    "직업" : np.random.choice(["학생", "자영업", "회원"], 7, p = [0.5, 0.3, 0.2]),
    "혈액형" : np.random.choice(["A", "B"], 7),
    "합격여부" : np.random.choice(["합격", "불합격"], 7)
}
df = pd.DataFrame(d)
print(df)

print(pd.crosstab(index = df["직업"], # index에 위치시킬 컬럼(범주형)
            columns = df["혈액형"] # column에 위치시킬 컬럼(범주형)
            ))

print(pd.crosstab(index = df['직업'],
            columns = [df['혈액형'], df['합격여부']]
            ))