import sys
N = int(sys.stdin.readline()) # 입력을 받음
for i in range(1,N+1):
    print(' '*(N-i)+'*'*i) # 띄어쓰기는 1개씩 줄고 별은 1개씩 증가