# Git

### 분산 버전 관리 프로그램

- 코드의 히스토리를 관리하는 도구
- 개발되어온 과정 파악이 가능
- 이전 버전과의 변경 사항 비교 및 분석

- Repository
  - 특정 디렉토리를 버전 관리하는 저장소

```txt
git init: git 생성
touch readme.md: 리드미 생성
ls: 목록 확인
git status: 깃 상태 확인
git add . :모든 파일을 staging area에 올리겠다
git rm --cached readme.md: staging area에 올라간 파일을 제거
git commit -m message: commit 진행해서 repository에 저장
code .: vscode로 띄어진다
mkdir:폴더 만들기
touch a.txt: touch는 폴더 만들기
git restore 파일명: 수정 취소할 때
git log --oneline : 깃의 이력 확인
git log:를 치면 다 알 수 있음.
git remote add origin master: 끝 단어 둘다 개발자가 만들어서 씀. local을 Github과 연결
git push -u origin master: orgin은 repo_name 그리고 master는 local branch이다
git clone 으로 repo를 불러옴
:q -> shift 콜론 q를 하면 나와짐
```

- Working Directory: 내가 작업하고 있는 실제 디렉토리
- Staging Area: 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
- Repository: 커밋들이 저장되는 곳

- git이 추적되지 않으면 untracked라고 함

- commit을 하면 고유 아이디가 생성된다.

- HEAD는 깃발에 가깝다 --> master는 branch의 의미

  - master로 기본값이 되어있는데 요즘은 main으로 이름을 만듦

  - 어느 commit에 깃발을 꽂고 어떤 branch가 잇는가



### Git Advanced

- Git undoing
  - Git으로 했던 작업들을 되돌리기(Undoing)
  - 되돌리는 단계는 크게 세 가지로 분류
    - Working Directory 작업 단계
    - Staging Area 작업 단계
    - Repository 작업단계
- Working Directory 작업 단계
  - Working Directory에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
  - git restore
- Staging Area 작업 단계
  - Staging Area에 반영된 파일을 Working Directory로 되돌리기
  - git rm --cached
  - git restore --staged
- Repository 작업 단계
  - 커밋을 완료한 파일을 Staging Area 로 되돌리기
  - git commit --amend

![image-20221028101457518](Git.assets/image-20221028101457518.png)

![image-20221028101526412](Git.assets/image-20221028101526412.png)

![image-20221028101854517](Git.assets/image-20221028101854517.png)

![image-20221028102228092](Git.assets/image-20221028102228092.png)

![image-20221028102256177](Git.assets/image-20221028102256177.png)

![image-20221028102432037](Git.assets/image-20221028102432037.png)

![image-20221028102454719](Git.assets/image-20221028102454719.png)

-a는 숨긴 폴더를 보여줌. git까지 없애야 추적이 멈춤.

![image-20221028111553782](Git.assets/image-20221028111553782.png)

![image-20221028103102795](Git.assets/image-20221028103102795.png)

![image-20221028103510732](Git.assets/image-20221028103510732.png)

![image-20221028103606423](Git.assets/image-20221028103606423.png)

![image-20221028103617244](Git.assets/image-20221028103617244.png)

![image-20221028103631750](Git.assets/image-20221028103631750.png)

![image-20221028103701535](Git.assets/image-20221028103701535.png)

![image-20221028103707872](Git.assets/image-20221028103707872.png)

![image-20221028103938661](Git.assets/image-20221028103938661.png)

- VIM 에디터, 수정 모드는 i로, 나올때는 ESC, 콜론을 붙이고 명령어 입력
  저장 w 종료 q(:w)
- 직전 커밋을 덮어쓰고 완전 새로운 커밋을 생성(고유 아이디가 다름)

![image-20221028104350603](Git.assets/image-20221028104350603.png)

- soft는 staging area로 이동, commit 전 다시 commit 할 수 있다.
- mixed working directory로 이동, add하기 전으로 이동, unstaged 상태
- 모두 working directory에서 삭제한다.

