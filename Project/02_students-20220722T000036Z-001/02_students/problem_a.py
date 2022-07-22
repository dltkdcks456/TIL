import json
from pprint import pprint

def movie_info(movie_dict):
    new_movie_dict = {
        'genre_ids' : movie_dict.get('genre_ids'),
        'id' : movie_dict.get('id'),
        'overview' : movie_dict.get('overview'),
        'poster_path' : movie_dict.get('poster_path'),
        'title' : movie_dict.get('title'),
        'vote_average' : movie_dict.get('vote_average') 
    } # 해당 키와 동일할 때의 값을 가져옴
    return new_movie_dict
    # 여기에 코드를 작성합니다.    
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
