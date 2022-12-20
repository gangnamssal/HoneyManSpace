import sys
sys.stdin = open('1974.txt','r')
# 9*9
# 겹치는 숫자가 없을 경우 1 아니면 0 출력
T = int(input())
for tc in range(1, T+1):
    # 스도쿠를 2차원 배열로 받음
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 스도쿠의 중복 숫자를 세는 변수
    counts = [0] * 10
    # 스도쿠의 중복 숫자가 있으면 저장하는 변수
    result = [1, 1]
    is_sdoqu = 1
    # 가로 세로의 중복 숫자를 구함
    for i in range(9):
        for j in range(9):
            counts[arr[i][j]] += 1
            counts[arr[j][i]] += 1
        # 가로 세로랑 네모칸을 비교하기 위한 네모칸 구하는 for 문
        for a in range(0,7,2):
            for b in range(0,7,2):
                for c in range(3):
                    for d in range(3):
                        counts[arr[a+c][b+d]] += 1
                # 만약에 숫자의 수가 다르다면 0을 출력해서 스도쿠가 아님을 증명
                for x in range(1, 9):
                    if counts[x] != counts[x + 1]:
                        result[1] = 0
                break
            break
    if 0 in result:
        is_sdoqu = 0
    print(f'#{tc} {is_sdoqu}')