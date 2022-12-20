import sys
T = int(sys.stdin.readline()) # 입력을 input 보다 더 빨리 받는다.
for i in range(1,T+1):
    A, B = map(int,sys.stdin.readline().split()) # 여러 개의 입력을 받을 때
    print(A+B)