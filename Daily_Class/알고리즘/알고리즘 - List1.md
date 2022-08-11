# 알고리즘(List1)

### 알고리즘

- 문제를 해결하기 위한 절차나 방법, 주로 컴퓨터용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말함.

- 의사코드(슈도코드)와 순서도 2가지로 표현

- 정확성, 작업량, 메모리 사용량, 단순성, 최적성

### 시간 복잡도(Time Complexity)

- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산

- 빅-오(O) 표기법

### 정렬의 종류

- 버블 정렬(Bubble Sort)
- 카운팅 정렬(Counting Sort)
- 선택 정렬(Selection Sort)
- 퀵 정렬(Quick Sort)
- 삽입 정렬(Insertion Sort)
- 병합 정렬(Merge Sort)

### 버블 정렬

- 인접한 요소들을 비교하여 정렬하는 법
- O(N^2)의 시간 복잡성을 가진다

```python
a = [3, 300, 240, 6000, 1, -3, -77]
for i in range(len(a) - 1, 0, -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
```

### 카운팅 정렬

- 순서를 결정하기 위해 항목의 개수를 세어서 선형 시간에 정렬하는 효율적인 알고리즘
- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
- 집합 내의 가장 큰 정수를 알아야 한다.
- 시간 복잡도: O(n + k), n은 리스트 길이, k는 정수의 최대값

```python
a = [20, 15, 12, 15, 5, 9]
cnt = [0 for i in range(max(a) + 1)]
result = [0 for j in range(len(a))]

for i in a:
    cnt[i] += 1

for j in range(1, len(cnt)):
    cnt[j] = cnt[j] + cnt[j - 1]

for k in range(len(a) - 1, -1, -1):
    cnt[a[k]] -= 1
    result[cnt[a[k]]] = a[k]

print(result)
```

- 안정 정렬을 위해서 뒤쪽부터 데이터를 읽어나간다

  - 본래 순서를 유지하기 위해서

  - (4, 1),  (4, 2) 처럼 해당 순서를 그대로 유지하기 위해서 그렇게 한다

```python
# 최대값의 위치, 같은 값이 있을 때는 맨 오른쪽
# 9
# 7 4 2 0 0 6 0 7 0

N=int(input())
arr = list(map(int, input().split()))
maxId = 0 #가정
for i in range(1, N):
    if arr[maxIdx] <= arr[i]: #등호가 없으면 제일 왼쪽, 등호를 선택하면 제일 오른쪽
        maxIdx = i
```

- 각 자리수의 추출

```python
# 자릿수를 각각 추출하는 경우
a = 123456
num = [0] * 10
while a > 0:
    num[a % 10] += 1
    a //= 10
print(num)
```

- Baby Gin

```python
n = list(map(int, input()))
i = 0
cnt = [0] * 10
run = triplet = 0

for j in n:
    cnt[j] += 1
    
while i < 10:
    if cnt[i] >= 3:
        cnt[i] -= 3
        triplet += 1
        continue

    if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:
        cnt[i] -= 1
        cnt[i + 1] -= 1
        cnt[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + triplet == 2:
    print('Runtriplet')
else:
    print('Lose')
```

