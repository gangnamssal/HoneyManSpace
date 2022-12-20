# M, N이 주어질 때 M이상 N이하의 소수의 합과 최소 소수를 출력
import sys
M = int(sys.stdin.readline().rstrip('\n'))
N = int(sys.stdin.readline().rstrip('\n'))
result = []
for i in range(M,N+1):
    for j in range(2,i):
        if not i % j:
            break
    else:
        if i != 1:
            result.append(i)

if not result:
    print(-1)
else:
    print(sum(result))
    print(result[0])