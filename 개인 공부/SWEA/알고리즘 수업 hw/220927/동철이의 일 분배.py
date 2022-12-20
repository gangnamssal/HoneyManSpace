# import sys
# sys.stdin = open('동철이의 일 분배.txt','r')

# 직원 번호 : 1~N
# 일 번호 : 1~N
# i번 직원이 j번 일을 하면 성공 확률이 Pij
# 주어진 일이 모두 성공할 확률의 최댓값
def solve(j,v):
    global maxV
    if j == N and maxV < v:
        maxV = v
    if v == 0:
        return
    if v < maxV:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            solve(j+1,v*Pij[i][j]/100)
            visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Pij = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    maxV = 0
    solve(0,1)
    print(f'#{tc} {maxV * 100:.6f}')
