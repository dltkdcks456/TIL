# Web

- CSS layout techniques
  - Display
  - Position
  - Float(CSS1, 1996)
  - Flexbox(2012)
  - Grid(2017)

- Inline Direction(글자)
- Block Direction

### Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping하도록 함
- 요소가 Normal flow를 벗어나도록 함
  - none: 기본값
  - left: 요소를 왼쪽으로 띄움
  - right: 요소를 오른쪽으로 띄움
- clearfix를 활용하면 float를 초기화시켜줌.

### Flexible Box Layout

- Inline처럼 변형
  - 내용물의 크기만큼만 차지

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - main axis(메인 축)
  - cross axis(교차 축)
- 구성 요소
  - Flex Container (부모 요소)
  - Flex Item(자식 요소)

# Bootstrap

- Spacing(Margin and padding)
  - {property}{sides}-{size}
    - t - top
    - b - bottom
    - s - left
    - e - right
    - x - left, right
    - y - top, bottom
    - blank - 4 sides

- script는 용량이 커서 제일 뒤에 넣고 동작시킨다.
  - JS는 데이터를 조작, 새로운 html생성을 담당하기 때문에 작동하는 것부터 화면에 보여주자는 의미로 script는 바디 위에 적는다
  - 