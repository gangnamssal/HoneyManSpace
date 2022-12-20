import sys
sys.stdin = open('달란트.txt','r')

# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    num_lst = [N // P] * P
    rest = N % P
    result = 1
    for i in range(rest):
        num_lst[i] += 1
    for i in range(len(num_lst)):
        result *= num_lst[i]
    print(f'#{tc} {result}')