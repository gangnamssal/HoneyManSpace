import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())  
multi = str(A * B * C)  # 세 수를 받아서 곱한다
for i in range(10):
    print(multi.count(f'{i}'))  #0부터 9까지 수를 세서 출력한다.
