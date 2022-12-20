import sys
sys.stdin = open('퍼펙트 셔플.txt','r')

# 퍼펙트 셔플하면 어떤 순서가 되는지 출력
# N이 홀수이면 교대로 놓을 때 먼저 놓는 쪽에 한장 더 들어간다.
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = input().split()
    result = ['']*N
    if N % 2:
        for i in range(N // 2):
            result[i * 2 + 1] = arr[N // 2 + i+1]
            result[i * 2] = arr[i]
        else:
            result[-1] = arr[N//2]
    else:
        for i in range(N//2):
            result[i*2+1] = arr[N//2+i]
            result[i*2] = arr[i]
    print(f'#{tc}', *result)