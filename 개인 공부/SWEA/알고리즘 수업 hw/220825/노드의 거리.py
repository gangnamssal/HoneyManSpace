import sys
sys.stdin = open('5102.txt','r')

# v개의 노드 개수와 E개의 간선 정보
# 몇 개의 간선을 지나치는지 구하라

def bfs(start, end):

    q = [0] * 1001
    front = rear = -1
    rear += 1
    q[rear] = start
    visited[start] = 1

    while front != rear:
        front += 1
        head = q[front]
        if head == end:
            return visited[head] - 1
        for i in road_arr[head]:
            if not visited[i]:
                visited[i] = 1 + visited[head]
                rear += 1
                q[rear] = i
    return 0


T = int(input())
for tc in range(1,T+1):
    v, E = map(int,input().split())
    road = [list(map(int,input().split())) for i in range(E)]
    # 출발, 도착
    S, G = map(int,input().split())
    road_arr = [[] for _ in range(v+1)]
    visited = [0] * 1001
    for x, y in road:
        road_arr[x].append(y)
        road_arr[y].append(x)

    print(f'#{tc} {bfs(S,G)}')