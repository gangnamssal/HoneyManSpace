import sys
X = int(sys.stdin.readline())  # 총 금액
N = int(sys.stdin.readline())  # 물건 갯수
sum = 0
for i in range(1,N+1):   # 물건 수 만큼 반복
    a, b = map(int,sys.stdin.readline().split()) # 물건 가격과 갯수를 받음
    sum += a * b   # 합에 누적
if sum == X:
    print('Yes')  # 합과 총 금액이 같으면 출력
else:
    print('No')