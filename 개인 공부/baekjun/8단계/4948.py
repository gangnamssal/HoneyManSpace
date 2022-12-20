# 입력은 여러 개의 테스트 케이스
# 입력의 마지막에는 0
# n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구함
import math
n_lst = [1 for _ in range(2 * 123456+1)]  # 입력의 2배 크기의 리스트를 만듬
for i in range(2, int(math.sqrt(123456 * 2)) + 1):
    if i:  # 소수가 아닌 수
        start = 2  # 소수의 배수는 걸러낸다.
        while i * start <= 2 * 123456:
            n_lst[i * start] = 0
            start += 1
while True:
    n = int(input())    # 입력을 받음
    if not n:
        break
    if n == 1:
        print(1)
    else:
        print(n_lst[n+1:2*n+1].count(1))


