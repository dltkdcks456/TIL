### 기타

- 소스 코드를 작성하고 저장을 누르면 bin에서는 .class 파일이 자동으로 만들어지고 해당 파일을 JVM이 실행시킨다

- Navigator를 누르면 bin파일 또한 볼 수 있다
- encoding 설정을 UTF-8로 바꾸지 않으면 환경이 달라서 깨지는 현상도 발생한다.
- package는 하나의 폴더라고 생각하면 된다. java01.intro는 java01이라는 폴더 안에 intro라는 폴더를 의미



### main method

- 실행 명령인 java를 실행 시 가장 먼저 호출 되는 부분
- 만약, Application 에서 main() 메소드가 없다면 절대로 실행 될 수 없음
- Application의 시작 -> 특정 클래스의 main() 실행
- 형태 (고정된 형태)
  - ctrl + space를 통해서 자동 완성이 생긴다.



### 주석(comment)

- `//` 내용: 해당 기호가 있는 위치부터 그 줄 끝까지 주석처리
- `/*내용*/`: 해당 범위의 내용 주석처리
- `/**내용*/`: Documentation API를 위한 주석 처리

```java
package java01.intro;

public class intro02_Comment {
	public static void main(String[] args) {
		// 기호가 등장한 순간부터 끝까지 해당 줄을 주석 처리
        // 슬래시 두 개를 가장 많이 사용하게 된다.
        // 그 이유는 단축기 때문이다
        // 단축키는 ctrl + /
		
		/*
		 해당 범위를 주석처리 하겠다.
		 */
		
		/**
		 * Documentation API를 위한 주석
		 */
		
		// ↑↑↑ 함수나 클래스를 만들 때 설명을 달 수 있음
	}
}

```



### 출력문

- print -> 한 줄 출력
- println -> 출력하고 줄을 한 번 바꿔준다(ln은 line의 줄인말)
- printf -> print방식에 format을 주겠다.
  - %d: 정수
  - %f: 실수
  - %c: 문자
  - %s: 문자열

```java
package java01.intro;

public class intro03_PrintTest {
	public static void main(String[] args) {
		// 한줄 출력을 해보자.
		// sysout을 입력하고 ctrl+space를 누르면 자동완성이 있다
		// \n을 입력하면 줄을 바꿀 수 있다.
		System.out.print("Hello World\n");
		
		//println을 써보자.
		// ctrl 누른 후 클릭하면 해당 함수의 원본 코드를 볼 수 있다.
		System.out.println("Hello World!!");
		
		// escape문을 활용하여 다른 특수문자를 활용할 수 있다.
		System.out.println("\\\"");
		
		System.out.printf("%d \n", 10); //정수 (10진수)
		System.out.printf("%o \n", 10); //정수 (8진수)
		System.out.printf("%x \n", 10); //정수 (16진수)
		
		
		System.out.printf("%4d\n", 10); //4칸을 확보한 뒤 오른쪽 정렬
		System.out.printf("%-4d\n", 10); //4칸을 확보한 뒤 왼쪽 정렬
		System.out.printf("%04d\n", 10); //4칸을 확보한 뒤 오른쪽 정렬 빈칸은 0을 채움
		
		
		System.out.printf("%f\n", 10.1); // 실수 기본으로 소수 6자리까지
		System.out.printf("%.2f\n", 10.105); // 소수점 둘째자리까지(반올림)
		
		System.out.printf("%s\n", "이상찬"); // 문자열 출력
		System.out.printf("%c\n", 'o'); // 문자 하나는 외따옴표
		
		System.out.printf("안녕하세요, 저는 %s입니다. 제 혈액형은 %c입니다.","이상찬",'o');
		
	}
}

```

