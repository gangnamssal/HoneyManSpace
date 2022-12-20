import sys
sys.stdin = open('정사각형 방.txt','r')
# N^2개의 방이 N*N형태로 있다.
# i,j에는 1 이상 N^2 이하의 수 Aij가 적혀있다.
# 이 숫자는 모든 방에 대해 서로 다르고 다른 방으로 이동할 수 있다.
# 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에
# 적힌 숫자보다 정확히 1 더 커야한다.

# 첫 번째 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 첫 번째 줄에는 정수 N
    N = int(input())
    # 다음 N개의 줄에는 N개의 정수
    room = [list(map(int, input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    max_num = 0
    lst = []
    for i in range(N):
        for j in range(N):
            r, c = i, j
            cnt = 1
            while True:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and room[ni][nj] - room[i][j] == 1:
                        i = ni
                        j = nj
                        cnt += 1
                        break
                else:
                    break
            lst.append([cnt,room[r][c]])
    lst.sort(key=lambda x:[-x[0],x[1]])
    print(f'#{tc} {lst[0][1]} {lst[0][0]}')


       # 최소값에서 사방을 판단

