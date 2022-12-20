# 어느 사다리를 고르면 X표시에 도착하게 되는지 구함
# 출발점 x = 100
# 사다리 1 도착지점 2
# 테스트 케이스 T
import sys
from unittest import result
sys.stdin = open('ladder.txt', 'r')
for tc in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    # 아래 왼 오 위
    ti = [1,0,0,-1]
    tj = [0,-1,1,0]
    # 도착지에서 위로 올라간다.
    x = 99
    y = 0
    move = 3
    # 도착지 2에서 출발한다.
    for i in range(100):
        if arr[99][i] == 2:
            y = i
    while x != 0:
        x += ti[move]
        y += tj [move]
        if 0<= y - 1 and arr[x][y-1] != 0 and move != 2:
            move = 1
        elif  y + 1 < 100 and arr[x][y+1] != 0 and move != 1:
            move = 2
        else:
            move = 3
    print(f'#{tc} {y}')           

