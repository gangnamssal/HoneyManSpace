# 스택2 (stack2)

---

## 1. 계산기

- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.



- **표기법**
  - **중위표기법 (infix notation)** : 연산자를 피연산자의 가운데 표기하는 방법 (ex. A+B)
  - **후위표기법 (postfix notation)** : 연산자를 피연산자 뒤에 표기하는 방법 (ex. AB+)



- **방법**

  - **중위 표기법의 수식을 후위 표기법으로 변경**한다. (스택 활용)

    1. 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현한다.
    2. 각 연산자를 그에 대응하는 오른쪽괄호의 뒤로 이동시킨다.
    3. 괄호를 제거한다.

    ```python
    # EX) A*B-C/D
    # 1. ((A*B)-(C/D))
    # 2. ((AB)*(CD)/)-
    # 3. AB*CD/-
    ```

    - **변환 알고리즘**
      1. 입력 받은 중위 표기식에서 토큰 (피연산자, 연산자) 을 읽는다.
      2. 토큰이 피연산자이면 토큰을 출력한다.
      3. 토큰이 연산자 (괄호포함) 일 때, 이 토큰이 스택의 top에 **저장되어 있는 연산자보다 우선순위가 높으면 스택에 push**, 아니면 **연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop** 한 후 토큰의 연산자를 push.
      4. 만약 top에 연산자가 없으면 push한다.
      5. 토큰이 오른쪽 괄호 ')' 이면 스택 top에 왼쪽 괄호 '(' 가 올 때까지 스택에서 pop 연산을 수행하고 pop 한 연산자를 출력. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
      6. 더 읽을 것이 있으면 1번부터 다시 반복, 없으면 스택에 남아있는 연산자를 모두 pop하여 출력

  

  - **후위 표기법의 수식을 스택을 이용하여 계산**한다.
    1. 피연산자를 만나면 스택에 push
    2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop 하여 연산하고, 연산 결과를 다시 스택에 push 한다.
    3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

----

## 2. 백트래킹

