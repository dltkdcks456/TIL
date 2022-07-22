import json


def max_revenue(movies):
    revenue_dict = {}
    for movie_each in movies_list:
        identity = movie_each['id'] # 각 영화별 id 찾기

        movie_identity = open(f'data/movies/{identity}.json', encoding = 'utf-8')
        movie_list_identity = json.load(movie_identity) # 지칭한 파일 오픈

        revenue_dict[movie_each['title']] = movie_list_identity['revenue'] # revenue_dict에 영화제목과 수익을 딕셔너리 형태로 넣음
    
    revenue_list = [] # 수입 내역 리스트 생성
    for key, revenue in revenue_dict.items():
        revenue_list.append(revenue) # 딕셔너리 각각을 순회하며 수입 내역 리스트 삽입
    max_total = max(revenue_list) # 해당 리스트에서 최고값 추출

    for key, revenue in revenue_dict.items(): # 딕셔너리 순회
        if revenue == max_total: # 최고 수익과 일치되는 value를 찾은 후
            return key # 해당 key를 리턴
    
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
