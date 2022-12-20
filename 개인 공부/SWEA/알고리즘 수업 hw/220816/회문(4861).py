# 회문을 찾아라
# 첫 줄에 테스트 케이스 갯수 T
import sys
sys.stdin = open('4861.txt','r')
T = int(input())
for tc in range(1,T+1):
    # 크기 N * N, 회문 길이 M
    N, M = map(int,input().split())
    strs = [input() for _ in range(N)]

    result = ''
    for i in strs:
        for j in range(N-M+1):
            for k in range(M//2):
                if i[j+k] != i[j+M-k-1]:
                    break
            else:
                for x in range(M):
                    result += i[j+x]

    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if strs[j+k][i] != strs[j+M-k-1][i]:
                    break
            else:
                for x in range(M):
                    result += strs[j+x][i]
    print(f'#{tc} {result}')
        