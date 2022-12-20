import sys
sys.stdin = open('장훈이의 높은 선반.txt','r')

# 각 점원의 키는 Hi, 높이 B
# 각 점원의 키 합이 B가 되어야 한다.
# 부분 집합을 구해서 값을 비교하는 함수
def solve(num):
    global minV
    if num == N:
        result = 0
        # 부분 집합의 결과를 키와 매치하여 값을 비교하는 과정
        for i in range(N):
            if part_set[i]:
                result += Hi[i]
        if result >= B and result - B < minV:
            minV = result - B
        return
    else:
        # 부분 집합을 구하는 부분
        for i in range(2):
            part_set[num] = i
            solve(num+1)

# 첫 번째 줄에 테스트 케이스 T
T = int(input())
for tc in range(1,T+1):
    # 첫 번째 줄에 두 정수 N, B
    N, B = map(int,input().split())
    Hi = list(map(int,input().split()))
    # 점원의 키를 큰 순으로 정렬
    Hi.sort()
    # 부분 집합을 구하는 리스트
    part_set = [0]*N
    minV = 999999
    # print(f'#{tc} {result - hight}')
    solve(0)
    print(f'#{tc} {minV}')
