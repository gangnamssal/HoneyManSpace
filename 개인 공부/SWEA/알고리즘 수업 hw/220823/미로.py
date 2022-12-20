import sys
sys.stdin = open('maze.txt','r')
# 도착할 수 있으면 1, 아니면 0

# 테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    # 미로의 크기
    N = int(input())
    # 0 : 통로, 1 : 벽, 2 : 출발, 3 : 도착
    maze = [list(map(int,input().strip())) for _ in range(N)]
    # 출발점 or 도착점을 찾음
    r, c = 0, 0
    # 방문을 저장하는 변수
    visited = [[0] * N for _ in range(N)]
    # 오 밑 왼 위
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    stack = []
    # 도착지 찾음
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                r, c = i, j
                break
        if r != 0 or c != 0:
            break
    stack.append((r, c))
    visited[r][c] = 1
    result = 0
    while stack:
        if result == 1:
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))
                    i = 0
                    break
                elif maze[nr][nc] == 2:
                    result = 1
                    break
        else:
            stack.pop()
    print(f'#{tc} {result}')