import sys
sys.stdin = open('보급로.txt','r')

# 출발지에서 도착지까지 가는 경로 중 복구 시간이 가장 짧은 경로의 총 복구 시간
# 상하좌우로 이동
# 지도에는 각 칸마다 파여진 도로의 깊이
def bfs(r,c):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    result_lst[r][c] = data[r][c]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0<= nr < N and 0 <= nc < N:
                if result_lst[nr][nc] > result_lst[x][y] + data[nr][nc]:
                    result_lst[nr][nc] = result_lst[x][y] + data[nr][nc]
                    queue.append([nr,nc])
    return result_lst[N-1][N-1]

# 테스트케이스
T = int(input())
for tc in range(1,T+1):
    # 지도의 크기 N
    N = int(input())
    data = [list(map(int,input())) for _ in range(N)]
    queue = [[0,0]]
    result_lst = [[0xffffff]*N for _ in range(N)]
    result = bfs(0,0)
    print(f'#{tc} {result}')
