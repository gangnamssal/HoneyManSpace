
# N*N 칸, 오른쪽 아랫쪽만 이동 가능
# 최소합 구하기
def solve(r, c, v):
    global result
    if r == N or c == N:
        return
    else:
        if v > result:
            return
        # 오른쪽 or 아랫쪽으로만 이동
        solve(r+1, c, v+data[r][c])
        solve(r, c+1, v+data[r][c])
        if r == N-1 and c == N-1:
            if result > v:
                result = v
            return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 최솟값을 구하는 변수
    result = 5000000
    solve(0,0,0)
    print(f'#{tc} {result+data[N-1][N-1]}')

