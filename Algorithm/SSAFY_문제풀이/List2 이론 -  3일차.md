# List2 이론 -  3일차

## 문제풀이 Note

### 🔰연습문제1 - 연습문제1

`1` 걸린 시간 :  15분

`2` 사용한 자료구조 및 개념 : 상, 하, 좌, 우를 활용하는 법과 2차원 배열



 💡 문제풀이 아이디어 및 어려웠던 점

- 상, 하, 좌, 우의 배치가 어려움
- 4방향의 위치가 배열을 벗어나지 않게 하는 조건 찾기가 어려울 것 같음

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('연습문제1.txt')

T = int(input())
for test in range(T):

    def around(arr, N):
        s = 0
        for i in range(N):
            for j in range(N):
                for k in range(4):  #  우, 하, 좌, 상를 다 찾아줌
                    ni = i + dj[k]
                    nj = j + di[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        s = s + abs(arr[i][j] - arr[ni][nj]) # 각 값들의 절대값의 합을 구함
        return s

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 0, 1, 0] # 우, 하, 좌, 상
    dj = [0, 1, 0, -1]
    ans = around(arr, N)
    print(f'#{test + 1} {ans}')
```

------

### 🔰연습문제2 - 연습문제2

`1` 걸린 시간 :  1시간

`2` 사용한 자료구조 및 개념 : 부분집합, 비트 연산자



 💡 문제풀이 아이디어 및 어려웠던 점

- 공집합 일 때의 조건을 찾기가 까다로웠음
- 아직 비트연산자가 익숙하지 않음

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('연습문제2.txt')

T = int(input())
for test in range(T):
    num_list = list(map(int, input().split()))
    N = len(num_list)
    ans = 0

    s_list = []
    for i in range(1 << N):  # 각 부분집합을 구하는 함수
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += num_list[j]   # 각 부분집합의 합
        if i == 0:  # 공집합 제외하는 조건
            continue
        else:
            s_list.append(s)
            if s == 0:
                ans = 1

    print(f'#{test + 1} {ans}')
```

------

### 🔰1954 - 달팽이 숫자

`1` 걸린 시간 : 1시간 30분

`2` 사용한 자료구조 및 개념 : 방향키 설정, 경계조건 설정



 💡 문제풀이 아이디어 및 어려웠던 점

- 2차원 배열을 읽고 추출하는 연습만 해서 직접 만드는 것은 낯설었음
- 달팽이의 얄미운 움직임을 잘 분석하고 조건문을 잘 세워서 해결이 가능
- 방향키를 계속해서 전환하며 경계를 돌아다니게 설정
- 우선 달팽이에게 초반 기세에서 압도당해 심리적 위축이 가장 큰 원인!!!

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('달팽이 숫자.txt')

T = int(input())
for _ in range(10):
    N = int(input())
    total_list = [[0 for _ in range(N)] for _ in range(N)]

    dx = [1, 0, -1, 0]                                                              # 우, 하, 좌, 상
    dy = [0, 1, 0, -1]
    step = 0                                                                        # 입력될 값 and 각 단계의 값
    direction = 0                                                                   # 방향키
    x = y = 0                                                                       # 초기값
    while step < N * N:                                                             # 25까지 하기 조건문 반복
        if y + dy[direction % 4] < N and x + dx[direction % 4] < N:                 # 범위를 이탈하면 안되므로 각각의 x, y 좌표값은 N 미만
            if total_list[y + dy[direction % 4]][x + dx[direction % 4]] == 0:       # 한 칸 진행할 곳의 값이 0이면 이동 가능
                step += 1                                                           # 해당 칸에 step 기록 후 step과 x, y 좌표값을 상승/여전히 direction은 동일
                total_list[y][x] = step
                x = x + dx[direction % 4]
                y = y + dy[direction % 4]
            else:                                                                   # 앞 칸에 숫자가 있으면 방향 전환 후 step과 x, y좌표값 상승
                direction += 1
                step += 1
                total_list[y][x] = step
                x = x + dx[direction % 4]
                y = y + dy[direction % 4]

        elif y + dy[direction % 4] == N or x + dx[direction % 4] == N:              # x, y 좌표가 범위를 초과하는 경우
            direction += 1                                                          # 방향 전환 및 다른 변수 값 조정
            step += 1
            total_list[y][x] = step
            x = x + dx[direction % 4]
            y = y + dy[direction % 4]

    print(f'#{N}')
    for i in range(N):                                                              # 결과 출력
        print(*total_list[i])
```

------

### 🔰1209 - Sum

`1` 걸린 시간 :  20분

`2` 사용한 자료구조 및 개념 : 각 상황에 대한 조건문



💡 문제풀이 아이디어 및 어려웠던 점

- 배열에 대한 규칙을 찾는 게 중요
- 조건문을 주의 깊게 작성 필요

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('1209.swea.txt')

for test in range(10):
    tc = int(input())
    num_list = [list(map(int, input().split())) for i in range(100)]

    max_ans = 0
    for i in range(100):
        s_r = 0
        s_c = 0
        s_cross_r = 0
        s_cross_l = 0
        for j in range(100):  # 행, 열, 대각선 2가지의 합 조건들을 모두 for문 하나에 넣음
            s_r += num_list[i][j] # 행의 합
            s_c += num_list[j][i] # 열의 합
            if i == j: # 대각선 오른쪽의 합
                s_cross_r += num_list[i][j]
            if i + j == 99: # 대각선 왼쪽의 합
                s_cross_l += num_list[i][j]
        if max_ans < s_r: # 최대값 구하기
            max_ans = s_r
        if max_ans < s_c:
            max_ans = s_c
        if max_ans < s_cross_r:
            max_ans = s_cross_r
        if max_ans < s_cross_l:
            max_ans = s_cross_l
    print(f'#{test + 1} {max_ans}')
```

------