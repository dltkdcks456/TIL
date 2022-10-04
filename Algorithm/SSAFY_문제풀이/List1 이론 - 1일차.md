# List1 이론 - 1일차

## 문제풀이 Note

### 🔰Gravity

`1` 걸린 시간 :  1시간

`2` 사용한 자료구조 및 개념 : for문, list, max 활용



 💡 문제풀이 아이디어 및 어려웠던 점

- 처음엔 풀지 못 했고, 보경님의 아이디어에 입각해서 품
- 각 라인의 가장 큰값을 확인하며 빈 공간의 개수를 세어준다는 개념으로 접근
- 논리적으로 해결하는 방법을 생각하지 못함.

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys

sys.stdin = open('input_Gravity.txt')

T = int(input())                                    # 테스트 케이스

for i in range(T):                                  # for문을 통해 입력값을 받음
    total_area = int(input())
    num_list = list(map(int, input().split()))

    max_cnt = 0                                     # 가장 멀리 떨어지는 낙차 값의 초기값

    for num in range(total_area - 1):               # 각 라인 마다 비교 진행
        fall = 0
        for other in range(num + 1, total_area):    # 다른 라인보다 크다면 1칸의 낙차가 허용되므로 1을 추가
            if num_list[num] > num_list[other]:
                fall += 1
        if fall > max_cnt:                          # 각 라인별 낙차를 구하고 최대값을 구함
            max_cnt = fall
    print(f'#{i + 1} {max_cnt}')
```

------

### 🔰Baby gin

`1` 걸린 시간 : 1시간 30분

`2` 사용한 자료구조 및 개념 : for, while, 각종 논리에 입각한 조건들



 💡 문제풀이 아이디어 및 어려웠던 점

- while을 이용해 break를 어떤 식으로 걸어줘야하는지에서 헷갈림
- 순열을 통해 완전 탐색을 활용하지 않고, 카운트를 하는 방식으로 구함
- triplet을 먼저 해주어야 해당 조건들이 성립이 가능

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys
sys.stdin = open('input_Baby gin.txt')

T = int(input())

for test in range(T):                   # 테스트 케이스
    cnt = [0] * 12                      # 숫자 개수를 담을 리스트
    run = triplet = 0                   # run과 triplet의 수

    number = input()
    for j in number:
        cnt[int(j)] += 1                # 각각의 숫자에 대해 카운트 진행

    for k in range(len(cnt)):           # triplet인 경우에 해당하는 조건문
        while cnt[k] >= 1:
            if cnt[k] >= 3:
                cnt[k] -= 3
                triplet += 1
                continue

            if cnt[k] >= 1 and cnt[k + 1] >= 1 and cnt[k + 2] >= 1:  # run에 해당하는 조건문
                cnt[k] -= 1
                cnt[k + 1] -= 1
                cnt[k + 2] -= 1
                run += 1
                continue

            else:                       # 그 어느 것에도 만족하지 않을 시 break 진행
                break

    if (run + triplet) * 3 == len(number):  # 총 6개의 카드이므로 run, triplet의 합과 3을 곱하면 6이된다
        print(f'#{test + 1} 1')
    else:
        print(f'#{test + 1} 0')             # 해당 조건 불만족 시 0 출력
```

------

### 🔰1206 - View

`1` 걸린 시간 :  20분

`2` 사용한 자료구조 및 개념 : for와 각종 조건문

💡 문제풀이 아이디어 및 어려웠던 점

- 양쪽에 있는 빌딩의 높이를 활용하여 문제를 풀면 쉽게 해결이 가능

> **Solution Code & 주석**

```python
#  솔루션 코드를 작성합니다.
import sys

sys.stdin = open('input_1206_swea')

for _ in range(10):                             # 10번의 테스트 진행
    row = int(input())                          # 건물이 들어설 수 있는 거리 길이
    building = list(map(int, input().split()))  # 건물의 층수

    ans = 0                                     # 조망권이 확보된 건물
    for each in range(2, row - 2):
        l_2 = building[each - 2]                # 왼쪽 2번 째부터 오른쪽 2번 째까지의 건물 높이
        l_1 = building[each - 1]
        r_1 = building[each + 1]
        r_2 = building[each + 2]
																                # 양쪽 건물들보다 높아야 조망권 확보가 가능
        if building[each] > l_2 and building[each] > l_1 and building[each] > r_1 and building[each] > r_2:
            ans += building[each] - max([l_2, l_1, r_2, r_1]) # 가장 높은 빌딩과의 차이를 합해줌
    print(f'#{_ + 1} {ans}')
```

------