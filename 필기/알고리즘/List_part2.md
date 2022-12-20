## 배열 part.2

---

### 1. 2차원 배열

- 1 차원 list를 묶어놓은 list

- 2 차원 이상의 다 차원 list는 차원에 따라 index를 선언

- 2 차원 list의 선언 : **세로 길이 (행의 개수), 가로 길이 (열의 개수)를 필요**로 한다.

- python 에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능하다.

- ```py
  # 행 우선 순회, i 행 j 열
  for i in range(n):
  	for j in range(m):
          Array[i][j] #필요한 연산 수행
  ```

- ```py
  # 열 우선 순회, i 행 j 열
  for j in range(m):
      for i in range(n):
          Array[i][j] # 필요한 연산 수행
  ```

- ```python
  # 지그재그 순회, i 행 j 열
  for i in range(n):
      for j in range(m):
          Array[i][j+(m-1-2*j)*(i%2)] # 필요한 연산 수행
  ```

- **델타를 이용한 2 차 배열 탐색**

  - ``` python
    # 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색
    # 예시
    di = [0, 1, 0, -1] # 오른쪽부터 시계 방향
    dj = [1, 0, -1, 0]
    N = 3
    M = 4
    arr = [[1,2,3,4],[4,5,6,8]]
    for i in range(N):
        for j in range(N):
           # for d in range(1,3): # 곱셈을 추가하여 칸의 접근을 다양하게 할 수 있다
                for k in range(4):
                    ni = i + di[k]*d 
                    nj = j + dj[k]*d
                    if 0<= ni < N and 0<= nj < M:
                        print(ni,nj)
    ```

  - ```python
    # 다른 모양
    for i in range(N):
        for j in range(M):
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i + dj, j + dj
                if 0<= ni < N and 0<= nj < M:
                    print(ni,nj)
    ```

- **전치 행렬**

  - ```python
    for i in range(3):
        for j in range(3):
            if i < j :
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ```

### 2. 부분 집합 생성

- 부분 집합의 수

  - 원소가 n개일 때, 공집합을 포함한 부분 집합의 수는 2**n개이다.

  - 각 원소를 부분 집합에 포함 시키거나 포함 시키지 않는 2 가지 경우를 모든 원소에 적용한 경우의 수와 같다.

  - ```py
    # loop 이용해 확인하고 부분 집합을 생성
    bit = [0,0,0,0]
    for i in range(2):
        bit[0] = i   # 0번째 원소
        for j in range(2):
            bit[1] = j    # 1번째 원소
            for k in range(2):
                bit[2] = k   # 2번째 원소
                for l in range(2):
                    bit[3] = l   # 3번째 원소
                    print_subset(bit)  # 생성된 부분 집합 출력
    ```

  - **비트 연산자**

    - **&** : 비트 단위로 AND 연산 - **( i&(1<<j) : i의 j번째 비트가 1인지 아닌 지를 검사 )**

    - **ㅣ** : 비트 단위로 OR 연산

    - **<<**  : 피연산자의 비트 열을 왼쪽으로 이동 ( 1<<n : 2**n , 원소가 n개일 경우 모든 부분 집합의 수 )

    - **'>>'** : 피연산자의 비트 열을 오른쪽으로 이동

    - ```python
      # ex
      arr = [3,6,7,1,5,4]
      n = len(arr) # 원소의 갯수
      for i in range(1<<n):   # 1<<n : 부분 집합의 개수
          for j in range(n):   # 원소의 수 만큼 비트를 비교
              if i & (1<<j):   # i의 j번 비트가 1인 경우
                  print(arr[j], end=', ')   # j번 원소 출력
          print()
      print()
      ```

### 3. 바이너리 서치

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

- **목적하는 탐색 키를 가진 항목을 찾는 것**

  - 탐색 키 (search key) : 자료를 구별하여 인식할 수 있는 키

