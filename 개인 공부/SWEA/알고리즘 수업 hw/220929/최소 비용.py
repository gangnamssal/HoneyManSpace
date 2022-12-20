import sys
sys.stdin = open('최소 비용.txt','r')
# (0,0)에서 (N-1,N-1)까지 갈 때 최소 비용을 구함
# 높이가 1 증가할 때 비용도 1 증가
def bfs(r,c):
    visited[r][c] = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    queue.append((r,c))
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0<= nr < N and 0<= nc < N:
                height = 0
                if H[nr][nc] - H[x][y] > 0:
                    height = H[nr][nc] - H[x][y]

                if visited[nr][nc] > visited[x][y] + 1 + height:
                    visited[nr][nc] = visited[x][y] + 1 + height
                    queue.append((nr,nc))
    return visited[N-1][N-1]

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 가로, 세로칸 수 N
    N = int(input())
    H = [list(map(int,input().split())) for _ in range(N)]
    visited = [[999999]*N for _ in range(N)]
    queue = []
    result = bfs(0, 0)
    print(f'#{tc} {result}')