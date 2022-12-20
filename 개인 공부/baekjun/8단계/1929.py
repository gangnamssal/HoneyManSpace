# M이상 N이하의 소수를 모두 출력
import math
m,n = map(int,input().split())
l = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지
    if l[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            l[i * j] = False
            j += 1
# 모든 소수 출력
for i in range(m, n + 1):
    if l[i]:
        if i != 1:
            print(i)