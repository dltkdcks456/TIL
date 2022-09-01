# Django - 09.01

app_name = 'articles'

path('', views.index, name='index')

- 경로로 요청이 들어오면 응답한다

- 127.0.0.8000/articles 를 받으면 view의 index함수를 실행, name뒤의 내용은 닉네임

- articles:index 로 사용된다.

- 로컬호스트8000/articles/로 보겠다.

- `path('new/', views.new, name='new')`

  - localhost:8000/articles/new/ 로 오는 경로를 가진다
  - url을 입력하면 또는 프로그램으로 요청이 오면 views의 new함수를 실행한다.
  - articles:new로 경로 사용

  - 장고 DTL 안에서 {% url articles:new %}까지 사용해주어야함.

```python
> articles
	>templates # 장고의 규약 
    	> articles # template namespace, 물리적인 방법으로 구분 진행
    	
```

- DB는 server와 따로 가져간다. 
- Oracle: DB서버만을 위한 OS, Language를 구성

- models.Model로 미리 구성해둠
- TextField가 4GB정도 들어감.

```python
created_at = models.DateTimeField(auto_now_add=True)# 생성 시간
updated_at = models.DateTimeField(auto_now=True)# 저장 시간
```

- Oracle이 세계적인 기업이며 많은 DB에서 독보적이며 많은 이익을 남김
- MySQL이 오픈 소스로 풀렸으며, 성장하자 Oracle이 기업 인수하고 2가지 버전으로 또 수익을 냄.

- create 세 번째 방법은 유효성을 체크하는 방법이 사라져서 좋지 않다.
- get은 고유한 정보를 받아옴
- filter는 복수, 단일, 빈 데이터도 받아올 수 있음

- update: 기존의 정보를 read한 후 수정해서 save진행

```python
{% url 'articles:index' %}
localhost/articles/index/
```

- redirect: 새로운 URL로 이동

- 302: 새로운 요청이 들어왔어요
- 200: 응답이 완료되었습니다.

- POST: 서버의 내용을 고치기 위한 것(조작)
- GET: 서버의 내용을 조회

- 개발자도구로 네트워크를 통해 실행되는 경로를 다 볼 수 있다.

- 데이터 추가 후 render를 할 경우 html 페이지만 보여주고, 데이터는 함께 보여주지 않음.

- 정보를 지울 때 POST로 해서 지우고 csrf가 함께 포함되어야 한다.