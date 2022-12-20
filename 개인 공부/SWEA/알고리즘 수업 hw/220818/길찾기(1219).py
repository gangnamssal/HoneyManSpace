import sys
sys.stdin = open('find_road.txt','r')
# A = 0, B = 99
# 첫 줄에는 테스트 케이스의 번호와 길의 총 개수
for tc in range(1, 11):
    T, V = map(int,input().split())
    # 순서쌍이 주어진다.
    route = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        route[arr[i]].append(arr[i+1])
    # 시작점
    top = -1
    stack = [0]*100
    visited = [0]*100
    top += 1
    stack[top] = 0
    visited[0] = 1
    result = 0
    while top > -1:
        # 인접한 지점을 찾는다.
        if stack[top] == 99:
            result = 1
            break
        for i in route[stack[top]]:
            if not visited[i]:
                top += 1
                stack[top] = i
                visited[i] = 1
                break
        else:
            top -= 1
    print(f'#{tc} {result}')