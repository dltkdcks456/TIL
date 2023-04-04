# Pandas

- \`JupyterNotebook`을 사용하면 결과를 블럭 단위로 볼 수 있어서 편리하다.
- 파일 열기

```python
import pandas as pd

file = pd.read_csv("./관광지.csv", encoding='utf-8')
```

- 컬럼 추가하기

```python
file['tendency'] = ''
file['type'] = ''
file['dtype'] = ''
print(file.iloc[0])
columns_length = len(file.columns)
print(len(file.columns))
```

- 특정 컬럼의 비교를 통해 데이터 추가하기
  - 최대한 반복을 피하기 위해 컬럼 `전체 길이`와 `type_name` 을 활용하였다.

```python
type_name = 'tour'
for i in range(len(file)):
    text = ''
    if file.iloc[i, columns_length - 10] > file.iloc[i, columns_length - 9]:
        text += 's'
    elif file.iloc[i, columns_length - 10] < file.iloc[i, columns_length - 9]:
        text += 'd'
    else:
        text += 'sd'
    
    if file.iloc[i, columns_length - 8] > file.iloc[i, columns_length - 7]:
        text += 'f'
    elif file.iloc[i, columns_length - 8] < file.iloc[i, columns_length - 7]:
        text += 'p'
    else:
        text += 'fp'
    
    if file.iloc[i, columns_length - 6] > file.iloc[i, columns_length - 5]:
        text += 'i'
    elif file.iloc[i, columns_length - 6] < file.iloc[i, columns_length - 5]:
        text += 'o'
    else:
        text += 'io'
    
    file.iloc[i, columns_length - 3] = text
    file.iloc[i, columns_length - 2] = type_name
    file.iloc[i, columns_length - 1] = type_name
```

- 행 이름 변경 명령어

```python
# 행 이름 변경
    file.rename(columns= {'mapx' : 'longitude', 'mapy' : 'latitude'}, inplace=True)
```

- 컬럼 삭제

  - `drop` 명령문을 사용한다

  - `axis = 1` 은 열을 의미한다

  - ```
    inplace = True
    ```

     는 현재 DataFrame에 변경을 주겠다는 의미이다.

    - 그렇지 않으면 다른 변수를 지정해주어야 한다.

```python
file.drop(['static', 'dynamic', 'flex', 'poor', 'indoor', 'outdoor', 'cluster'], axis = 1, inplace = True)
```

- 파일 csv로 추출
  - cp949를 선택해도 utf8로 변환이 잘 되었다.
  - 추후에 확인이 더 필요하다.(어떤 파일은 열 하나에 모든 데이터가 합쳐지는 에러 발생함)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f3dae07-b4bc-4db9-8f0a-78734d542b6f/Untitled.png)

```python
file.to_csv("관광지 가공(utf-8).csv", encoding='cp949', index=False)
file.to_csv("관광지 가공(utf-8).csv", encoding='utf-8', index=False)
file.to_csv("관광지 가공(utf-8).csv", encoding='utf-8-sig', index=False)
```