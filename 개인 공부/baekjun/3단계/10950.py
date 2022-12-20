import sys
T = int(sys.stdin.readline().rstrip('\n')) # 줄 갯수를 입력 받음
sum = 0 # 합을 저장하는 변수
for i in range(1,T+1): 
    A, B = map(int,input().split()) # for문이 변수만큼 실행되고
    sum = A + B                     # 두 개의 수를 변수만큼 받고 합을 구한다.
    print(sum)
    
