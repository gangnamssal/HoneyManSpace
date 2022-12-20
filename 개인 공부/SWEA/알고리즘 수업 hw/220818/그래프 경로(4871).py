import sys
sys.stdin = open('4871.txt','r')
# 첫 줄에 테스트 케이스
# 둘째 줄에 V, E
# 마지막 줄에 S G
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    route = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        route[a].append(b)
    S, G = map(int, input().split())
    top = -1
    stack = [0]*V
    visited = [0]*(V+1)
    top += 1
    stack[top] = S
    visited[S] = 1
    result = 0
    while top > -1:
        if stack[top] == G:
            result = 1
            break
        for i in route[stack[top]]:
            if visited[i] == 0:
                visited[i] = 1
                top += 1
                stack[top] = i
                break
        else:
            top -= 1
    print(f'#{tc} {result}')


