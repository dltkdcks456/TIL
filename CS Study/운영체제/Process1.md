# Process1

### 프로세스의 개념

- Process is a program in execution
- 프로세스의 문맥(context)
  - CPU 수행 상태를 나타내는 하드웨어 문맥
    - Program Counter
    - 각종 register
  - 프로세스의 주소 공간(메모리와 관련)
    - code, data, stack
  - 프로세스 관련 커널 자료 구조
    - PCB(Process Control Block)
      - process가 하나 실행될 때마다 pcb를 가지면서 관리를 한다.
    - Kernerl stack



### 프로세스의 상태

- 프로세스는 상태(state)가 변경되며 수행된다
  - Running
    - CPU를 잡고 instruction을 수행중인 상태
  - Ready
    - CPU를 기다리는 상태(메모리 등 다른 조건을 모두 만족)
  - Blocked(wait, sleep)
    - CPU를 주어도 당장 instruction을 수행할 수 없는 상태
    - Process 자신이 요청한 event(예: I/O)가 즉시 만족되지 않아 이를 기다리는 상태
    - 디스크에서 file을 읽어와야 하는 경우
  - New: 프로세스가 생성중인 상태
  - Terminated: 수행(execution)이 끝난 상태