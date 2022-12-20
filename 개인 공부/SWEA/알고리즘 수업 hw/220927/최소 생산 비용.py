import sys
sys.stdin = open('최소 생산 비용.txt','r')
# 최소 생산 비용을 구하라
# 한 공장에서는 하나의 제품만 생성
def choice(num, v):
    global minV
    if v > minV:
        return
    if num == N and minV > v:
        minV = v
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            choice(num+1,v+Vij[num][i])
            visited[i] = 0

# 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    # 제품 수 N
    N = int(input())
    # 생산 비용 Vij
    Vij = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    minV = 9999
    choice(0, 0)
    print(f'#{tc} {minV}')
