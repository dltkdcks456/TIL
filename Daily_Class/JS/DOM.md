### DOM

- HTML, CSS를 조작하기 위해서 객체로 잡아서 구조화 시키는 것이 DOM (tag, 속성, 내용)

- ES 6+ 이후부터는 queryselect(Node list가 리턴)
  - getElement by는 옛날 코드(collect 객체를 리턴)

- innerText와 innerHTML이 존재
  - innerHTML = "<h1>제목</h1>" -> 사이트 공격이 가능해서 innerText가 더 낫다.
- append()는 부모-자식을 따지지 않고 그냥 추가
  - appendChild()가 구조적으로 안정적이다. 
- Event
  - 선택하지 않고 태그 안에 함수가 모두 작성될 수 있으나, 재사용성이 어렵고 코딩이 지저분해진다.
- form tag활용 시 preventDefault()를 활용해 해당 작동을 중지할 수 있다.

- DOM의 각 객체들은 node로 불리고 요소는 element, 그 내용은 content node이며 그 둘은 부모/자식관계이다. class와 style은 요소와 관련된 attribute node라고 한다.