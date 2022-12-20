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



T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    adj = [[987654321]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
    print(dijkstra(0))