![image-20221028104638194](Git.assets/image-20221028104638194.png)

![image-20221028104754265](Git.assets/image-20221028104754265.png)

![image-20221028104832679](Git.assets/image-20221028104832679.png)

![image-20221028104846684](Git.assets/image-20221028104846684.png)

![image-20221028104934971](Git.assets/image-20221028104934971.png)

![image-20221028105531123](Git.assets/image-20221028105531123.png)

![image-20221028112212764](Git.assets/image-20221028112212764.png)

commit이 완료된 파일은 흰색 아니면 초록색이다

![image-20221028112409246](Git.assets/image-20221028112409246.png)

![image-20221028112721668](Git.assets/image-20221028112721668.png)

![image-20221028112904733](Git.assets/image-20221028112904733.png)

![image-20221028113727194](Git.assets/image-20221028113727194.png)

![image-20221028113231829](Git.assets/image-20221028113231829.png)

![image-20221028113905496](Git.assets/image-20221028113905496.png)

![image-20221028114027858](Git.assets/image-20221028114027858.png)

![image-20221028114145454](Git.assets/image-20221028114145454.png)

-r은 remote라는 의미

![image-20221028114344321](Git.assets/image-20221028114344321.png)

### 📛주의사항: 반드시 커밋해야함

![image-20221028114546998](Git.assets/image-20221028114546998.png)

![image-20221028114719423](Git.assets/image-20221028114719423.png)

![image-20221028115506380](Git.assets/image-20221028115506380.png)

![image-20221028115923369](Git.assets/image-20221028115923369.png)

- 그래프를 그려줄 수도 있음

- branch만들고 가지고 있는 branch 확인하기

![image-20221028120045405](Git.assets/image-20221028120045405.png)

- switch로 HEAD 변경하기
- ![image-20221028120220144](Git.assets/image-20221028120220144.png)

- master branch가 login branch보다 1개 commit 앞서 있음

![image-20221028120550161](Git.assets/image-20221028120550161.png)

![image-20221028133434683](Git.assets/image-20221028133434683.png)

![image-20221028133500084](Git.assets/image-20221028133500084.png)

![image-20221028133603637](Git.assets/image-20221028133603637.png)

![image-20221028133613071](Git.assets/image-20221028133613071.png)

![image-20221028133652232](Git.assets/image-20221028133652232.png)

- 모든 브랜치의 모든 커밋을 보고 싶을 때에는 all을 붙여준다.

![image-20221028133915932](Git.assets/image-20221028133915932.png)

- 3개를 공통으로 가지고 분화

![image-20221028134243379](Git.assets/image-20221028134243379.png)

### git Merge

![image-20221028134338075](Git.assets/image-20221028134338075.png)

![image-20221028134558979](Git.assets/image-20221028134558979.png)

![image-20221028134718254](Git.assets/image-20221028134718254.png)

- 커밋의 수는 늘어나지 않는다.

![image-20221028134824444](Git.assets/image-20221028134824444.png)

![image-20221028135759231](Git.assets/image-20221028135759231.png)

![image-20221028140050360](Git.assets/image-20221028140050360.png)

- merge 후에는 병합해준 branch는 삭제해주는 것이 관례

![image-20221028140116172](Git.assets/image-20221028140116172.png)

![image-20221028140151963](Git.assets/image-20221028140151963.png)

![image-20221028140413128](Git.assets/image-20221028140413128.png)

- merge strategy를 search해서 찾아보면 좋음❤
- 새로운 commit을 생성함.

![image-20221028141927814](Git.assets/image-20221028141927814.png)

- 완성후 브랜치 삭제

![image-20221028152842736](Git.assets/image-20221028152842736.png)

![image-20221028153205234](Git.assets/image-20221028153205234.png)

- 대부분 사람이 직접 쳐서 수정을 진행

![image-20221028153634499](Git.assets/image-20221028153634499.png)

