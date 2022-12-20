import sys, math
sys.stdin = open('세제곱근을 찾아라.txt','r')

# 양의 정수 N에 대해 N = x^3가 되는 양의 정수 x

# 첫 줄에 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 하나의 정수 N
    N = int(input())
    # 1/3제곱한 것을 result에 담는다.
    result = N**(1/3)
    # 부동소수점 검사를 실시해서 오차가 많이 작으면 반올림해서 출력
    if abs(round(result) - result) <= 1e-9:
        print(f'#{tc} {round(result)}')
    # 아니면 -1을 출력
    else:
        print(f'#{tc} -1')