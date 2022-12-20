import sys
sys.stdin = open('최대상금.txt','r')
# 주어진 숫자판들 중 2개를 선택해 정해진 횟수만큼 자리를 교환
# 왼쪽부터 10^N 자리
# 주어진 횟수만큼 교환이 이루어져야하고 동일한 위치의 교환이 가능

# 수를 계산하는 함수
# cnt : 몇 번 바꿨는지 보는 변수
def solve(cnt):
    global maxV
    if cnt == change:
        result = ''.join(numbers)
        if maxV < int(result):
            maxV = int(result)
        return
    # change번 교환을 해야한다.
    # 자리를 바꾸고 그 다음 자리부터 다시 바꿔야한다.
    # 자리를 바꾼 값을 check해서 중복된 값이 없도록 한다.
    else:
        for i in range(N):
            for j in range(i+1,N):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                char = ''.join(numbers)
                if char not in check[cnt]:
                    check[cnt].append(char)
                    solve(cnt+1)
                numbers[i], numbers[j] = numbers[j], numbers[i]


# 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 숫자판의 정보 - 정수형 숫자 최대 6자리, 최대 교환 횟수 10번
    numbers, change = map(str,input().split())
    # number의 문자열을 숫자로 바꿔 리스트에 저장
    numbers = list(map(str,numbers))
    N = len(numbers)
    change = int(change)
    check = [[] for _ in range(10)]
    maxV = 0
    solve(0)
    print(f'#{tc} {maxV}')
