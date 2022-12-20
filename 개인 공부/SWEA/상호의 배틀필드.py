import sys
sys.stdin = open('상호의 배틀필드.txt','r')
'''
문자	의미
.	    평지(전차가 들어갈 수 있다.)
*	    벽돌로 만들어진 벽
#	    강철로 만들어진 벽
-	    물(전차는 들어갈 수 없다.)
^	    위쪽을 바라보는 전차(아래는 평지이다.)
v	    아래쪽을 바라보는 전차(아래는 평지이다.)
<	    왼쪽을 바라보는 전차(아래는 평지이다.)
>	    오른쪽을 바라보는 전차(아래는 평지이다.)
-----------------------------------------------
U	    Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	    Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	    Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	    Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	    Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
'''
# 포탄은 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진
# 포탄이 벽에 부딪히면 포탄은 소멸하고, 부딪힌 벽이 벽돌로 만들어진 벽이라면 이 벽은 파괴되어 칸은 평지
# 강철로 만들어진 벽에 포탄이 부딪히면 아무 일도 일어나지 않는다

T = int(input())
for tc in range(1, T+1):
    # 높이, 너비
    H, W = map(int, input().split())
    maap = [list(input()) for _ in range(H)]
    # 넣을 입력의 개수
    N = int(input())
    command = input()
    command_dict = {'U': (0, '^'), 'D': (1,'v'), 'L': (2,'<'), 'R': (3,'>')}
    command_idx = [[-1,0],[1,0],[0,-1],[0,1]]
    for i in range(H):
        for j in range(W):
            if maap[i][j] in '^v<>':
                x, y = i, j
    dx = x + command_idx[command_dict[maap[x][y]][0]]
    dy = y + command_idx[command_dict[maap[x][y]][0]]
    print(dx, dy)
    # for i in command:
    #     if i == 'S':
    #         while True:
    #             dx, dy = x + command_idx[command_dict[maap[x][y]][0]], y + command_idx[command_dict[maap[x][y]][0]]
    # print(maap)
            


