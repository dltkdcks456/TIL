#  List2 실습 - 4일차

## 문제풀이 Note

### 🔰4839 - 이진탐색

`1` 걸린 시간 :  30분

`2` 사용한 자료구조 및 개념 : 이진탐색



<aside> 💡 문제풀이 아이디어 및 어려웠던 점</aside>

- 문제의 조건을 제대로 읽지 않고 수업 시간의 내용으로만 해서 계속 오답 발생

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('이진탐색.txt')

def seartch(total, page):                           # 총 페이지와 찾을 페이지를 입력 시 해당 값을 찾는 데 걸리는 카운트 추출
    start = 1                                       # 시작 페이지
    end = total                                     # 끝 페이지
    cnt = 0                                         # 카운트 초기값
    while start != end:                             # start와 end가 같아지는 시기가 될 때까지
        middle = (start + end) // 2                 # 가운데 값
        if middle == page:                          # 일치
            cnt += 1
            return cnt
        elif middle < page:                         # 중간값보다 페이지 값이 클 경우 start 재설정
            start = middle
            cnt += 1
        else:                                       # 중간값보다 페이지가 작을 경우 end 재설정
            end = middle
            cnt += 1
    else:
        cnt += 1
        return cnt

T = int(input())
for test in range(T):
    total, A, B = map(int, input().split())
    A_cnt = seartch(total, A)
    B_cnt = seartch(total, B)
    if A_cnt > B_cnt:                               # cnt 횟수 비교를 통한 정답 도출
        print(f'#{test + 1} B')
    elif A_cnt < B_cnt:
        print(f'#{test + 1} A')
    else:
        print(f'#{test + 1} 0')
```

------

### 🔰4836 - 색칠하기

`1` 걸린 시간 :  20분

`2` 사용한 자료구조 및 개념 : set의 교집합



<aside> 💡 문제풀이 아이디어 및 어려웠던 점</aside>

- 예전엔 2가지 방식으로 풀었지만 지금이 더 못 푸는 느낌

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('색칠하기.txt')

def color_area(x1, y1, x2, y2, color):                          # 좌표값과 색깔 입력
    diff_x = x2 - x1
    diff_y = y2 - y1
    for i in range(diff_y + 1):                                 # 차이만큼 좌표 생성
        for j in range(diff_x + 1):
            x = x1 + j
            y = y1 + i
            if color == 1:                                      # 색깔에 따라 넣어줄 위치 바꾸기
                R_pos.add((x, y))
            else:
                B_pos.add((x, y))

T = int(input())
for test in range(T):
    N = int(input())
    R_pos = set()
    B_pos = set()
    for i in range(N):                                          # 각각의 경우에 따라 교집합 구함
        x1, y1, x2, y2, color = map(int, input().split())
        color_area(x1, y1, x2, y2, color)
    print(f'#{test + 1} {len(R_pos & B_pos)}')
```

------

### 🔰4837 - 부분집합의 합

`1` 걸린 시간 : 10분

`2` 사용한 자료구조 및 개념 : 부분집합



<aside> 💡 문제풀이 아이디어 및 어려웠던 점</aside>

- 수업 내용과 동일해서 어려운 점은 없었음

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.

import sys
sys.stdin = open('부분집합의 합.txt')

A = [_ for _ in range(1, 13)]                       # 1부터 12까지의 집합
T = int(input())                                    # 테스트 케이스

for test in range(T):                               # 부분집합에 대한 기본정보 입력
    N, K = map(int, input().split())
    개수 = 0

    for i in range(1, 1 << len(A)):                 # A의 총 부분집합(공집합 제외)
        cnt = 0                                     # N 값을 찾기 위한 변수
        Sum = 0                                     # K 값을 찾기 위한 변수
        for j in range(len(A)):                     # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            if i & (1 << j):                        # 이진수 i와 일치되는 위치가 곧 A의 원소를 지칭
                cnt += 1                            # 조건 성립 시 cnt, Sum 진행
                Sum += A[j]
        if cnt == N and Sum == K:                   # cnt와 Sum을 만족하는 부분집합의 개수 카운트
            개수 += 1
    print(f'#{test + 1} {개수}')
==================================================================

import sys
sys.stdin = open('부분집합의 합.txt')

A = [_ for _ in range(1, 13)]
T = int(input())

for test in range(T):                               # 부분집합에 대한 기본정보 입력
    N, K = map(int, input().split())
    subset = [[]]
    cnt = 0

    for i in A:                                     # 부분집합 생성
        for j in range(len(subset)):                # 갱신되는 subset의 인자 수만큼 추가
            subset.append(subset[j] + [i])

    for k in subset:                                # 각 부분집합의 개수와 합으로 조건 확인
        if len(k)  == N and sum(k) == K:
            cnt += 1

    if cnt >= 1:                                    # 조건을 통해 결과값 도출
        print(f'#{test + 1} {cnt}')
    else:
        print(f'#{test + 1} 0')
```

------

### 🔰4843 - 특별한 정렬

`1` 걸린 시간 : 15분

`2` 사용한 자료구조 및 개념 : 양쪽에서 들어오도록 구현



<aside> 💡 문제풀이 아이디어 및 어려웠던 점</aside>

- 문제를 제대로 읽지 않은 문제

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('특별한 정렬.txt')

T = int(input())
for test in range(T):
    N = int(input())
    num_list = sorted(list(map(int, input().split())))      # 오름차순 정리
    new_list = []
    if N % 2:                                               # 홀수 일 때는 가운데에 하나가 남으므로 따로 추가해줌
        for i in range(5):
            new_list.append(num_list[N - 1 - i])
            new_list.append(num_list[i])
        new_list.append(num_list[N // 2])
    else:                                                   # 짝수 일 때는 큰값 작은값 진행
        for i in range(5):
            new_list.append(num_list[N - 1 - i])
            new_list.append(num_list[i])

    print(f'#{test + 1}', end = ' ')
    print(*new_list)
```

