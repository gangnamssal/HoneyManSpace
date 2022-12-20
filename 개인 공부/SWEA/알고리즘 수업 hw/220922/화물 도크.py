import sys
sys.stdin = open('화물 도크.txt','r')

# 0시부터 다음날 0시 이전까지 최대 몇 대의 화물차가 이용할 수 있는지
# def solve(r):
#     global cnt, maxV
#     for i in range(data[r][0],data[r][1]):
#         if check[i]:
#             if maxV < cnt:
#                 maxV = cnt
#             return
#     else:
#         for i in range(data[r][0], data[r][1]):
#             check[i] += 1
#         cnt += 1
#         for j in range(N):
#             solve(j)
#         cnt -= 1
#         for i in range(data[r][0], data[r][1]):
#             check[i] -= 1
#
#
# # 테스트케이스
# T = int(input())
# for tc in range(1,T+1):
#     # 신청서 N
#     N = int(input())
#     # 작업 시간 s, 종료 시간 e
#     data = [list(map(int,input().split())) for _ in range(N)]
#     # 작업을 시작하는 시간을 체크
#     check = [0]*25
#     maxV = 0
#     for i in range(N):
#         cnt = 0
#         solve(i)
#     print(f'#{tc} {maxV}')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 끝나는 시간 순으로 정렬
    data.sort(key=lambda x: x[1])
    e = data[0][1]
    cnt = 1
    for i in range(1, N):
        if data[i][0] >= e:
            e = data[i][1]
            cnt += 1

    print(f'#{tc} {cnt}')