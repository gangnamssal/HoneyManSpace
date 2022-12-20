import sys
sys.stdin = open('하나로.txt','r')
# 모든 섬을 해저터널로 연결
# 환경 부담금 = E(환경 부담 세율) * L(각 해저터널 길이)^2
# 환경 부담금을 최소로 하며 모든 섬을 연결, 길이를 최소
def prim(s):
    MST = [0xfffffffffffffffff]*N
    check = [0]*N
    MST[s] = 0
    check[s] = 1
    for i in range(N):
        MST[i] = ((rocate[s][0] - rocate[i][0])**2 + (rocate[s][1] - rocate[i][1])**2)
    while sum(check) < N:
        min_val = 0xffffffffffffffff
        min_idx = 0
        for i in range(N):
            if not check[i] and min_val > MST[i]:
                min_val = MST[i]
                min_idx = i
        check[min_idx] = 1
        for i in range(N):
            if not check[i]:
                value = ((rocate[min_idx][0] - rocate[i][0]) ** 2 + (rocate[min_idx][1] - rocate[i][1]) ** 2)
                if MST[i] >value:
                    MST[i] = value
    return round(sum(MST)*E)

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 섬의 개수 N
    N = int(input())
    # 정수인 x좌표
    X = list(map(int,input().split()))
    # 정수인 y좌표
    Y = list(map(int,input().split()))
    # 환경 부담 세율
    E = float(input())
    rocate = []
    for i in range(N):
        rocate.append([X[i], Y[i]])
    print(f'#{tc} {prim(0)}')
