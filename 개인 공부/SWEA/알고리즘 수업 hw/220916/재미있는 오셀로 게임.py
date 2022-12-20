import sys
sys.stdin = open('재미있는 오셀로 게임.txt','r')
# 보드는 4*4, 6*6, 8*8

# 첫 줄에 테스트 케이스 T
T = int(input())
for tc in range(1,T+1):
    # 한변의 길이 N, 플레이어가 돌을 놓는 횟수 M
    N, M = map(int,input().split())
    # M줄에는 돌을 놓을 위치와 돌의 색
    # 1이면 흑, 2이면 백
    board = [[0] * N for _ in range(N)]
    # 초기 보드 상태
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 2, 2
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 1, 1
    # 돌의 위치에서 8방향 탐색
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    # M번의 게임을 반복
    for i in range(M):
        r, c, player = map(int, input().split())
        # 받은 위치를 인덱스 값으로 반환하기 위한 계산
        r -= 1
        c -= 1
        # 현재 돌 위치를 저장하는 변수
        x, y = r, c
        # 보드에 현재 위치에 플레이어를 표시
        board[r][c] = player
        # 현재 위치에서 8방향 탐색
        for j in range(8):
            nr = r + dr[j]
            nc = c + dc[j]
            # 탐색 범위가 벗어나거나 탐색한 값이 0이면 다음 탐색
            if nr < 0 or nr >= N or nc < 0 or nc >= N or not board[nr][nc] or board[r][c] == board[nr][nc]:
                continue
            # 탐색 방향의 수가 다르면 실행
            # 첫 위치의 돌 색갈과 같을 때 까지 실행
            while True:
                # 그 방향으로 이동 후 다시 같은 방향으로 탐색
                r, c = nr, nc
                nr, nc = r + dr[j], c + dc[j]
                if 0<= nr < N and 0<= nc <N and board[nr][nc] == board[x][y]:
                # 첫 위치로 돌아가면서 돌 색갈 첫 위치의 색갈로 바꾼다.
                    while r != x or c != y:
                        board[r][c] = board[x][y]
                        nr, nc = r - dr[j], c - dc[j]
                        r, c = nr, nc
                    break
                elif 0<= nr < N and 0<= nc <N and board[nr][nc] == board[r][c]:
                    continue
                else:
                    r, c = x, y
                    break
    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b_cnt += 1
            if board[i][j] == 2:
                w_cnt += 1
    print(f'#{tc} {b_cnt} {w_cnt}')
