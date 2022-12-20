import sys
sys.stdin = open('2001.txt','r')
# 파리 영역 5<= N <= 15
# 파리채 영역 2<= M <=N
# 파리 갯수는 30이하
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_num = 0
    sum_num = 0
    for i in range(N-M+1):
        sum_num = 0
        for j in range(N-M+1):
            sum_num = 0
            for k in range(M):
                for l in range(M):
                    sum_num += arr[i+k][j+l]
            if max_num < sum_num:
                max_num = sum_num
    print(f'#{tc} {max_num}')


