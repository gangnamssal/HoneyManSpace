import sys
sys.stdin = open('디저트 카페.txt','r')

# 디저트 카페를 방문
# 대각선으로만 이동 가능
# 같은 숫자의 카페는 갈 수 없음
# 투어를 마치고 다시 돌아와야 한다.
# 디저트를 먹을 수 없는 경우 -1
# 테스트 케이스
def solve(r,c,i):
    global maxV
    dr = [-1,1,1,-1]
    dc = [1,1,-1,-1]

    if 0<= r <N and 0<= c < N and visited and (r,c,data[r][c]) == visited[0] and maxV < len(visited) and len(visited) >= 3:
        maxV = len(visited)
        return
    elif r < 0 or c < 0 or r >= N or c >= N or check[data[r][c]] >= 1 or (r,c,data[r][c]) in visited:
        return
    else:
        for q in range(i,4):
            nr = r + dr[q]
            nc = c + dc[q]
            visited.append((r,c,data[r][c]))
            check[data[r][c]] += 1
            solve(nr,nc,q)
            check[data[r][c]] -= 1
            visited.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = []
    maxV = -1
    for i in range(N):
        for j in range(N):
            check = [0]*101
            solve(i,j,0)
    print(maxV)



# def solve(r,c,cnt):
#     global maxV
#     dr = [-1,1,1,-1]
#     dc = [1,1,-1,-1]
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if nr < 0 or nc < 0 or nr > N or nc > N:
#             return
#         elif visited and (nr,nc) == visited[0] and check[data[nr][nc]] and maxV < cnt:
#             maxV = cnt+1
#             return
#         visited.append((r,c))
#         check[data[r][c]] += 1
#         solve(nr,nc,cnt)
#         visited.pop()
