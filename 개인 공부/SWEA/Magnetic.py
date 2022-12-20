import sys
sys.stdin = open('Magnetic.txt', 'r')
for tc in range(1, 11):
    N = int(input())
    # 1은 N극 성질, 2는 S극 성질
    # 위에 N극, 밑에 S극
    arr = [list(map(int,input().split())) for _ in range(100)]
    cnt = 0

    for i in range(N):
        stack = []
        for j in range(N):
            if arr[j][i] == 1 and not stack:
                stack.append(1)
            elif stack and arr[j][i] == 2:
                stack.pop()
                cnt += 1

    print(f'#{tc} {cnt}')
