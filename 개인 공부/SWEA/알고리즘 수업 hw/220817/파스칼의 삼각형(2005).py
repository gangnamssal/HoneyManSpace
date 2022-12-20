# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', end='')
    for i in range(N+1):
        for j in range(i):
            if i <= 2:
                print('1', end=' ')
            else:
                if j == 0 or j == i-1:
                    print('1', end=' ')
                else:
                    print(f'{i-1}', end=' ')
        print()
