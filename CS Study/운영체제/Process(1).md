# Process(1)

- 프로세스의 상태

  - Resource queue(blocked)은 공유 데이터에 접근할 때 일관성을 유지하기 위해 해당 작업이 완료될 때까지 그 다음 작업이 기다림
  - Disk I/O queue(blocked)는 디스크의 작업이 완료될 때까지 작업순서를 기다리고, 완료가 되면 인터럽트를 걸어줘서 CPU를 할당받을 수 있게 Ready queue로 이동하게 된다.
  - keyboard I/O queue(blocked)는 키보드의 입력을 받는 상황을 의미한다.

  - queue들은 운영체제 커널이 Data 영역에 자료구조로 만들어놓고 프로세스 상태를 바꾸면서 관리(ready인 상태는 CPU를 주고, blocked는 주지 않음)

- PCB(Process Control Block)

  - 운영체제가 각 프로세스를 관리하기 위해 프로세스당 유지하는 정보
  - 구성 요소
    - OS가 관리상 사용하는 정보
      - Process state(ready, blocked ...), Process ID
      - scheduling information, priority(우선 순위의 정보를 넣음)
    - CPU 수행 관련 하드웨어 값
      - Program counter, registers
    - 메모리 관련
      - Code, data, stack의 위치 정보(메모리의 어디에 위치하는지)
    - 파일 관련
      - Open file descriptors...

- 문맥 교환(Context Switch)

  - CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정
  - CPU가 다른 프로세스에게 넘어갈 때 운영체제는 다음을 수행
    - CPU를 내어주는 프로세스의 상태를 그 프로세스의  PCB에 저장
      - Memory Map, Program Counter, register 정보를 저장(커널의 Data 메모리 공간)
    - CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴

- System call이나 Interrupt 발생시 반드시 context switch가 일어나는 것은 아님
  - 사용자 프로세스부터 운영체제로 넘어가는 것은 문맥 교환이 아니고, 사용자 프로세스 간의 이동을 의미한다.
  - 자신의 필요로 시스템콜을 요청하고 다시 자신으로 돌아올 경우 문맥교환이 일어나지 않음
    - 약간의 문맥 저장은 일어나지만, 커널 모드에 들어갔다 나오는 게 부담이 적음
    - Cache memory flush는 Main memory와 CPU 사이의 빠른 기억 장치인데, 문맥교환이 일어날 경우 담겨 있는 정보를 다 지워야한다. 하지만 커널 모드로 넘어갔다 오는 경우는 그 정도의 overhead가 발생하진 않음, CPU context정보만 간단히 저장됨
  - 만약 timer interrupt가 발생하면 다른 사용자 프로세스로 CPU 제어권이 넘어간다
  - I/O요청 시스템 콜도 해당 작업이 오래 걸리므로 다른 프로세스로 CPU 제어권을 넘길 경우 문맥 교환이 일어난다.

- 프로세스를 스케줄링하기 위한 큐
  - Job queue
    - 현재 시스템 내에 있는 모든 프로세스의 집합
  - Ready queue
    - CPU를 잡아서 실행되기를 기다리는 프로세스의 집합
    - PCB를 연결해놓음
  - Device queue
    - I/O Device의 처리를 기다리는 프로세스의 집합
    - 여기도 PCB가 연결되어 기다리는 중

- 스케줄러(Scheduler)

  - Long-term scheduler(장기 스케줄러 or job scheduler)

    - 시작 프로세스 중 어떤 것들을 ready queue로 보낼지 결정
    - 프로세스에 memory(및 각종 자원)을 주는 문제
    - degree of Multiprogramming을 제어(메모리에 올라가 있는 프로세스의 수)
    - time sharing system에는 보통 장기 스케줄러가 없음(**무조건 ready**)
    - 어떤 프로세스가 new상태에 있는데 메모리를 줄지 안 줄지를 결정하는 것

  - Short-term scheduler(단기 스케줄러 or CPU scheduler)

    - 어떤 프로세스를 다음번에 running 시킬지 결정
    - 프로세스에 CPU를 주는 문제
    - 충분히 빨라야 함(millisecond 단위)

  - Medium-Term Scheduler(중기 스케줄러 or Swapper)

    - 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄
    - 프로세스에게서 memory를 뺏는 문제
    - degree of Multiprogramming을 제어

    - 지금은 우선 메모리에 다 올려놓고 너무 많은 경우 쫓아내면서 수를 조절

    - Suspended(stopped)
      - 외부적인 이유로 프로세스의 수행이 정지된 상태
      - 프로세스는 통째로 디스크에 swap out 된다
      - 메모리에 너무 많은 프로세스가 올라와 있을 때
      - break key를 눌러서 일시정지를 시킬 때에도 Suspended된다.

> Blocked: 자신이 요청한  event가 만족되면 Ready
>
> Suspended: 외부에서 resume을 해주어야 Active 상태로 돌아감

> 사용자 프로세스가 인터럽트, 시스템 콜등을 했을 때 커널모드로 들어가는데 운영체제가 러닝을 하고 있다고 칭하지는 않음, 그대로 프로세스가 러닝하고 있다고 표현해야함. 커널 모드에서 사용자 프로그램이 진행 중이라고 말하면 된다.

![image-20221025105605777](Process(1).assets/image-20221025105605777.png)

