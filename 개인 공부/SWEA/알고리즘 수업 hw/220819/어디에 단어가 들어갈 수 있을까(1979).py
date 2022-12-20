import sys
sys.stdin = open('1979.txt','r')
# 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력
# 5 <= N <= 15
# 2<= k <= N
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [input().split() for _ in range(N)]
    cnt = 0
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1':
                cnt += 1
            elif arr[i][j] == '0' and cnt == K:
                result += 1
                cnt = 0
            else:
                cnt = 0
        if cnt == K:
            result += 1
        cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[j][i] == '1':
                cnt += 1
            elif arr[j][i] == '0' and cnt == K:
                result += 1
                cnt = 0
            else:
                cnt = 0
        if cnt == K:
            result += 1
        cnt = 0
    print(f'#{tc} {result}')