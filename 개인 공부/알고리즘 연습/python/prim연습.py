def prim(s):
    MST = [0xffffff]*(V+1)
    check = [0]*(V+1)
    MST[s] = 0
    check[s] = 1
    for i in range(V+1):
        if not check[i] and adj[s][i] < MST[i]:
            MST[i] = adj[s][i]

    while sum(check) < V+1:
        min_idx = 0
        min_val = 0xffffff
        for i in range(V+1):
            if not check[i] and MST[i] < min_val:
                min_val = MST[i]
                min_idx= i
        check[min_idx] = 1
        for j in range(V+1):
            if not check[j] and MST[j] > adj[min_idx][j]:
                MST[j] = adj[min_idx][j]
                # MST[min_idx] = min_val
    return sum(MST)




T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    adj = [[0xffffff]*(V+1) for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    print(f'#{tc} {prim(0)}')
