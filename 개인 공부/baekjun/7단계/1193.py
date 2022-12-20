import sys
# 첫 줄에는 x가 주어진다.
N = int(sys.stdin.readline())
n = 1  # j번째까지의 합
i = 1 # j의 인덱스
while n < N:
    i += 1
    n += i
n -= i
i -= 1
# 사선 위, 사선 아래
di = [-1, 1]
dj = [1, -1]
if (i+1)%2:
    x, y = i+1, 1
    for i in range(N-n-1):
        x += di[0]
        y += dj[0]
else:
    x, y = 1, i + 1
    for i in range(N-n-1):
        x += di[1]
        y += dj[1]
print(f'{x}/{y}')