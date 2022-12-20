import sys
sys.stdin = open('BFS_DFS_TEST.txt','r')

def bfs(start, end):
    visited = [0]*100
    q = [0]*(length*2)
    front = rear = -1

    rear += 1
    q[rear] = start
    visited[rear] = 1

    while front != rear:
        front += 1
        if q[front] == end:
            return 1
        for i in board[q[front]]:
            if not visited[i]:
                rear += 1
                q[rear] = i
                visited[i] = 1
    return 0



for tc in range(1,11):
    N, length = map(int,input().split())
    arr = list(map(int,input().split()))

    board = [[]*_ for _ in range(100)]
    # 좌표를 저장한다.
    for i in range(length):
        x, y = arr[2*i], arr[2*i + 1]
        board[x].append(y)
    visited = [0] * 100
    stack = [0] * 100
    print(f'#{tc} {bfs(0, 99)}')