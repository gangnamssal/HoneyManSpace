# 큐(Queue)

---

## 0. Queue

- **큐의 특성**
  - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - **선입 선출 구조(FIFO : First in First Out)** : 큐에 삽입한 순서대로 원소가 저장, 가장 먼저 삽입된 원소가 가장 먼저 삭제된다.
  - **기본 연산**
    - **enQueue(item)** : 큐의 뒤쪽(rear 다음) 에 원소를 삽입하는 연산
    - **deQueue()** : 큐의 앞쪽(front) 에서 원소를 삭제하고 반환하는 연산
    - **createQueue()** : 공백 상태의 큐를 생성하는 연산
    - **isEmpty()** : 큐가 공백 상태 인지를 확인하는 연산
    - **isFull()** : 큐가 포화 상태 인지를 확인하는 연산
    - **Qpeek()** : 큐의 앞쪽(front) 에서 원소를 삭제 없이 반환하는 연산



- **연산 과정**

> 1. 공백 큐 생성 : createQueue()
> 2. 원소 A 삽입 : enQueue(A)
> 3. 원소 B 삽입 : enQueue(B)
> 4. 원소 반환/삭제 : deQueue() - A 삭제
> 5. 원소 C 삽입 : enQueue(C)
> 6. 원소 반환/삭제 : deQueue() - B 삭제
> 7. 원소 반환/삭제 : deQueue() - C 삭제
> 8. front와 rear가 같으면 Queue가 비어있는 상태라고 판단

---

## 1. 선형큐

- **정의**
  - 1 차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front : 저장된 첫 번째 원소의 인덱스
  - rear : 저장된 마지막 원소의 인덱스



- **상태 표현**
  - **초기 상태 : front = rear = -1**
  - **공백 상태 : front == rear**
  - **포화 상태 : rear == n-1 (n : 배열의 크기,  n-1 : 배열의 마지막 인덱스)**



- **구현**

  - **삽입 : enQueue(item)**

  - ```python
    def enQueue(item):
        global rear
        if isFull():       # 디버깅용
            print('Q_Full')
        else:
            rear += 1
            Q[rear] = item
    ```

  - **삭제 : deQueue()**

  - ```python
    # front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
    # 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능을 한다.
    def deQueue():
        global front
        if isEmpty:			# 디버깅용
            print('error')
        else:
            front += 1
            return Q[front]
    ```

  - **공백 및 포화 검사 : isEmpty(), isFull()**

  - ```python j
    # 공백 상태 : front == rear
    # 포화 상태 : rear == n-1
    def isEmpty():
        return front == rear
    def isFull():
        return rear == len(Q) - 1
    ```

  - **검색 : Qpeek()**

  - ```python
    # 가장 앞에 있는 원소를 검색하여 반환하는 연산
    # 현재 front의 한자리 뒤(front+1)에 있는 원소, 큐의 첫 번째에 있는 원소를 반환
    def Qpeek():
        if isEmpty():		# 디버깅용
            print('Q_Empty')
        else:
            return Q[front+1]
    ```



- **선형 큐의 문제점**
  - **잘못된 포화 상태 인식**
    - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞 부분에 활용할 수 있는 공간이 있음에도 rear = n-1인 상태, 포화 상태로 인식하여 더 이상 삽입을 할 수 없다.
  - **해결 방법 1**
    - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞 부분으로 모두 이동시킨다.
    - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 많이 떨어진다.
  - **해결 방법 2**
    - 1 차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용. **(원형 큐)**

---

## 2. 원형 큐

- **구조**
  - **초기 공백 상태**
    - front = rear = 0
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 한다.
  - 이를 위해 **나머지 연산자 mod를 사용**한다.
  - **front 변수**
    - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 **사용하지 않고 항상 비워둔다.**
  - **삽입 및 삭제 위치**
    - **선형 큐**
      - 삽입 위치 : rear += 1
      - 삭제 위치 : front += 1
    - **원형 큐**
      - 삽입 위치 : rear = (rear + 1) mod n
      - 삭제 위치 : front = (front + 1) mod n