![image-20221028153910450](Git.assets/image-20221028153910450.png)

![image-20221028153917231](Git.assets/image-20221028153917231.png)

- 동일한 파일 동일한 코드 수정 시 충돌이 발생

![image-20221028153946569](Git.assets/image-20221028153946569.png)

![image-20221028153952982](Git.assets/image-20221028153952982.png)

![image-20221028154002280](Git.assets/image-20221028154002280.png)

![image-20221028154022773](Git.assets/image-20221028154022773.png)

![](Git.assets/image-20221028154110567.png)

![image-20221028154123473](Git.assets/image-20221028154123473.png)

![image-20221028154130102](Git.assets/image-20221028154130102.png)

## Git workflow

![image-20221028154148886](Git.assets/image-20221028154148886.png)

- django.githup은 클론이 불가능(소유권이 없기 때문에)
- Fork 후 clone은 가능!! → PR로 요청해서 바꿔도 되는지 물어본다.

![image-20221028154448844](Git.assets/image-20221028154448844.png)

![image-20221028155011171](Git.assets/image-20221028155011171.png)

![image-20221028155044147](Git.assets/image-20221028155044147.png)

![image-20221028155105321](Git.assets/image-20221028155105321.png)

![image-20221028155224219](Git.assets/image-20221028155224219.png)

![image-20221028155238396](Git.assets/image-20221028155238396.png)

![image-20221028155247535](Git.assets/image-20221028155247535.png)

![image-20221028155256381](Git.assets/image-20221028155256381.png)

![image-20221028155317333](Git.assets/image-20221028155317333.png)

![image-20221028155334700](Git.assets/image-20221028155334700.png)

![image-20221028155421493](Git.assets/image-20221028155421493.png)

![image-20221028155512038](Git.assets/image-20221028155512038.png)

### 💥<span style = "color:red">github에서 settings에 들어가 collaborator에 아이디를 입력해서 등록 진행!!</span>



### Fork & Pull

![image-20221028173327725](Git.assets/image-20221028173327725.png)

![image-20221028173404117](Git.assets/image-20221028173404117.png)

![image-20221028173532721](Git.assets/image-20221028173532721.png)

![image-20221028173607550](Git.assets/image-20221028173607550.png)

![image-20221028173622166](Git.assets/image-20221028173622166.png)

![image-20221028173631317](Git.assets/image-20221028173631317.png)

![image-20221028173639464](Git.assets/image-20221028173639464.png)

![image-20221028173657342](Git.assets/image-20221028173657342.png)

![image-20221028173704381](Git.assets/image-20221028173704381.png)

![image-20221028173710288](Git.assets/image-20221028173710288.png)

![image-20221028173719912](Git.assets/image-20221028173719912.png)

![image-20221028173725034](Git.assets/image-20221028173725034.png)

![image-20221028173730533](Git.assets/image-20221028173730533.png)

![image-20221028173759182](Git.assets/image-20221028173759182.png)

![image-20221028173825438](Git.assets/image-20221028173825438.png)

![image-20221028173832952](Git.assets/image-20221028173832952.png)

![image-20221028173851700](Git.assets/image-20221028173851700.png)

![image-20221028173902163](Git.assets/image-20221028173902163.png)

![image-20221028173919880](Git.assets/image-20221028173919880.png)

![image-20221028173951496](Git.assets/image-20221028173951496.png)

![image-20221028173959122](Git.assets/image-20221028173959122.png)

![image-20221028174005093](Git.assets/image-20221028174005093.png)

![image-20221028174011980](Git.assets/image-20221028174011980.png)

![image-20221028174033335](Git.assets/image-20221028174033335.png)

![image-20221028174051180](Git.assets/image-20221028174051180.png)

![image-20221028174057433](Git.assets/image-20221028174057433.png)

![image-20221028174136900](Git.assets/image-20221028174136900.png)

![image-20221028174143495](Git.assets/image-20221028174143495.png)