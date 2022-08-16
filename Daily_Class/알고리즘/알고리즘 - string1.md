### 패턴 매칭에 사용되는 알고리즘

- 카프-라빈 알고리즘
  - 미리 준비한 Hash table을 통해 패턴의 연산값을 구함
  - Hash 값이 일치하는 Window를 찾음
  - 그 후 Brute Force를 통해 일치하는 값을 도출
- KMP 알고리즘
  -  틀린 부분의 앞쪽에 대한 히스토리를 통해 반복되는 부분을 기준으로 다시 패턴을 찾음
  - 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함
  - LPS(Longest Prefix & Suffix): 접두어, 접미사
  - a, b, c, a, b, d
  - Mismatch가 된 pattern의 문자(char)의 한 칸 앞 pattern char의 반복 정보를 읽는다.
  - C T C A C T G C C T G C C T A G
  - C T G C C T A G -> G의 앞 T에 대한 LPS 정보를 읽어보고 해당 인덱스로 이동!
  -    C T  G C C T A G -> 이렇게 계속 이동하면서 진행
  - LPS = [0, 0, 0, 1, 1, 2, 0, 0]



## 글자수

- from collections import defaultdict
- 딕셔너리로 풀어보기
- 바이어-무어로 풀어보기

## 회문 2

- for, else구문은 for문이 break없이 다 정상 진행되게 되면 else 진행