- **정의** 
  - 해를 찾는 도중에 **막히면 (해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법**
  - **최적화 (optimization) 문제와 결정 (decision) 문제를 해결할 수 있다.**
    - **결정 문제** : 문제의 조건을 만족하는 해가 존재하는지의 여부를 yes or no가 답하는 문제 
  - **DFS와 차이점**
    - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 **시도의 횟구를 줄인다.** (Prunning 가지치기)
    - **불필요한 경로를 조기에 차단**, 즉 모든 후보를 검사하지 않는다.
      - 어떤 노드의 유망성을 점검한 후에 **유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 간다**.
      - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 **해답이 될 수 없으면** 그 노드는 **유망하지 않다**고 하고 **해답의 가능성이 있으면 유망**하다고 한다.
    - DFS를 하기에는 경우의 수가 너무 많으면 사용
    - 백트래킹을 적용하면 일반적으로 경우의 수가 줄어들지만 최악의 경우 지수함수 시간이 된다.

- **절차**
  1. 상태 공간 트리의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지를 점검
  3. 만일 그 노드가 유망하지 않다면, 그 노드의 부모 모드로 돌아가서 검색을 계속 진행

- **응용**

  **1. 미로 찾기**

  - 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제
  - 이동할 수 있는 방향은 4방향으로 제한.

  - **방법**
    1. 벽을 만나면 스택을 이용하여 지나온 경로를 역으로 되돌아 간다.
    2. 스택을 이용하여 다시 경로를 찾는다.

  **2. n-queen**

  ```python
  # n-queen
  def checknode (V): # node
      if promising(V): #놓을 수 있으면
          if there is a solution at V: # 마지막 칸에 놓인 퀸인지 확인
              write the solution	
          else:
              for u in each child of V: # 다시 체크
                  checknode(u)
  ```
  
  3. **부분집합 구하기**

  - n개의 원소가 들어있는 집합의 2^n 개의 부분집합을 만들 때는 **true or false 값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용**한다.

  - 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값.

  - ```python
    # 부분 집합 2진수
    def f(i, N):
        if i == N:
            print(bit)
        else:
            bit[i] = 1 # A[i]가 부분집합에 포함
            f(i+1, N)
            bit[i] = 0
            f(i+1, N)
    
    A = [1,2,3]
    bit = [0] * 3
    f(0, 3)
    
    # 부분 집합 원소
    def f(i, N):
        if i == N:
            for i in range(N):
                if bit[i]:
                    print(A[i], end=' ')
            print()
        else:
            bit[i] = 1 # A[i]가 부분집합에 포함
            f(i+1, N)
            bit[i] = 0
            f(i+1, N)
    
    A = [1,2,3,4,5,6,7,8,9,10]
    bit = [0] * 10
    f(0, 10)
    ```
  
  - ```python
    def backtrack(a, k, input):
        global MAXCANDIDATES
        c = [0] * MAXCANDIDATES
        if k == input:
            process_solution(a, k) # 답이면 원하는 작업을 실행
        else:
            k+=1
            ncandidates = construct_candidates(a, k, input, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k, input)
                
    def construct_candidates(a, k, input, c):
        c[0] = True
        c[1] = False
        return 2
    
    MAXCANDIDATES = 2
    NMAX = 4
    a = [0] * NMAX
    backtrack(a,0,3)
    ```
  
  
  4. **순혈 구하기**
  
  - ```python
    def backtrack(a, k, input):
        global MAXCANDIDATES
        c = [0] * MAXCANDIDATES
        if k == input:
            for i in range(1, k+1):
                print(a[i], end=' ')
            print()
        else:
            k+=1
            ncandidates = construct_candidates(a, k, input, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k, input)
                
    def construct_candidates(a, k, input, c):
        in_perm = [False] * NMAX
        
        for i in range(1, k):
            in_perm[a[i]] = True
            
        ncandidates = 0
        for i in range(1, input+1):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1
        return ncandidates
    ```
  
  - ```python
    def (i, N):
        if i == N:
            return
        else:
            for j, i in range(N-1):
                p[i], p[j] = p[j], p[i]
                f(i+1, N)
                p[i], p[j] = p[j], p[i]
    ```

---

## 3. 분할 정복 알고리즘

- **전략**
  - 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine) : (필요하다면) 해결된 해답을 모은다.



- **활용**

  - ```python
    # 거듭제곱
    def Power(Base, Exponent):
        if Exponent == 0 or Base == 0:
            return 1
        if Exponent % 2 == 0:
            NewBase = Power(Base, Exponent/2)
            return NewBase * NewBase
        else:
            NewBase = Power(Base, (Exponent-1)/2)
            return (NewBase * NewBase) * Base
    ```

---

## 4. 퀵 정렬

- **정의**
  - 주어진 배열을 두 개로 분할하고, 각각을 정렬
  - **합병 정렬과 차이점**
    -  **합병정렬은 두 부분으로 나누는 반면**에, **퀵정렬은 분할할 때, 기준 아이템 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치**시킨다.
    - 각 부분 정렬이 끝난 후, **합병정렬은 '합병'이란 후처리 작업이 필요**하나, **퀵정렬은 필요하지 않다.**

- **알고리즘**

  - ```python 
    def quickSort(a, begin, end):
        if begin < end:
            p = partition(a, begin, end)
            quickSort(a, begin, p-1)
            quickSort(a, P+1, end)
    ```

  - ```python
    def partition(a, begin, end):
        pivot = (begin + end) // 2
        L = begin
        R = end
      	while L < R:
            while L<R and a[L] < a[pivot]:
                L += 1
            while L<R and a[R] >= a[pivot]:
                R -= 1
            if L < R:
                if L == pivot:
                    pivot = R
                    a[L], a[R] = a[R], a[L]
        a[pivot], a[R] = a[R], a[pivot]
        return R
    ```

- **시간 복잡도** : 최악의 경우 O(n**2)이지만, 평균 nlogn로 가장 빠르다.