- **구현**

  - **초기 공백 큐 생성**

    - 크기 n인 1 차원 배열 생성
    - front와 rear를 0으로 초기화

  - **공백 및 포화 상태 검사 : isEmpty(), isFull()**

  - ```python
    # 공백 상태 : front == rear
    # 포화 상태 : 삽입할 rear의 다음 위치 == 현재 front : (rear + 1) mod n == front
    def isEmpty():
        return front == rear
    def isFull():
        return (rear + 1) % len(cQ) == front
    ```

  - **삽입 : enQueue(item)**

  - ```py
    # 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    # 1) rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련 : rear=(rear + 1) % len(Q)
    # 2) 그 인덱스에 해당하는 배열 원소 cQ[rear]에 item을 저장
    def enQueue(item):
        global rear
        if isFull():		# 디버깅용
            print('Q_Full')
        else:
            rear = (rear + 1) % len(cQ)
            cQ[rear] = item
    ```

  - **삭제 : deQueue(), delete()**

  - ```python
    # 가장 앞에 있는 원소를 삭제하기 위해
    # 1) front 값을 조정하여 삭제할 자리를 준비함
    # 2) 새로운 front 원소를 리턴 함으로써 삭제와 동일한 기능을 한다.
    def deQueue():
        global front
        if isEmpty():		# 디버깅용
            print('Q_Empty')
        else:
            front = (front + 1) % len(cQ)
            return cQ[front]
    ```

---

## 3. 우선순위 큐

- **특성**
  - 우선 순위를 가진 항목들을 저장하는 큐
  - FIFO 순서가 아니라 우선 순위가 높은 순서대로 먼저 나가게 된다.
  - **적용 분야**
    - 시뮬레이션 시스템
    - 네트워크 트래픽 제어
    - 운영체제의 테스크 스케줄링



- **구현**
  - **배열을 이용한 우선 순위 큐**
    - 배열을 이용하여 자료 저장
    - 원소를 삽입하는 과정에서 우선 순위를 비교하여 적절한 위치에 삽입하는 구조
    - 가장 앞에 최고 우선 순위의 원소가 위치하게 된다.
    - **문제점**
      - 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생
      - 소요되는 시간이나 메모리 낭비가 크다.
  - **리스트를 이용한 우선 순위 큐**

---

## 4. 활용

- **버퍼(Buffer)**
  - 데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링 : 버퍼를 활용하는 방식 or 버퍼를 채우는 동작을 의미
  - **자료 구조**
    - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
    - 순서대로 입력/출력이 전달되어야 하므로 FIFO 방식의 자료 구조인 큐가 활용된다.

----

## 5. BFS

- **정의**
  - 탐색 시작 점의 **인접한 정점들을 먼저 모두 차례로 방문**한 후에, **방문했던 정점을 시작 점으로 하여 다시 인접한 정점들을 차례로 방문**하는 방식
  - 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행해야 하므로, 선입 선출 형태의 자료구조인 큐를 활용한다.



- **알고리즘**

- ```python
  def BFS(G, v): # G : 그래프, V : 탐색 시작점
      visited = [0]*(n+1)			 # n : 정점의 개수
      queue = []				    # 큐 생성
      queue.append(v)				# 시작점 v를 큐에 삽입
      while queue:				# 큐가 비어있지 않은 동안
          t = queue.pop(0)		 # 큐의 첫번째 원소 반환
          if not visited[t]:		 # 방문하지 않은 곳
              visited[t] = True	  # 방문 했다고 표시
              visit(t)			 # 정점 t에서 할 일
              for i in G[t]:		  # t와 연결된 모든 정점에 대해
                  if not visited[i]: # 방문되지 않은 곳이라면
                      queue.append(i) # 큐에 넣는다.
      
  ```

- ```python
  def BFS(G, v, n): # G : 그래프, V : 탐색 시작점
      visited = [0]*(n+1)			 # n : 정점의 개수
      queue = []				    # 큐 생성
      queue.append(v)				# 시작점 v를 큐에 삽입
      visited[v] = 1
      while queue:				# 큐가 비어있지 않은 동안
          t = queue.pop(0)		 # 큐의 첫번째 원소 반환
          visit(t)			 # 정점 t에서 할 일
          for i in G[t]:		  # t와 연결된 모든 정점에 대해
              if not visited[i]: # 방문되지 않은 곳이라면
                  queue.append(i) # 큐에 넣는다.
                  visited[i] = visited[t] + 1 # n으로부터 1만큼 이동
  ```

  