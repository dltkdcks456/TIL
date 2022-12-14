# 4-6. 반복문(for, while, break, continue)

- `range()`
  - 정수에 관련된 수를 나열
  - range(1, 10)과 같은 표현은 1부터 9까지 정수를 생성
  - List를 씌워서 리스트로 출력 진행
  - 감소하는 형태는 `range(10, 0, -1)`과 같은 형태로 입력해준다.
- `for i in range(10)`
  - for문이 실행되면서 i가 지역 변수로 0부터 9까지 실행됨
  - for... else...구문은 중간에 break되어 종료되면 else 뒤의 구문을 실행하지 않음
  - 정상적으로 모두 지나고 종료되면 else 뒤의 구문이 실행됨

```python
for i in range(1, 11):
    print(i)
    if i == 15:
        break
else:
    print(11)
```



- `print`
  - 자동적으로 출력 후 엔터가 입력되어 있다.
    - end='' 에 입력을 넣어주면서 그 형태를 바꿀 수 있다.
    - sep=''을 통해서 나열된 출력 사이에 입력 형태를 바꿀 수 있다.

- `while`
  - 뒷 조건을 만족할 경우 아래 작성된 명령어를 순차적으로 실행

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

- `break`
  - 반복문 내에서 조건 만족 시 반복문 종료

```python
i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1
    
```

- `continue`
  - continue 이하의 명령문을 실행하지 않고 반복문의 다음 순서를 진행

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

### 1. 1부터 N까지 홀수 출력하기

```python
n = int(input())
for i in range(1, n + 1):
    if i % 2:
        print(i)
```

### 2. 1부터 N까지의 합 구하기

```python
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
print(s)
```

### 3. N의 약수 출력하기

```python
n = int(input())
li = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        li.append(i)
        li.append(n // i)
print(sorted(set(li)))
```

- 중첩 반복문(2중 for문)

```python
for i in range(5):
    for j in range(5):
        print(i, j)
```

### 별 그리기(자습)

````python
for i in range(1, 7):
    star = '*' * (2 * i - 1)
    print(f'{star:^11}')
```
     *     
    ***
   *****
  *******
 *********
***********
```
for i in range(1, 7):
    star = '*' * i
    print(f'{star:>6}')
```
     *
    **
   ***
  ****
 *****
******
```
````

