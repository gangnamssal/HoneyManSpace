import sys

N = []
for i in range(1,10): # 9개의 숫자를 받기 위한 반복문
    num = int(sys.stdin.readline().rstrip('\n'))
    N.append(num)  # 빈 리스트에 저장
print(max(N))  # 최댓값을 구함
print(N.index(max(N))+1)  # 최댓값의 인덱스를 구함