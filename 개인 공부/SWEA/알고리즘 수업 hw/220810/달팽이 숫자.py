# 1부터 N*N까지의 숫자가 시계 방향으로 있다
# 첫 줄에는 테스트 케이스 개수 T
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     x = 0
#     y = 0
#     move = 0
#     for i in range(1, N*N + 1):
#         arr[x][y] = i
#         x += di[move]
#         y += dj[move]
#         if x < 0 or y < 0 or x >= N or y >= N or arr[x][y] != 0:
#             x -= di[move]
#             y -= dj[move]
#             move = (move + 1) % 4
#             x += di[move]
#             y += dj[move]
#
#     print(f"#{tc}")
#     for row in arr:
#         print(*row)

# 1부터 N*N까지의 숫자가 시계 방향으로 있다
# 첫 줄에는 테스트 케이스 개수 T
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    x, y = 0, 0
    move = 0
    for i in range(1, N**2 + 1):
        arr[x][y] = i
        x += di[move]
        y += dj[move]
        if x < 0 or y < 0 or x >= N or y >= N or arr[x][y] != 0:
            x -= di[move]
            y -= dj[move]
            move = (move + 1) % 4
            x += di[move]
            y += dj[move]
    print(f'#{tc}')
    for k in arr:
        print(*k)


