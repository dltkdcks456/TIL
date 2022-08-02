# CSS

- CSS는 HTML과 함께 어우러져 사용
- 인라인
- 내부참조
  - h1이 선택자(selector)
- 주로 외부참조를 사용, 똑같은 템플릿을 활용하기 위해

### CSS 적용 우선순위

!important > 인라인 > id > class > 요소

- viewport 개념 활용

- em, rem도 쓰게 됐다

- 똑같은 depth를 가지면 자식이 없다. 형제

- class 구역을 정해줌

### box model

- padding -> background color
- margin -> border 바깥



- html의 주석은 `<!-- -->`
- CSS의 주석은 `/* */`



# Homework

- user agent style

- 브라우저마다 적용된 스타일은 다르다

# workshop

- `div#ssafy`하면 emmit이 id를 완성하도록 도와준다
- `div.ssafy`도 동일

- `Ctrl + Enter`클릭하면 바로 다음 줄로 이동

- `Ctrl + Alt`하면 동시에 작성 가능
- `Alt` 클릭하면 여러개 동시 작성 가능
- `Alt + Shift`를 누르면 복사가 된다
- `Alt` 화살표는 해당 줄을 옮긴다.



# Homework

- placeholder는 입력하면 사라짐

# Practice

- float는 화면을 나누는 것
- clearfix

# workshop

- relative 상대좌표를 이용해 다른 것들을 또 포지션 시킴
- %를 활용하면 해당 픽셀의 퍼센트만큼 화면 보여줌
- display는 기본적으로 block

#### problem 05

- margin: 위로 100px 좌,우는 auto 아래는 500px

- 형제지간이며 small-box라는 스타일링 진행

```html
#red{
position: relative;
left: 400px;
top: 400px;
}
position: absolute;
top: 400px;
left: 400px;

#gold {
position: fixed;
bottom: 50px;
right: 50px;
}

#green {
position: absolute;
top: 200px;
right: 200px;
}

#blue {
position: absolute;
top: 100px
left: 100px
}
```

#### problem 6

```html
container {
width: 1200px
margin:200px auto;  #상하 200px 띄우고, 좌우는 auto;
}


```