------

### 🔰1210 - Ladder1

`1` 걸린 시간 :  3시간

`2` 사용한 자료구조 및 개념 : while과 if



<aside> 💡 문제풀이 아이디어 및 어려웠던 점</aside>

- 사다리를 거꾸로 추적하는 것을 생각하지 못함
- 양쪽의 경계선에서 Index out되는 것을 제대로 잡아내지 못함
- 실수한 이후로 계속 좁은 시야로 해석 진행

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('Ladder.txt')

for _ in range(10):
    test = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    c = [i for i in range(100) if ladder[99][i] == 2][0]            # 아래에서부터 진행
    r = 99                                                          # 마지막 행
    while r > 0:                                                    # 제일 첫 행에 도달할 때까지
        ladder[r][c] += 1                                           # 지나온 자리는 +1로 조건 중복 회피
        if (c + 1) < 100 and ladder[r][c + 1] == 1:                 # 정해진 영역 안에서 오른쪽에 1이 있는지 확인
            c += 1
        elif (c - 1) > -1 and ladder[r][c - 1] == 1:                # 정해진 영역 안에서 왼쪽에 1이 있는지 확인
            c -= 1
        else:
            r -= 1                                                  # 왼쪽, 오른쪽이 없는 경우 상으로 직진
    print(f'#{test} {c}')
```

------

### 🔰2001 - 파리 퇴치

`1` 걸린 시간 : 10분

`2` 사용한 자료구조 및 개념 : 4중 for 문



<aside> 💡 문제풀이 아이디어 및 어려웠던 점</aside>

- 좌표 설정
- 2차원 배열의 활용이 지금은 익숙해짐

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('파리 퇴치.txt')

T = int(input())
for test in range(T):
    N, M = map(int, input().split())                                    # N, M 조건 확인
    num_list = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0                                                            # 최대값 확인용
    for r in range(N - M + 1):                                          # r, c좌표 찾기
        for c in range(N - M + 1):
            sum = 0
            for i in range(M):                                          # M x M만큼 더하기
                for j in range(M):
                    sum += num_list[r + i][c + j]                   
            if maxV < sum:                                              # 최대합 찾기
                maxV = sum
    print(f'#{test + 1} {maxV}')
```

------

### 🔰1966 - 숫자를 정렬하자

`1` 걸린 시간 :  1시간

`2` 사용한 자료구조 및 개념 : 버블 정렬, 선택 정렬



<aside> 💡 문제풀이 아이디어 및 어려웠던 점</aside>

- 구글링 시 버블 정렬에 대한 최적화 아이디어를 얻을 수 있었음
  - 스스로 생각한 것은 아니지만 최적화를 어떻게 시켜야하는지 감을 잡을 수 있었다.
    - while이나 for 문에서 적정 조건을 만족하면 break 시킬 수 있어야 함.

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('1966.swea.txt')

T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    #버블 정렬: 스스로 창조해낸 것..
    for i in range(N):
        for j in range(N - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j + 1], num_list[j] = num_list[j], num_list[j + 1]
    print(num_list)

    #버블 정렬2: 기존 버블 정렬
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j + 1]:
                num_list[j + 1], num_list[j] = num_list[j], num_list[j + 1]
    print(num_list)

    #버블 정렬 최적화1: swap이 있었던 경우는 계속 진행을 하고, swap이 없는 경우가 생기면 바로 종료
    for i in range(N - 1, 0, -1):
        swap = False
        for j in range(i):
            if num_list[j] >= num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swap = True
        if not swap:
            break
    print(num_list)

    #버블 정렬 최적화2: 가장 마지막에 swap한 위치를 기억하고, 버블정렬 범위를 축소 시킴
    end = len(num_list) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                last_swap = i
        end = i
    print(num_list)

    #선택 정렬: 수업시간에 했던 정렬
    for i in range(N - 1):
        Min = i
        for j in range(i + 1, N):
            if num_list[Min] > num_list[j]:
                Min = j
        num_list[i], num_list[Min] = num_list[Min], num_list[i]
    print(num_list)
```

------

### 🔰1979 - 어디에 단어가 들어갈 수 있을까

`1` 걸린 시간 : 30분

`2` 사용한 자료구조 및 개념 : for, if



<aside> 💡 문제풀이 아이디어 및 어려웠던 점

- 행과 열을 구분해서 풀어야한다는 점에서 헷갈리기도 하면서 복잡했음

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.

import sys
sys.stdin = open('1979.어디에 단어가 들어갈 수 있을까.txt')

T = int(input())
for test in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 조건부
    for i in range(N):                      # 행에 대한 조건 확인
        cnt_c = 0
        cnt_r = 0
        for j in range(N):                  # 1이면 cnt를 1씩 증가
            if puzzle[i][j] == 1:
                cnt_c += 1
                if j == N-1:                # 마지막 라인에서 cnt가 1이면 개수 확인 후 종료
                    if cnt_c == K:
                        ans += 1
            else:                           # 해당 자리가 0이면 개수 카운트 후 cnt 0으로 초기화
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

            if puzzle[j][i] == 1:           # 열에 대한 조건문, 위 조건과 대칭
                cnt_r += 1
                if j == N-1:
                    if cnt_r == K:
                        ans += 1
            else:
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
    print(f'#{test + 1} {ans}')
```