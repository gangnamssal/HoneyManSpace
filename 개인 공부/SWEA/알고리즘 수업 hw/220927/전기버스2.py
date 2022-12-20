import sys
sys.stdin = open('전기버스2.txt','r')

# 충전지마다 최대로 운행할 수 있는 정류장 수가 있다.
# 마지막 정류장에는 배터리가 없다.

# 테스트 케이스 T
T = int(input())
for tc in range(1,T+1):
    # 정류장 수 N, 정류 별 배터리 Mi
    N, *Mi = map(int,input().split())
    ride = [0]*(N-1)
    for i in range(N-1):
        ride[i] = Mi[i]+i
    start = 0
    cnt = 0
    while start < N-1:
        maxV = 0
        if ride[start] >=N-1:
            break
        for i in range(start,ride[start]+1):
            if maxV <= ride[i]:
                maxV = ride[i]
                start = i
        cnt += 1
    print(f'#{tc} {cnt}')
