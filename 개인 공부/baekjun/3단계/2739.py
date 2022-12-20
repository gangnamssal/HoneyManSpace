# N을 입력받음
import sys

N = int(sys.stdin.readline().rstrip('\n')) # 입력을 받음

for i in range(1,10):  
    print(f"{N} * {i} = {N*i}") #구구단을 출력함
