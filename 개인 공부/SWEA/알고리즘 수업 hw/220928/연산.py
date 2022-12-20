# 자연수 N에 몇 번의 연산을 통해 M을 만들 수 있는가
# 사용할 수 있는 연산 +1, -1, *2, -10
def bfs(N, M):
    while queue:
        # 큐에서 하나씩 꺼내 목표 값이랑 같은지 비교
        queue.pop(0)
        if queue[0][0] == M:
            result = queue[0][1]
            break
        # 다르면 다시 큐의 값을 계산하여 큐의 뒤에 삽입
        # 이것을 반복하면서 계속 값을 비교
        for i in queue:
            for j in numbers:
                if j == 2 and i[0] * j > 0 and i[0] * j <= M + 1 and not visited[i[0] * j]:
                    visited[i[0] * j] = 1
                    queue.append([i[0] * j, i[1] + 1])
                else:
                    if i[0] + j > 0 and i[0] + j <= M + 1 and not visited[i[0] + j]:
                        visited[i[0] + j] = 1
                        queue.append([i[0] + j, i[1] + 1])
            else:
                break
    return result


# 첫 줄에 테스트케이스의 개수
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = [1, -1, 2, -10]
    # 큐에 N을 최초로 계산한 값을 넣고 시작한다.
    queue = [[N + 1, 1], [N - 1, 1], [N * 2, 1], [N - 10, 1]]
    # 이미 계산된 숫자가 있는지 판단하는 리스트
    visited = [0]*1000001
    for i in queue:
        visited[i[0]] = 1
    print(f'#{tc} {bfs(N, M)}')
