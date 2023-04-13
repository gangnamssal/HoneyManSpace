def prim(r,V):
    MST = [0]*(V+1)
    key = [1000]*(V+1)
    key[r] = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if not MST[i] and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1
        for v in range(V+1):
            if not MST[v] and adj[u][v] > 0:
                key[v] = min(key[v],adj[u][v])
    return sum(key)


V, E = map(int,input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    adj[u][v] = w
    adj[v][u] = w