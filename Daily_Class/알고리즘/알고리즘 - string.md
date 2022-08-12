# 문자열

- ASCII 코드의 발전은 미국을 기준으로 발전
- 한글은 조합형과 완성형 2가지가 존재
  - 완성형이 2byte를 사용하므로 효율적

- 다국어 표현을 처리하기 위해 유니코드를 탄생시킴!

- 슬라이싱은 얕은 복사

```python
text = 'algorithm'
# 방법 1 ... x
text1 = ''
for i in text:
    text1 = i + text1
print(text1)

# 방법 2
print(text[-1::-1])
print(text[::-1])

# 방법 3
text2 = list(text)
for j in range(len(text2) // 2):
    text2[j], text2[- j - 1] = text2[- j - 1], text2[j]
print(''.join(text2))

# 방법 4
list1 = list(text)
list1.reverse()
print(*list1, sep='')

# 방법 5
reverse_s = ''
for idx in range(len(text) - 1, -1, -1):
    reverse_s += text[idx]
print(reverse_s)
```

```python
# 문자를 정수로 변환
def atoi(s): #문자를 정수로 변환
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i
print(atoi('123'))
```

```python
# 정수를 문자로 변환
def itoa(s):
    text = ''
    if s != 0:                              # s가 0이 아닌 경우
        minus = False                       # minus 판별 변수
        if s < 0:                           # s가 음수일 경우
            minus = True                    # minus를 인식 후 True
            s = -s                          # 양수 변환
        while s > 0:                        # 자리수마다 문자화진행
            plus = chr(s % 10 + ord('0'))   # 10을 나누어 1의 자리를 아스키코드를 통해 문자로 변환
            text = plus + text              # 출력할 결과값에 문자 추가
            s = s // 10                     # 그 다음 자리수로 가기 위한 변수값 갱신
        if minus == True:                   # minus일 경우 아스키코드를 통해 - 붙여줌
            text = chr(ord('-')) + text
        return text
    else:
        text = chr(ord('0'))                # 0일 경우 따로 아스키코드로 문자화 진행
        return text                         # 위 조건에서 0이 포함되면 while의 반복문을 빠져나오지 못함

i = 0                                       # 테스트 케이스 출력 변수
while True:                                 # itoa 함수에 값 입력해주기
    try:                                    # Input이 들어올 때 연산 후 출력
        N = int(input())
        print(f'#{i + 1} {itoa(N)} {type(itoa(N))}')
        i += 1
    except:                                 # Input이 없을 시 while문 종료
        break
```

<hr>

### 패턴 매칭

text.count(), text.index(), chr in text

- Brute-Force Method(완전 탐색)

```python
source = "This is a book~!"
pattern = "is"
def BruteForce(pattern, source):
    for idx in range(len(source) - len(pattern) + 1):
        for j in range(len(pattern)):
            if source[idx + j] != pattern[j]:
                break
        else:
            return idx
    else:
        return -1
print(BruteForce(pattern, source))
```

### 보이어-무어 알고리즘

- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 오른쪽에서 왼쪽으로 비교

### 연습문제

- 딕셔너리 활용해보기(GNS)