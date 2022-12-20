import sys
sys.stdin = open('rotation2.txt','r')


for tc in range(1,11):
    T = int(input())
    arr = [input() for _ in range(100)]
    result = ''
    max_num = 0
    N = 100

    for i in range(N):
        M = 100
        while M > 0:
            for j in range(N-M+1):
                for k in range(M//2):
                    if arr[i][j+k] != arr[i][j+M-k-1]:
                        break
                else:
                    result = ''
                    for x in range(M):
                        result += arr[i][j+x]
                if max_num < len(result):
                    max_num = len(result)
            M -= 1


    for i in range(N):
        M = 100
        while M > 0:
            for j in range(N-M+1):
                for k in range(M//2):
                    if arr[j+k][i] != arr[j+M-k-1][i]:
                        break
                else:
                    result = ''
                    for x in range(M):
                        result += arr[j+x][i]
            if max_num < len(result):
                max_num = len(result)
            M -= 1
    print(max_num)