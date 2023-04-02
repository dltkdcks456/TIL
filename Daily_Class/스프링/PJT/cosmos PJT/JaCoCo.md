# JaCoCo

- JaCoCo(Java Code Coverage) 자바 코드 커버리지를 체크하는 데 사용되는 오픈소스 라이브러리

  - JaCoCo의 특징
    - Line, Branch Coverage를 제공한다
    - 코드 커버리지 결과를 파일 형태로 저장할 수 있다.
      - html, xml, csv 등으로 Report를 생성한다.
    - 설정한 커버리지 기준을 만족하는지 확인할 수 있다.
      - 설정한 커버리지 기준을 만족하지 못할 경우 빌드하지 못하도록 막을 수 있습니다.

- ```
  build.gradle
  ```

   설정 사항

  - excludes를 통해 원하지 않는 클래스를 제외할 수 있다
  - Report에서도 제외를 하여 커버리지 퍼센트를 올릴 수 있다.

```java
jacoco {
    toolVersion = "0.8.7"
    reportsDirectory = layout.buildDirectory.dir('customJacocoReportDir')
}

jacocoTestReport {
    reports {
        xml.required = false
        csv.required = false
        html.outputLocation = layout.buildDirectory.dir('jacocoHtml')
    }
}

jacocoTestCoverageVerification {
    def Qdomains = []

    for (qPattern in '*.QA'..'*.QZ') { // qPattern = '*.QA', '*.QB', ... '*.QZ'
        Qdomains.add(qPattern + '*')
    }

    violationRules {
        rule {
            enabled = true
            element = 'CLASS'

            limit {
                counter = 'LINE'
                value = 'COVEREDRATIO'
                minimum = 0.00
            }

            limit {
                counter = 'BRANCH'
                value = 'COVEREDRATIO'
                minimum = 0.00
            }

            excludes = [
//                    '*.KakaoProfile*',
//                    '*.Jwt*',
//                    '*/model*'
            ] + Qdomains // 제외할 Qdomains 패턴 추가
        }
    }
}

test {
    finalizedBy jacocoTestReport // test 작업이 끝나고 jacocoTestReport를 실행
    useJUnitPlatform()
}

jacocoTestReport {
    reports {
        html.enabled true
        csv.enabled true
        xml.enabled false
    }

    def Qdomains = []

    for (qPattern in '**/QA'..'**/QZ') { // qPattern = '**/QA', '**/QB', ... '*.QZ'
        Qdomains.add(qPattern + '*')
    }

    // 여기부터
    afterEvaluate {
        classDirectories.setFrom(
                files(classDirectories.files.collect {
                    fileTree(dir: it, excludes: [
//                            '**/KakaoProfile*',
//                            '**/Jwt*',
//                            '**/model*'
                    ] + Qdomains)
                })
        )
    }

    finalizedBy 'jacocoTestCoverageVerification'
    dependsOn test // jacocoTestReport 에 test라는 종속성을 추가
}
```

- 커버리지에서 제외할 수 있는 커스텀 

  ```
  Annotation
  ```

   생성

  - 원하지 않는 클래스 위해 `@Generated` 를 붙이면 테스트에서 제외가 가능하다.

- https://recordsoflife.tistory.com/1016