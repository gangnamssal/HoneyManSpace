import sys
sys.stdin = open('최소 신장 트리.txt','r')
# 최소 신장 트리를 구성
# 최소 신장 트리를 구성하는 간선을 모두 더해 출력하는 프로그햄
def prim(r,V):
    MST = [0]*(V+1)
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 1:
                for j in range(V+1):
                    if adj[i][j] > 0 and MST[j] == 0 and minV>adj[i][j]:
                        u = j
                        minV = adj[i][j]
        s += minV
        MST[u] = 1
    return s

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 마지막 노드 번호 V, 간선의 개수 E
    V, E = map(int,input().split())
    # 처음 가중치를 최댓값으로 초기화한다.
    adj = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        n1,n2,w = map(int,input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    print(f'#{tc} {prim(0, V)}')
