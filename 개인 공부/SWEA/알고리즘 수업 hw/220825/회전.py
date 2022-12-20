import sys
sys.stdin = open('5097.txt','r')

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # N개의 숫자 수열, M번 작업
    N, M = map(int,input().split())
    # 10억 이하의 자연수 N개
    num_lst = list(map(int, input().split()))

    for i in range(M+1):
        num_lst.append(num_lst.pop(0))
    print(f'#{tc} {num_lst[-1]}')
