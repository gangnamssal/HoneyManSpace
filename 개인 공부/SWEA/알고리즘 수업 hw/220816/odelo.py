# 교수님 풀이
import sys
sys.stdin = open('odelo.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 돌을 놓을수 있는 배열 준비
    # 흑 1, 백 2
    # 0행과 0열은 사용하지 않음, 문제에서 주어지는 좌표와 실제 위치를 맞추기 위해서
    # N+1 * N+1
    board = [[0]*(N+1) for _ in range(N+1)]
    center = N // 2
    board[center][center] = 2
    board[center+1][center] = 2
    board[center+1][center] = 1
    board[center][center+1] = 1
    
    # 8방 탐색을 위해서 배열 준비
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    
    # M개의 돌의 위치가 주어진다.
    for i in range(N):
        c, r, color = map(int,input().split())
        # (r, c)에 돌을 놓음
        board[r][c] = color
        # 8방을 탐색하면서, 색깔을 바꿀 수 있는 돌이 있는지 탐색
        
        for d in range(8):
        # 1. 같은 색 돌을 찾고
        # 2. 원래 위치로 돌아오면서 사이에 있는 돌들을 같은 색으로 바꿔버린다.
        # 3. 만약에 같은색 돌을 찾기전 (1번) 빈칸과 범위를 벗어나며 작업 x
        
            # 다음 위치
            nr = r + dr[d]
            nc = c + dc[d]
            while True:
                if nr < 1 or nr > N or nc < 1 or nc > N or board[nr][nc] == 0:
                    # 아무 작업 안함
                    break
                if board[nr][nc] == color:
                    # 원래 자리로 돌아 오면서 색 바꾸기
                    while (nr,nc) != (r,c):
                        nr -= dr[d]
                        nc -= dc[d]
                        board[nr][nc] = color
                    break
                    
                nr += dr[d]
                nc += dc[d]
    # N번 끝나고 나면 흰, 검 개수세기
    w_cnt = 0
    b_cnt = 0
    for i in range(N+1):
        for j in range(N+1):
            if board[i][j] == 2:
                w_cnt += 1
            elif board[i][j] == 1:
                b_cnt += 1