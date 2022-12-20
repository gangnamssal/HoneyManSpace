'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
# def dijkstra(s):
#     distance = adj[s][:]
#     visited[s] = 1
#     distance[s] = 0
#     while sum(visited) <= V:
#         minV = 0xffffff
#         min_idx = 0
#         for i in range(V+1):
#             if minV > distance[i] and not visited[i]:
#                 minV = distance[i]
#                 min_idx = i
#         visited[min_idx] = 1
#         for i in range(V+1):
#             if not visited[i] and distance[i] > minV + adj[min_idx][i]:
#                 distance[i] = minV + adj[min_idx][i]
#     return distance
#
# V, E = map(int,input().split())
# adj = [[0xffffff]*(V+1) for _ in range(V+1)]
# for i in range(E):
#     n1,n2,w = map(int,input().split())
#     adj[n1][n2] = w
# visited = [0]*(V+1)
# result = dijkstra(0)
# print(result)

def Dijkstra(s):
    visited[s] = 1
    result = [0xffffff]*(V+1)
    result[s] = 0
    for i in adj[s]:
        result[i[0]] = i[1]
    while sum(visited) <= V:
        min_V = 0xffffff
        min_idx = 0
        for i in range(V+1):
            if not visited[i] and min_V > result[i]:
                min_V = result[i]
                min_idx = i
        visited[min_idx] = 1
        for i in range(len(adj[min_idx])):
            if not visited[adj[min_idx][i][0]] and result[adj[min_idx][i][0]] > min_V + adj[min_idx][i][1]:
                result[adj[min_idx][i][0]] = min_V + adj[min_idx][i][1]
    return result

V, E = map(int,input().split())
adj = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2,w = map(int,input().split())
    adj[n1].append((n2,w))

visited = [0]*(V+1)
result = Dijkstra(0)
print(result)
