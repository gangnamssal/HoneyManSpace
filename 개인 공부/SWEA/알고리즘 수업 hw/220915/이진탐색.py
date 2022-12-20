import sys
sys.stdin = open('이진탐색.txt','r')
# N이 주어졌을 때 완전 이진 트리로 만든
# 이진 탐색 트리의 루트에 저장된 값과
# N/2번 노드에 저장된 값을 출력하는 프로그램

# 첫 줄에 테스트 케이스
def inorder(v):
    global number
    if v < N+1 and v:
        inorder(2*v)
        arr[v] = number
        number += 1
        inorder(2*v+1)

T = int(input())
for tc in range(1,T+1):
    # 테스트 케이스의 별로 N이 주어짐
    N = int(input())
    arr = [_ for _ in range(N+1)]
    number = 1
    inorder(1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')