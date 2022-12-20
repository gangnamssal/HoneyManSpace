import sys
from collections import deque
sys.stdin = open('보급로.txt','r')
def bfs(r,c):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    visited[r][c] = 0
    queue.append((r,c))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0<= nr < N and 0<= nc < N:
                if visited[nr][nc] > data[nr][nc] + visited[x][y]:
                    visited[nr][nc] = data[nr][nc] + visited[x][y]
                    queue.append((nr,nc))
    return visited[N-1][N-1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input())) for _ in range(N)]
    visited = [[0xffffff]*N for _ in range(N)]
    queue = deque(set())
    result = bfs(0,0)
    print(f'#{tc} {result}')
