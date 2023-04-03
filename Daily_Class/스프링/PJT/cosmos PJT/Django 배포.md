### Django 배포

- requirements.txt에서 

  ```
  pywin32
  ```

   와 

  ```
  pywinpty
  ```

  는 삭제 필요(window버전이기 때문에 우분투와 맞지 않음)

  - `pip install -r requirements.txt` 에서 오류 발생함

- DockerFile

```python
# python 버전 or latest 입력
FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /srv/django
ADD . /srv/django

WORKDIR /srv/django
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
# django를 단독으로 실행할때 사용 명령어
# 단, nginx를 이용해서 django를 실행할때는 주석처리!!
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

- Allowed_host 에러
  - `settings.py`에 다음과 같이 url을 입력해주면 된다.
  - `‘*’`도 가능하지만 비추천!

```python
ALLOWED_HOSTS = ['localhost','j8e104.p.ssafy.io']
```

- 수동 배포를 하면서 느낀점은 코드 수정 시 

  ```
  Docker image
  ```

  까지 모두 삭제해야 반영이 된다.

  - 컨테이너까지만 삭제하고 진행하다가 많은 시간을 낭비했다.

참고사이트: https://choco-life.tistory.com/17