- **종류**

  - **순차 검색 (sequential search)**

    - 일렬로 되어 있는 자료를 순서대로 검색하는 방법

    - 가장 간단하고 직관적인 검색 방법

    - 배열이나 연결 리스트 등 순차 구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용

    - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행 시간이 급격히 증가하여 비효율적

    - **정렬되어 있지 않은 경우**

      1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교

      2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환

      3. 자료 구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

         - 첫 번째 원소를 찾을 때는 1 번 비교, 두 번째 원소를 찾을 때는 2 번 비교

         - 평균 비교 횟수 : (n+1) / 2

         - 시간 복잡도 : O(n)

         - ```python
           def sequentialsearch(a, n, key):
               i = 0
               while (i < n) and (a[i] != key):
                   i += 1
                   if i < n:
                       return i
                   else:
                       return -1
           ```

    - **정렬되어 있는 경우**

      1. 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정

      2. 자료를 순차적으로 검색하면서 키 값을 비교, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없음으로 검색 종료

         - 찾고자 하는 원소의 순서에 따라 비교 횟수가 결정된다.

         - 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어든다.

         - 시간 복잡도 : O(n)

         - ```python
           def sequetialsearch(a,n,key):
               i = 0
               while (i < n) and (a[i] < key):
                   i += 1
                   if (i < n) and (a[i] == key):
                       return i
                   else:
                       return -1
           ```

  - **이진 검색 (binary search)**

    - 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

    - 목적 키를 찾을 때까지 이진 검색을 순환 적으로 반복 수행하여 검색 범위를 반으로 줄여 가면서 보다 빠르게 검색을 수행

    - **이진 검색을 하기 위해서는 자료가 정렬된 상태**여야 한다.

    - **검색 과정**

      1. 자료의 중앙에 있는 원소를 고름

      2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교

      3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로운 검색을 수행, 크다면 자료의 오른쪽 반에 대해서 새로운 검색을 수행

      4. 찾고자 하는 값을 찾을 때까지 반복

         - 검색 범위의 시작 점과 종료 점을 이용하여 검색을 반복 수행

         - 이진 검색의 경우, **자료의 삽입이나 삭제가 발생**했을 때 배열의 상태를 **항상 정렬 상태로 유지하는 추가 작업이 필요**.

         - ```python
           def binarysearch(a, N, key):
               start = 0
               end = N-1
               while start <= end:
                   middle = (start + end)//2
                   if a[middle] == key:       # 검색 성공
                       return true
                   elif a[middle] > key:
                       end = middle - 1
                   else:
                       start = middle + 1
               return false                   # 검색 실패
           ```

         - ```python
           # 재귀 함수 이용 (효율이 떨어진다.)
           def binarysearch(a, low, high, key):
               if low > high:                 # 검색 실패
                   return False
               else:
                   middle = (low + high) // 2
                   if key == a[middle]:       # 검색 성공
                       return True
                   elif key < a[middle]:
                       return binarysearch(a, low, middle-1, key)
                   elif key > a[middle]:
                       return binarysearch(a, middle +1, high, key)
           ```

### 4. 셀렉션 알고리즘

- **인덱스**

  - 테이블에 대한 동작 속도를 높여주는 자료 구조를 말한다.
  - 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 떄문이다.

- **선택 정렬**

  - 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

  - **정렬 과정**

    1. 주어진 리스트 중에서 최솟값의 인덱스를 찾는다.
    2. 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
    3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

  - **시간 복잡도** : O(n**2)

  - ```py
    def selectionsort(a,n):
        for i in range(n-1):
            minidx = i
            for j in range(i+1,N):
                if a[minidx] > a[j]:
                    minidx = j
             	a[i], a[minidx] = a[minidx], a[i]
    ```

- **셀렉션 알고리즘**

  - 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라고 한다.
  - 최솟값, 최댓값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.
  - **과정**
    1. 정렬 알고리즘을 이용하여 자료 정렬하기
    2. 원하는 순서에 있는 원소 가져오기

  - **시간 복잡도** : O(kn)

  - ```python
    # 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고 배열의 k번째를 반환
    def select(arr, k):
    	for i in range(0,k):
    		minidx = i
            for j in range(i+1, len(arr)):
                if arr[minidx] > arr[i]:
                    minidx = j
            arr[i], arr[minidx] = arr[minidx], arr[i]
        return arr[k-1]
    ```

