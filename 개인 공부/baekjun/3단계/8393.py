import sys
n = int(sys.stdin.readline()) # 입력을 받는다.
sum = 0                     # 합을 초기화 한 함수.
for i in range(1,n+1):
    sum += i          # n번 동안 for문이 실행되고 합을 누적한다.
print(sum)