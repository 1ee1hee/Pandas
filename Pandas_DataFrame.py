# 실습
import pandas as pd
import numpy as np

# data/movie.csv를 읽어서 변수 movie에 할당
movie = pd.read_csv('data/movie.csv')
print(movie.head())

# 데이터 프레임을 파일로 저장 (파일명 : saved_data/movie_df.csv)
movie.to_csv('saved_data/movie_df.csv', index = False)

# 데이터 프레임을 엑셀파일로 저장(파일명 : saved_data/movie_df.xlsx)
movie.to_excel('saved_data/movie_df.xlsx', index = False)

# 저장한 movie_df.xlsx 파일을 읽어서 m_df 변수에 할당
m_df = pd.read_excel('saved_data/movie_df.xlsx')
print(m_df.head())

# movie dataframe를 이용해 코드 작셩

# director_name 컬럼의 값들을 조회
print(movie['director_name'])

# actor_1_name, actor_2_name, actor_3_name 컬럼의 값들
print(movie[['actor_1_name', 'actor_2_name', 'actor_3_name']])

# 1, 3, 4, 7 번 컬럼 조회
print(movie[movie.columns[[1, 3, 4, 7]]])

# 1 ~ 5 번 컬럼 조회
print(movie[movie.columns[1:6]])

# 정수형(int64) 컬럼만 조회
print(movie.select_dtypes(include='int64'))

# 정수형(int64) 실수형(float64) 타입을 제외한 컬럼들만 조회
print(movie.select_dtypes(exclude=['int64', 'float64']))

# actor_1_name, actor_2_name, actor_3_name 컬럼의 값을 조회
a = movie.filter(like='_name')
print(a.filter(like='actor'))
print(movie.filter(regex='actor_[123]_name'))

# actor_1_facebook_likes, actor_1_name 컬럼의 값을 조회
print(movie.filter(like='actor_1'))

# color, director 컬럼을 조회. 없는 컬럼명이라도 에러가 안나도록 조회
print(movie.filter(items = ['color', 'director']))

# movie가 들어가는 컬럼 조회
print(movie.filter(like='movie'))

# movie dataframe을 이용해 loc과 iloc 관련 코드 작성

# movie_title 컬럼을 index명으로 지정
movie.set_index('movie_title', inplace=True)
print(movie)

# 행이름이 Avatar인 행 조회
print(movie.loc['Avatar'])

# 행이름이 Spider-Man 3, The Avengers, Titanic인 행 조회
print(movie.loc[['Spider-Man 3', 'The Avengers', 'Titanic']])

# 행이름 Spectre ~ Robin Hood까지 범위 조회
print(movie.loc['Spectre' : 'Robin Hood'])

# 행이름이 John Carter이고 열이름이 director_name인 값 조회
print(movie.loc['John Carter', 'director_name'])

# 1번행
print(movie.iloc[0]) # 첫번째 행
print(movie.iloc[1]) # index 1번

# 마지막 행 조회
print(movie.iloc[-1])

# 1, 2, 5, 6, 9 번행 조회
print(movie.iloc[[1, 2, 5, 6, 9]])

# 10 ~ 20 행 조회
print(movie.iloc[10:21])

# movie dataframe에서 5 ~ 10 행의 color, director_name, num_critic_for_reviews 컬럼(0, 1, 2번째 컬럼)을 iloc을 이용해 조회
print(movie.iloc[5:11, [0, 1, 2]])
print(movie.iloc[5:11, :3]) # 같은 코드

# movie dataframe의 index명을 컬럼 설정
movie.reset_index(inplace=True)
print(movie)

# 상영시간 (duration)이 300 이상인 영화를 조회
print(movie[movie['duration'] >= 300])

# 상영시간 (duration)이 300 이상인 영화들의 영화제목(movie_title)과 감독이름(director_name) 조회
print(movie[movie['duration'] >= 300][['movie_title', 'director_name']])

# 감독이름(director_name)이 'Quentin Tarantino'의 영화들만 조회
print(movie[movie["director_name"] == "Quentin Tarantino"])

# James Cameron의 영화중 상영시간이 150분 이상인 영화들의 제목(movie_title), 상영시간(duration), 컬러여부(color) 조회
print(movie[(movie["director_name"] == "James Cameron") & (movie['duration'] >= 150)][['movie_title', 'duration', 'color']])

# query() 메소드
# 상영시간이 300분 이상인 영화들만 조회
print(movie.query('duration >= 300'))

# 상영시간이 250분 ~ 300분인 영화들 조회
print(movie.query("250<duration<300"))
print(movie.query("duration>250 & duration<300")) # 같은 코드

# 컬러 영화가 아닌 영화 조회
print(movie.query("color != 'Color'"))

# 이름에 James가 들어가는 감독의 영화 조회
print(movie.query("director_name.notna()").query("director_name.str.contains('James')"))