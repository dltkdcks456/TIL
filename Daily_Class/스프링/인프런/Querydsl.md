# Querydsl

- 쿼리를 자바 코드로 작성

- 문법 오류를 컴파일 시점에
- 동적 쿼리 작성
- 쉬운 SQL 스타일 문법

![image-20230411201622313](assets/image-20230411201622313.png)

> Native 쿼리는 컴파일 시점에서 오류를 알 수가 없다. 위쪽에는 m뒤에 공백이 필요하다.

![image-20230411201718189](assets/image-20230411201718189.png)

> 자바 컴파일러가 오류를 잡아준다. 자바이기 때문에. 코드 자동완성의 도움을 받을 수 있다. `.`을 찍어주면 알 수 있다.



### 실습 시작하기

- 스프링 부트 스타터(https://start.spring.io/)

![image-20230411202234951](assets/image-20230411202234951.png)

> H2 Database는 DB없이 메모리상에서 만들어주는 장점이 있다.
>
> 기본적인 Dependencies를 적어준다

- java version을 잘 맞춰준 후에 build.gradle을 실행해서 다운 받아준다.
- 빌드가 끝난 후에는 test -> java 로 들어가서 테스트를 한번 실행해서 동작하는지 확인한다.

![image-20230411204044481](assets/image-20230411204044481.png)

> Gradle이 위임받아서 실행하기 때문에 실행 속도가 굉장히 느리다. gradle 세팅을 위와 같이 바꾸면 훨씬 빠르게 진행이 가능하다.



### Lombok 세팅 필요

- setting에 플러그인 설치

![image-20230411220547835](assets/image-20230411220547835.png)



- Annotation Processors에서 Enable을 꼭 해야 lombok 활성화 된다.

![image-20230411220635496](assets/image-20230411220635496.png)