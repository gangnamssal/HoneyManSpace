import sys
sys.stdin = open('간단한 369 게임.txt','r')

# 입력으로 정수 N이 주어짐
# 박수를 치는 부분에 '-'출력
# 박수를 두번 칠 때는 '--'

# 정수 N
N = int(input())
for i in range(1, N+1):
    cnt = 0
    for k in str(i):
        if k in '369':
            cnt += 1
    if cnt == 0:
        result = f'{i}'
    else:
        result = '-'*cnt
    print(f'{result}', end=' ')
