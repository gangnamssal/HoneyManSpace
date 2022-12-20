import sys
sys.stdin = open('5105.txt','r')

# 최소 몇 개의 칸을 지나면 도착지에 다다를 수 있는지
# 경로가 없으면 0
# 1 벽, 0 통로
# 2에서 출발, 3 도착
def bfs(end): # 도착지
    global x, y
    front = rear = -1
    visited[x][y] = 1
    rear += 1
    q[rear] = (x, y)
    while front != rear:
        front += 1
        x, y = q[front]
        if maze[x][y] == end:
            return visited[x][y]-2
        # 우 밑 왼 위
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x + dx
            ny = y + dy
            if 0<= nx < N and 0<= ny < N and maze[nx][ny] != 1 and not visited[nx][ny]:
                rear += 1
                q[rear] = (nx, ny)
                visited[nx][ny] = visited[x][y] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    x, y = -1, -1
    # 출발지를 찾는다
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
                break
        if x != -1 and y != -1:
            break
    visited = [[0] * N for _ in range(N)]

    q = [0]*(N**2)
    print(f'#{tc} {bfs(3)}')
