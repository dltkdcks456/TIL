# 큐(Queue)의 특성

- 삽입과 삭제의 위치가 제한적인 자료 구조
  - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
- 선입선출구조(FIFO : First In First Out)
  - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제된다.

- 큐의 연산 과정

  - 공백 큐 생성: createQueue();
    - front = rear = -1
  - 원소 A 삽입: enQueue(A);
    - front = -1, rear += 1
  - 원소 반환/삭제 : deQueue();
    - front:마지막으로 꺼낸 자리, rear: 마지막 저장 위치
  - 원소 C 삽입: enQueue(C);
    - rear += 1
  - front == rear이면 큐가 비어있는 상태

  - 포화 상태: rear == n-1
  - 



- 설계와 관련된 내용
- 빠짐없이 중복없이: DFS, BFS
- 최단거리: DFS, BFS
- 경로의수: DFS
- 확산(출발이 여러 곳): BFS

![image-20220824164304128](큐(Queue).assets/image-20220824164304128.png)

![image-20220824164649245](큐(Queue).assets/image-20220824164649245.png)