# List1 실습 - 2일차

## 문제풀이 Note

### 🔰4831 - 전기버스

`1` 걸린 시간 : 15분

`2` 사용한 자료구조 및 개념 : for, while, if문



 💡 문제풀이 아이디어 및 어려웠던 점

- 총 거리에서 충전소가 꼭 필요한 지점까지로 범위 제한
- 충전소 찾기 실패 시 while문 탈출과 cnt 초기화 진행

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('전기버스.txt')

T = int(input())
for test in range(T):
    K, N, M = map(int, input().split())             # 변수 설정
    charge = list(map(int, input().split()))        # 충전소 장소

    N_list = [True] + [False] * (N - 2) + [True]    # 충전기 위치 표시

    for _ in charge:                                # 추가 충전기 위치 추가
        N_list[_] = True

    i = 0                                           # 초기 위치
    cnt = 0                                         # 총 충전 개수

    while i < N - K:                                # 충전기가 필요한 최대 범위
        for j in range(K, 0, -1):                   # 해당 위치에서부터 갈 수 있는 가장 먼 위치부터 충전소 확인
            if N_list[i + j] == True:               # 충전소를 찾으면 해당 인덱스를 불러오고 개수 1 증가
                i = i + j
                cnt = cnt + 1
                break
            elif j == 1:                            # 충전소를 끝까지 못 찾았을 경우, while문 탈출과 cnt를 0으로 초기화
                i = N
                cnt = 0

    print(f'#{test + 1} {cnt}')
```

------

### 🔰4828 - min_max

`1` 걸린 시간 :  10분

`2` 사용한 자료구조 및 개념 : for



 💡 문제풀이 아이디어 및 어려웠던 점

- 수업 내용과 동일하여 풀이가 쉬움

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('min_max.txt')

T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))          # 리스트와 변수 설정

    max = min = num_list[0]                             # min, max를 리스트의 가장 첫 번째 요소로 설정

    for num in num_list:                                # 각 값을 비교하면서 max와 min 찾기
        if num > max:
            max = num
        elif num < min:
            min = num

    print(f'#{test + 1} {max - min}')
```

------

### 🔰4834 - cards

`1` 걸린 시간 : 10분

`2` 사용한 자료구조 및 개념 : for, if



<aside> 💡 문제풀이 아이디어 및 어려웠던 점

- 수업시간의 카운트 정렬과 엇비슷한 맥락

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('cards.txt')

T = int(input())
for test in range(T):                       # 변수 설정
    N = int(input())
    a = list(map(int, input()))
    cards = [0] * 10

    for card in a:                          # 중복된 숫자 개수 세기
        cards[card] = cards[card] + 1

    max_cnt = 0                             # 숫자의 개수와 값을 변수 설정
    max_num = 0
    for num, cnt in enumerate(cards):       # cards 내부의 리스트를 확인하면서 index와 값을 비교 후 최대 추출
        if cnt > max_cnt:
            max_cnt = cnt
            max_num = num
        elif cnt == max_cnt and num > max_num:
            max_num = num

    print(f'#{test + 1} {max_num} {max_cnt}')
```

------

### 🔰4835 - 구간합

`1` 걸린 시간 : 15분

`2` 사용한 자료구조 및 개념 : for, if



💡 문제풀이 아이디어 및 어려웠던 점

- 수업과 동일한 문제

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.

import sys
sys.stdin = open('구간합.txt')

T = int(input())
for test in range(T):                           # 변수 설정
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = []

    for i in range(len(a) - M + 1):             # 더할 수 있는 개수만큼을 제외한 범위
        sum_num = 0
        for j in range(M):
            sum_num = sum_num + a[i + j]        # 더해야하는 개수만큼 더해감
        sum_a.append(sum_num)

    max_a = min_a = sum_a[0]

    for k in sum_a:                             # 찾은 합에서 min, max 찾기
        if k > max_a:
            max_a = k
        elif k < min_a:
            min_a = k

    print(f'#{test + 1} {max_a - min_a}')
```

------

### 🔰1208 - flatten

`1` 걸린 시간 : 20분

`2` 사용한 자료구조 및 개념 : for, if



💡 문제풀이 아이디어 및 어려웠던 점

