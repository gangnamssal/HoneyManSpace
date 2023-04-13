# DFS 재귀로 구현
import sys
sys.stdin = open('BFS_DFS_TEST.txt','r')

# def dfs(v, E, top, visited): # 시작, 찾는 값, 개수
#     stack[top] = v
#     if stack[top] == E:
#          return 1
#     result = 0
#     for i in board[stack[top]]:
#         if not visited[i]:
#             visited[i] = 1
#             result += dfs(i, E, top + 1, visited)
#     return result
# 
# 
# for tc in range(1,11):
#     N, length = map(int,input().split())
#     arr = list(map(int,input().split()))
# 
#     board = [[]*_ for _ in range(100)]
#     # 좌표를 저장한다.
#     for i in range(length):
#         x, y = arr[2*i], arr[2*i + 1]
#         board[x].append(y)
#     visited = [0] * 100
#     stack = [0] * 100
#     print(f'#{tc} {dfs(0, 99, -1, visited)}')

#----------------------------------------------------------#
# DFS 반복문 구현
def dfs(v, E):
    visited = [0] * 100
    stack = [0] * 100
    top = -1

    top += 1
    stack[top] = v
    visited[v] = 1

    while top > -1:
        if stack[top] == E:
            return 1
        for i in board[stack[top]]:
            if not visited[i]:
                top += 1
                stack[top] = i
                visited[i] = 1
                break
        else:
            top -= 1
    return 0

for tc in range(1,11):
    N, length = map(int,input().split())
    arr = list(map(int,input().split()))

    board = [[]*_ for _ in range(100)]
    # 좌표를 저장한다.
    for i in range(length):
        x, y = arr[2*i], arr[2*i + 1]
        board[x].append(y)
    print(f'#{tc} {dfs(0, 99)}')
#-------------------------------------------------------#