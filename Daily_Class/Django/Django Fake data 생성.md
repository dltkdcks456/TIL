

```python
1.
pip install django-seed
pip install psycopg2 (맥북은 깔리지 않음)

'''
django-seed         0.3.1
djangorestframework 3.14.0
Faker               15.1.1
pip                 22.0.4
psycopg2            2.9.4
'''

2.
settings.py의INSTALLED_APPS에 django_seed를 추가

3.
python manage.py migrate

4.
db.sqlite3를 OPEN DATABASE로 열어줌.

5.
python manage.py seed articles --number=20
```

