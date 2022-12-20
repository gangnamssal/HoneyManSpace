import sys
sys.stdin = open('5099.txt','r')

# 1~M까지 M개의 피자를 순서대로 화덕에 넣음
# 1번에서 넣거나 뺄 수 있음
# 처음 뿌려진 치즈의 양이 주어지고
# 한 바퀴 돌 떄 녹지 않는 치즈는 반으로 줄어듬
# C = C //2
# 치즈가 0이 되면 다 꺼냄

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # 화덕의 크기 N, 피자 개수 M
    N, M = map(int, input().split())
    # 치즈의 양 ci
    ci = list(map(int, input().split()))
    room = []*N
    idx = [_ for _ in range(1, N+1)]
    for i in range(N):
        room.append(ci.pop(0))
    idx_num = 1
    while len(room) > 1:
        for i in range(len(room)):
            if len(room) == 1:
                break
            elif ci and (room[0] // 2) == 0:
                room.pop(0)
                idx.pop(0)
                room.append(ci.pop(0))
                idx.append(N + idx_num)
                idx_num += 1
            elif (room[0] // 2) == 0 and not ci:
                room.pop(0)
                idx.pop(0)
            else:
                room.append(room.pop(0) // 2)
                idx.append(idx.pop(0))
    print(f'#{tc}',*idx)

