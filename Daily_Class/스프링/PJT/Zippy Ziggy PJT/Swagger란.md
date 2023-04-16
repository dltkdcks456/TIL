### 📌 Swagger란?

- OAS(Open Api Specification)를 위한 프레임워크
- 개발자들의 필수 과제인 API 문서화를 쉽게 할 수 있도록 도와주며, 파라미터를 넣어서 실제로 어떤 응답이 오는지 테스트 가능
- 협업하는 클라이언트 개발자들에게도 Swagger만 전달해주면 API Path와 Request, Response값 및 제약 등을 한번에 알려줄 수 있다.

### 💡 OpenAPI와의 관계

- https://swagger.io/blog/api-strategy/difference-between-swagger-and-openapi/ 를 보면 Swagger와 OpenAPI의 차이가 나와 있다.
- OpenAPI는 RESTful API 설계를 위한 업계 표준 사양을 나타내고 Swagger는 SmartBear 도구 세트를 나타낸다
- Swagger는 이제 OpenAPI 사양을 구현하기 위한 도구 세트(Swagger Editor, Swagger UI, Swagger Hub)가 되었다.

### 📑 Swagger 적용 방법

1. 의존성 추가
   - 2.x 버전과 다르게 `springfox-boot-starter` 하나만 추가하면 하위에 필요한 모든 라이브러리가 포함되어 있다.

```java
/* build.gradle */

dependencies {
    // ..
    implementation 'io.springfox:springfox-boot-starter:3.0.0'
    // ..
}
```

1. Config 추가

```java
@Configuration
public class SwaggerConfig {

    @Bean
    public Docket api() {
        return new Docket(DocumentationType.OAS_30)
                .useDefaultResponseMessages(false)
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.springswagger.controller"))
                .paths(PathSelectors.any())
                .build()
                .apiInfo(apiInfo());
    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("Practice Swagger")
                .description("practice swagger config")
                .version("1.0")
                .build();
    }
}
```

- `Docket`: Swagger 설정의 핵심이 되는 Bean
- `useDefaultResponseMessage`: Swagger에서 제공해주는 기본 응답코드(200, 401, 403, 404). false로 설정하면 기본 응답 코드를 노출하지 않음
- `apis`: api 스펙이 작성되어 있는 패키지(Controller)를 지정
- `paths`: apis에 있는 API중 특정 path를 선택
- `apiInfo`: Swagger UI로 노출할 정보

### 🛠 Controller에 적용

```java
@RestController
public class HelloController {

    @Operation(summary = "test hello", description = "hello api example")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "OK !!"),
            @ApiResponse(responseCode = "400", description = "BAD REQUEST !!"),
            @ApiResponse(responseCode = "404", description = "NOT FOUND !!"),
            @ApiResponse(responseCode = "500", description = "INTERNAL SERVER ERROR !!")
    })
    @GetMapping("/hello")
    public ResponseEntity<String> hello(@Parameter(description = "이름", required = true, example = "Park") @RequestParam String name) {
        return ResponseEntity.ok("hello " + name);
    }
}
```

### 💻 실행 후 접속

- Swagger2: http://localhost:8080/swagger-ui.html
- Swagger3: http://localhost:8080/swagger-ui/index.html

### Reference

- https://bcp0109.tistory.com/326
- https://github.com/springfox/springfox
- https://springfox.github.io/springfox/docs/current/