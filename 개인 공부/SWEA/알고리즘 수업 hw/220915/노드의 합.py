import sys
sys.stdin = open('노드의 합.txt','r')

def preorder(v):
    if v > N:
        return 0
    l_result = preorder(2*v)
    r_result = preorder(2*v+1)
    tree[v] += l_result + r_result
    return tree[v]

# 테스트 케이트 T
T = int(input())
for tc in range(1,T+1):
    # 노드의 개수 N, 리프 노드의 개수M, 값을 출력할 노드 번호 L
    N, M, L = map(int,input().split())
    # M개의 줄에 걸쳐 리프 노드 번호, 자연수
    tree = [0] * (N+1)
    for i in range(M):
        L_num, nat = map(int,input().split())
        tree[L_num] = nat
    print(tree)
    # L, R = 0, 0
    result = preorder(1)
    print(tree[L])