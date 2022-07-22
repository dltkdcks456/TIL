import json


def dec_movies(movies):
    dec_movie_list = list() # 영화 제목을 넣을 빈 리스트 작성
    for each_movie in movies: # 앞 예제와 동일하게 파일 열어주는 루트 작성
        identity = each_movie['id']
        open_movie = open(f'data/movies/{identity}.json', encoding = 'utf-8')
        movie_list = json.load(open_movie)

        if movie_list['release_date'][5:7] == '12': # 개봉 날짜 비교
            dec_movie_list.append(movie_list['title']) # 조건 만족 시 리스트 원소로 추가
    return dec_movie_list
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
