# N개의 숫자가 공백 없이 쓰여있다.
# 이 숫자를 모두 합해서 출력하는 프로그램
import sys
# 숫자의 갯수
N = int(sys.stdin.readline())
# 숫자열
num_str = list(map(int,sys.stdin.readline().rstrip('\n')))
sum = 0 # 합을 저장하는 변수
for i in num_str:
    sum += i
print(sum)