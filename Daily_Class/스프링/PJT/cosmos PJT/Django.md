# Django

### DB에 연동하기

- 커넥터 설치

```python
pip install mysqlclient
```

- settings.py

   설정

  - manage.py가 있는 디렉토리에서 my_setting.py를 생성한다.
  - github에 올릴 때 DB를 보호하기 위해서이다.

```python
touch my_settings.py
#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'cosmos', #2
        'USER': 'root', #3                      
        'PASSWORD': '1234',  #4              
        'HOST': 'localhost',   #5                
        'PORT': '3306', #6
    }
}

# 기존 settings.py에 있던 시크릿키를 붙여넣는다
SECRET_KEY ='django-insecure-!wodkkgg9%wo^54_*v-2h^%u7hsho2)sce%&@7ryn9^a*pz+5l'
```

\#1 :사용할 엔진 설정

\#2 : 연동할 MySQL의 데이터베이스 이름

\#3 : DB 접속 계정명

\#4 : 해당 DB 접속 계정 비밀번호

\#5 : 실제 DB 주소

\#6 : 포트번호

- [settings.py](http://settings.py) 수정

```python
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': BASE_DIR / 'db.sqlite3',
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'db name',
#         'USER' : 'user name',
#         'PASSWORD' : 'password',
#         'HOST':'localhost',
#         'PORT':'port number'
#     }
# }

DATABASES = my_settings.DATABASES

SECRET_KEY = my_settings.SECRET_KEY
```

### 연동된 DB table 자동 생성

```python
python manage.py inspectdb
```

- 복사해서 models.py에 업데이트하면 된다.