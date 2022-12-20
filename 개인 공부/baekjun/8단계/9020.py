# 골드바흐 수 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있고 이때 수를 의미
# 골드바흐 파티션 : 짝수를 두 소수의 합으로 나타내는 표현
# 2보다 큰 짝수 n, n의 골드바흐 파티션을 출력하는 프로그램
# 가능한 n의 골드바흐 파티션이 여러가지인 경우 두 소수의 차이가 가장 작은 것을 출력
import sys
# 첫째 줄에 테스트 케이스 T
T = int(sys.stdin.readline())
# 수의 범위 만큼 소수 리스트를 구한다.
prime_num = [1]*10001
# 소수 리스트를 구하는 반복문
for i in range(2,10001):
    if prime_num[i]:
        num = 2
        # 소수가 아닌 수를 0으로 초기화
        while i*num <= 10000:
            prime_num[i*num] = 0
            num += 1
for tc in range(1,T+1):
    # 각 테스트 케이스는 한 줄로 이루어진 짝수
    N = int(sys.stdin.readline())
    # 입력 수보다 작거나 같은 소수 중
    # 하나씩 확인해서 합이 적용되는 소수를 찾는다.
    result1 = 0     # 첫 번째 소수
    result2 = 0     # 두 번째 소수
    min_num = 10000 # 최솟 값을 찾기 위한 변수
    for i in range(2,N+1):
        # 소수라면
        if prime_num[i]:
            # 첫 번째 값으로 정함
            first_num = i
            # 두 번째 값은 N - 소수
            second_num = N - i
            # 두 번째 값이 소수가 아니면 다시 검사
            if prime_num[second_num] and min_num > abs(first_num - second_num):
            # 둘다 소수인데  최소값이면 저장, 최솟값이 0이면 바로 출력
                if not min_num:
                    break
                min_num = abs(first_num - second_num)
                result1 = first_num
                result2 = second_num
    print(f'{result1} {result2}')