- 양쪽에서 min과 max를 찾아오도록 구현함(while 사용)
- 조건에 주어진 값을 활용

> **Solution Code & 주석**

```python
import sys
sys.stdin = open('Flatten.txt')

for test in range(10):                                  # dump, box 변수 입력
    dump = int(input())
    box = list(map(int, input().split()))
    height = [0] * 101                                  # 최대 높이가 100이므로 0부터 100까지 높이 지정

    for j in box:
        height[j] = height[j] + 1                       # box에 입력된 값들을 세어서 추가한다

    start = 0                                           # height 리스트의 첫 시작점
    end = 100                                           # height 리스트의 끝점
    cnt = 0

    while cnt <= dump:                                  # dump의 개수가 될 때까지 실행
        while height[start] == 0:                       # 값이 나타나는 start 출력
            start = start + 1

        while height[end] == 0:                         # 값이 나타나는 end 출력
            end = end - 1

        if height[start] >= 1:                          # 가장 낮은 값이 0이 될 때까지 뺄셈 진행
            height[start] = height[start] - 1
            height[start + 1] = height[start + 1] + 1

        if height[end] >=1:                             # 가장 높은 값이 0이 될 때까지 뺄셈 진행
            height[end] = height[end] - 1
            height[end - 1] = height[end - 1] + 1

        if end - start <= 1:                            # break 필요
            break

        cnt = cnt + 1                                   # 덤프 진행 시 1 추가

    print(f'#{test + 1} {end - start}')
```

------

### 🔰5789 - 현주의 상자 바꾸기

`1` 걸린 시간 : 15분

`2` 사용한 자료구조 및 개념 : for



 💡 문제풀이 아이디어 및 어려웠던 점

- 중복 for 문을 활용하여 list를 계속해서 갱신

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.

import sys
sys.stdin = open('현주의 상자 바꾸기.txt')

T = int(input())
for test in range(T):
    N, Q = map(int, input().split())        # N, Q 변수 받기
    N_list = [0] * (N + 1)

    for i in range(1, Q + 1):
        L, R = map(int, input().split())    # L, R 변수 받기
        for j in range(L, R + 1):
            N_list[j] = i                   # 해당 범위를 i값으로 동일하게 변경

    print(f'#{test + 1}', *N_list[1:])
```

------

### 🔰6485 - 삼성시의 버스노선

`1` 걸린 시간 : 20분

`2` 사용한 자료구조 및 개념 : for, if



 💡 문제풀이 아이디어 및 어려웠던 점

- 카운트를 활용하여 문제 해결

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('삼성시의 버스 노선.txt')

T = int(input())

for test in range(T):
    N = int(input())                                # 버스 노선의 개수
    lines = [0] * 5001                              # 총 버스 라인
    for _ in range(N):
        A, B = map(int, input().split())            # 범위 입력 받기
        for line in range(A, B + 1):
            lines[line] = lines[line] + 1           # 해당 라인 내 개수 1 증가

    P = int(input())
    input_list = []                                 # 출력할 정류장 번호

    for i in range(P):
        input_list.append(int(input()))

    print(f'#{test + 1}', end = ' ')

    for j in input_list:
        print(f'{lines[j]}', end = ' ')
```

------

### 🔰1945 - 간단한 소인수분해

`1` 걸린 시간 : 25분

`2` 사용한 자료구조 및 개념 : for, if, while



 💡 문제풀이 아이디어 및 어려웠던 점

- while 조건문을 작성하기가 까다로움
- print하는 것도 생각보다 어려웠음

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('간단한 소인수분해.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    num_list = [0] * 12                         # 소수의 카운트할 범위
    for i in range(2, N):
        if N != 1:                              # 소인수분해 완료 시점까지
            while N % i == 0:                   # 약분이 더 이상 되지 않을 때
                if N % i:
                    break
                else:
                    N = N // i                  # 약분이 진행되고 해당 소수를 셈
                    num_list[i] += 1
        else:
            break

    prime = [2, 3, 5, 7, 11]                    # 우리가 원하는 소수의 지수를 구함
    print(f'#{_ + 1}', end = ' ')
    for j in prime:
        print(num_list[j], end = ' ')
    print()
```

------