import sys
sys.stdin = open('미생물 격리.txt','r')
# 정사각형 구역 안에 K개의 미생물
# 가로 * 세로 = N*N
# 가장자리 부분에 약품

# 군집의 위치, 미생물 수, 이동 방향이 주어진다.
# 1시간마다 상하좌우 이동
# 이동 후 약품이 칠해진 셀에 도착하면 절반이 없어짐, 이동 방향이 반대
# 홀 수 = //
# 한 셀에 두 개 이상의 군집이 모이면 합쳐짐, 이동 방향은 수가 많은 미생물 군집의 방향

# 정사각형, 한 변의 셀의 개수 5<= N <= 100
# 미생물 군집의 개수 5<=K<=1000
# 격리 시간 1<=M<=1000
# 미생물 수 1이상 10000 이하

T = int(input())
for tc in range(1,T+1):
    # 한 변 N, 격리 시간 M ,군집 개수 K
    N,M,K = map(int,input().split())
    # c,r,미생물 수,이동 방향
    arr = [list(map(int,input().split())) for _ in range(K)]
    # 상 하 좌 우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    # 미생물 수를 담는 리스트
    board = [[0]*N for i in range(N)]
    # 미생물의 이동 방향을 나타내는 리스트
    move = [[0]*N for i in range(N)]
    for i in arr:
        board[i[0]][i[1]] = i[2]
        move[i[0]][i[1]] = i[3]
    result = 0
    cnt = 0
    while cnt < M:
        # 변경된 이동 방향을 나타내는 리스트
        change = [[0]*N for i in range(N)]
        # 변경된 미생물의 수를 나타내는 리스트
        c_board = [[0]*N for i in range(N)]
        for r in range(N):
            for c in range(N):
                if move[r][c]==1:
                    nr = r + dr[0]
                    nc = c + dc[0]
                    if not change[nr][nc]:
                        change[nr][nc] = [1,board[r][c]]
                    else:
                        change[nr][nc] += [1, board[r][c]]
                    if not c_board[nr][nc]:
                        c_board[nr][nc] = [board[r][c]]
                    else:
                        c_board[nr][nc] += [board[r][c]]
                elif move[r][c]==2:
                    nr = r + dr[1]
                    nc = c + dc[1]
                    if not change[nr][nc]:
                        change[nr][nc] = [2, board[r][c]]
                    else:
                        change[nr][nc] += [2, board[r][c]]
                    if not c_board[nr][nc]:
                        c_board[nr][nc] = [board[r][c]]
                    else:
                        c_board[nr][nc] += [board[r][c]]
                elif move[r][c]==3:
                    nr = r + dr[2]
                    nc = c + dc[2]
                    if not change[nr][nc]:
                        change[nr][nc] = [3, board[r][c]]
                    else:
                        change[nr][nc] += [3, board[r][c]]
                    if not c_board[nr][nc]:
                        c_board[nr][nc] = [board[r][c]]
                    else:
                        c_board[nr][nc] += [board[r][c]]
                elif move[r][c]==4:
                    nr = r + dr[3]
                    nc = c + dc[3]
                    if not change[nr][nc]:
                        change[nr][nc] = [4, board[r][c]]
                    else:
                        change[nr][nc] += [4, board[r][c]]
                    if not c_board[nr][nc]:
                        c_board[nr][nc] = [board[r][c]]
                    else:
                        c_board[nr][nc] += [board[r][c]]
        for i in range(N):
            for j in range(N):
                maxV = 0
                index = 0
                if c_board[i][j] != 0:
                    if i == 0 or j == 0 or i == N-1 or j == N - 1:
                        su = 0
                        for k in range(len(c_board[i][j])):
                            su += c_board[i][j][k]
                        c_board[i][j] = su//2
                    else:
                        su = 0
                        for k in range(len(c_board[i][j])):
                            su += c_board[i][j][k]
                        c_board[i][j] = su
                if change[i][j] != 0:
                    for k in range(1,len(change[i][j]),2):
                        if maxV < change[i][j][k]:
                            maxV = change[i][j][k]
                            index = change[i][j][k-1]
                    if i == 0 or j == 0 or i == N-1 or j == N - 1:
                        if index == 1:
                            change[i][j] = 2
                        elif index == 2:
                            change[i][j] = 1
                        elif index == 3:
                            change[i][j] = 4
                        elif index == 4:
                            change[i][j] = 3
                    else:
                        change[i][j] = index
        move = change[:]
        board = c_board[:]
        cnt += 1

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                result += board[i][j]
    print(f'#{tc} {result}')
