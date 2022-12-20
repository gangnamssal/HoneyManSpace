# 한번 충전으로 이동할 수 있는 정류장 수가 정해져있음
# 중간에 충전기가 설치된 정류장을 만듦
# 0에서 N까지 이동
# 한번 충전으로 최대 K 정류장을 이동
# 충전기가 설치된 M개의 정류장 번호
# 최소 몇 번을 충전해야 종점에 도착
# 충전기 설치가 잘못되어 종점에 도착 못하면 0 출력
# 출발지에서 항상 충전기가 설치, 갯수에 포함 x

# 첫 줄에 노선 수 T
T = int(input())
for tc in range(1,T+1):
    # K = 한번 충전으로 최대 이동 거리, N = 전체 이동 거리 , M = 충전기 설치 갯수
    K, N, M = map(int,input().split())
    # M개의 정류장 번호
    M_num = list(map(int,input().split()))
    # K 만큼 이동하는데 그  사이 인덱스에 충전기가 없으면 실패 있으면 1번 충전
    # 마지막 도착은 충전 안해도 괜찮음
    cnt = 0 # 충전 횟수를 누적하는 변수
    bus = 0 # 버스의 현재 위치
    for i in range(len(M_num)-1):
        if (bus + K) < M_num[i]:
            cnt = 0
            break
        if (bus + K) >= M_num[i+1]:
            bus = M_num[i+1]
            cnt += 1
            i += 1
        elif (bus + K) < M_num[i+1]:
            if bus >= N:
                break
            bus = M_num[i]
            cnt += 1       
        if bus + K >= N:
                break
    print(f'#{tc} {cnt}')
----------------------------------------------------

# 방법 1
T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    battery = list(map(int,input().split()))

    stations = [0]*N # 인덱스에 해당하는 정류소에 충전소가 있으면 1, 없으면 0
    for idx in battery:
        stations[idx] = 1

    cnt = 0 #충전 횟수 저장 변수
    position = 0 # 현재 위치    
    # 가능한 멀리 가는 동작을 반복
    while True:
        # 멀리있는 충전소 찾아서 이동하기
        # 내가 갈 수 있는 최대 위치 : K + position
        # position + K : 도착 지점 이상이라면 이동할 필요 x
        position += K
        if position >= N:
            break # 도착지에 도착
        #가장 멀리 있는 충전소 찾기

        for i in range(position,position-K,-1):
            if stations[i] == 1: # 충전소가 있음
                cnt += 1
                position = i
                break # 충전소 찾기 중단
        else: # break가 안걸리면 충전소가 없다.
            cnt = 0
            break # 다음 칸으로 이동하는 반복 중단

    print(f'#{tc} {cnt}')
                 
# 방법 2
T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    stations = list(map(int,input().split()))
    #일단 갈 수 있으면 지나쳐 가고, 갈 수 없으면 이전에 충전
    stations.insert(0,0)
    stations.append(N)
    position = 0
    cnt = 0
    for i in range(1,M+2): # 0번 빼고, 2개 추가했으니 M+2
        # i-1번에서 i번으로 이동 불가할 때
        if (stations[i] - stations[i-1]) > K:
            cnt = 0
            break
        # i-1번에서 i번으로 충전하면 올 수 있는 상황
        #그런데 이 시점에서 현재 위치에서는 i번으로 못온다면
        if stations[i] > position + K:
            position = stations[i-1]
            cnt += 1
        # else는 아무 작업 안해도 된다.
    print(f'#{tc} {cnt}')