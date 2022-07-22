import json
from pprint import pprint


def my_movie_list(movies):
    total_movie_list = list() # 총 영화 정보가 담길 곳(딕셔너리 형태)
    for each_movie in movies: # 보여줄 정보 모음집
        identity = each_movie.get('id') # 각각의 영화에 해당하는 id 정보
        movies_sub_json = open(f'data/movies/{identity}.json',encoding = 'utf-8')
        movies_sub_data = json.load(movies_sub_json) # 일치하는 영화에 대한 정보 재추출
        
        In_generes =[i['name'] for i in movies_sub_data['genres']] # 데이터 안에 다시 딕셔너리 값 추출
        In_generes_join = ', '.join(In_generes) # 리스트 합쳐서 문자열로 출력

        final_error = movies_sub_data['production_companies'][0].get('origin_country') # 국가 정보 추출을 변수로 만듦

        movie_dict = {
            "영화제목  " : each_movie.get('title'),
            "개봉일  " : each_movie.get('release_date'),
            "평점  " : each_movie.get('vote_average'),
            "장르  " : (In_generes_join), # 위에 for문을 통해 추출한 장르를 문자열로 출력
            "국가  " : '없음' if final_error == '' else final_error, # 조건문을 통해 국가가 없는 경우 '없음'을 추출
            "러닝타임  " : movies_sub_data.get('runtime'),
            "배급사  " : movies_sub_data['production_companies'][0]['name'], # 딕셔너리 -> 리스트 -> 딕셔너리로 들어가서 값을 출력
        }
        total_movie_list.append(movie_dict)
    return total_movie_list


# movies와 movies폴더 활용
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding = 'utf-8')
    movies_data = json.load(movies_json)

    pprint(my_movie_list(movies_data))