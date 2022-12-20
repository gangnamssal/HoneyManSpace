import sys
sys.stdin = open('농작물 수확하기.txt', 'r')
# 농장의 크기는 항상 홀수
# 수확은 항상 농장의 크기에 맞는 정사각형 마름모 형태로만 가능

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    result = 0
    middle = N//2
    for i in range(middle+1):
        for k in range(middle-i, middle+i+1):
            result += farm[i][k]

    for i in range(middle):
        for k in range(i+1, N-i-1):
            result += farm[i+middle+1][k]
    print(f'#{tc} {result}')