import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt','r')

# 4*4 크기의 격자판, 0~9 사이의 숫자가 적혀있다.
# 임의의 위치에서 시작, 4방향으로 인접한 격자로 총 여섯 번 이동후
# 이어붙이면 7자리 수
# 한 번 거쳤던 격자 칸을 다시 거쳐도 된다.
def solve(r,c,cnt,char):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    if cnt == 7:
        check.append(char)
        return
    elif r < 0 or c < 0 or r > 3 or c > 3:
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            solve(nr,nc,cnt+1,char+data[r][c])

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    data = [input().split() for _ in range(4)]
    check = []
    for i in range(4):
        for j in range(4):
            solve(i,j,0,'')

    print(f'#{tc} {len(set(check))}')
