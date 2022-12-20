import sys
sys.stdin = open('미로1.txt','r')

def bfs(i,j): # 가로 세로
    visited[i][j] = 1
    front = rear = -1
    rear += 1
    q[rear] = (i,j)
    while front != rear:
        front += 1
        i,j = q[front]
        #오 밑 왼 위
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0<= ni < 16 and 0<= nj < 16 and not visited[ni][nj] and maze[ni][nj] != 1:
                visited[ni][nj] = 1
                rear += 1
                q[rear] = ni,nj
    return 0


# 테스트 케이스
for tc in range(1,11):
    TC = int(input())
    # 1 = 벽, 0 = 길, 2 = 출발점, 3 = 도착점
    maze = [list(map(int,input())) for _ in range(16)]
    # 시작점 (1,1)
    x, y = 1, 1
    # 방문 체크
    visited = [[0] * 16 for _ in range(16)]
    q = [0] * (16**2)
    print(f'#{tc} {bfs(x, y)}')

