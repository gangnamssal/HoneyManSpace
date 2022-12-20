# E개의 일방통행 구간
# 0~N번
# 0~N 지점까지 최소한의 거리
def dijkstra(start):
    distance = adj[start][:]
    visited = [0]*(N+1)
    visited[start] = 1
    distance[start] = 0
    while sum(visited) <= N:
        min_idx = 0
        min_val = 0xffffff
        for i in range(N+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        visited[min_idx] = 1
        for i in range(N+1):
            if not visited[i] and distance[i] > min_val + adj[min_idx][i]:
                distance[i] = min_val + adj[min_idx][i]
    return distance

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 마지막 연결 지점 번호 N, 도로의 개수 E
    N ,E = map(int,input().split())
    # 인접 리스트
    adj = [[0xfffffff]*(N+1) for _ in range(N+1)]
    # 시작 s, 끝 e, 구간 거리 w
    for i in range(E):
        s, e, w = map(int,input().split())
        adj[s][e] = w
    print(f'#{tc} {dijkstra(0)[N]}')
