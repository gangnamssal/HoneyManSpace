import sys
sys.stdin = open('typing.txt','r')
# 테스트 케이스 
T = int(input())
for _ in range(1,T+1):
    strs1, strs2 = input().split()
    N = len(strs1)
    M = len(strs2)
    i = 0
    j = 0
    cnt = 0

    while i < N and j < M:
        if strs1[i] != strs2[j]:
            cnt += 1
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == M:
            cnt += 1
            j = 0
    print(f'#{_} {cnt}')


