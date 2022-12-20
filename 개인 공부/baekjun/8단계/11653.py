# 정수 N의 소수인수분해
import sys
# N을 입력 받음
N = int(sys.stdin.readline().rstrip('\n'))
# 소인수 분해할 수
number = 2
while N > 1:
    # 나눠서 0이면 출력
    if not N % number:
        N //= number
        print(number)
    else:
        # 안되면 수를 1씩 증가
        number += 1
