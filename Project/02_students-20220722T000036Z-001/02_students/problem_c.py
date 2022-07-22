import json
from pprint import pprint


def movie_info(movies, genres):

    all_movies = []
    for movies_inform in movies:
        # b번 문제 함수 재활용
        genre_ids = movies_inform.get('genre_ids') # ids의 리스트 값 추출
        genre_names = {} # 빈 딕셔너리 생성
        for genre in genres: # 해당 리스트에 들어있는 딕셔너리 순환
            for i in genre_ids: 
                if i == genre.get('id'): # id와 숫자가 동일한 경우를 찾는 조건식
                    list1 = list(genre.items()) # 찾은 값을 list1에 (키, 값) 형식으로 저장
                    genre_names[list1[1][1]] = list1[1][0] # genre_names키에 저장하려고 했으나 키 중복으로 값이 겹쳐서 거꾸로 적어 넣음

        genre_names_list = [name for name in genre_names.keys()] # 키만 뽑아내서 리스트 생성
        genre_names_list = genre_names_list[::-1] # 풀이와 동일하게 만들어주기 위해 역순생성

    
        new_movie_dict = {
            'genre_names' : genre_names_list,
            'id' : movies_inform.get('id'),
            'overview' : movies_inform.get('overview'),
            'poster_path' : movies_inform.get('poster_path'),
            'title' : movies_inform.get('title'),
            'vote_average' : movies_inform.get('vote_average') 
        } 
        all_movies.append(new_movie_dict)
    return all_movies
    

    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
