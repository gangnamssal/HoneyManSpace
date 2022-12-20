import sys
sys.stdin = open('홈 방범 서비스.txt','r')
# 운영 비용 = K*K + (K - 1)*(K - 1)
# 서비스를 제공받는 집들은 각각 M의 비용을 지불할 수 있다.
# 도시의 크기 5<= N <= 20
# 지불 비용 1<= M <= 10
# 집이 있는 위치는 1, 나머지는 0

# 손익계산하는 함수
def service(r,c,k):
    cnt = 0
    colume = -1
    for x in range(r-(k-1),r+k):
        if x <= r:
            colume += 1
            for y in range(c-colume,c+colume+1):
                if 0<= x < N and 0<= y < N and city[x][y]:
                    cnt += 1
        elif x > r:
            colume -= 1
            for y in range(c-colume,c+colume+1):
                if 0<= x < N and 0<= y < N and city[x][y]:
                    cnt += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    # 도시의 크기 N, 비용 M
    N, M = map(int,input().split())
    # 도시 정보
    city = [list(map(int,input().split())) for _ in range(N)]
    # 손해를 보지 않으면서 서비스를 가장 많이 제공한 집을 저장하는 변수
    result = 0
    # 집 갯수를 저장하는 변수
    home = 0
    # 총 집의 갯수를 찾음
    for i in range(N):
        for j in range(N):
            if city[i][j]:
                home += 1
    # 집이 있는 위치를 찾음
    for i in range(N):
        for j in range(N):
            # 집이 존재하면 집 주위로 서비스 영역을 넓히면서 손익계산
                k = 1
                while True:
                    # 운영비용
                    cost = k*k + (k - 1)*(k - 1)
                    earn = service(i,j, k)
                    if earn > home or cost > home * M:
                        break
                    if earn*M - cost >= 0 and result < earn:
                        result = earn
                    k += 1
    print(f'#{tc} {result}')