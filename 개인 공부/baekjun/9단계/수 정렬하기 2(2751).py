#N개의 수가 주어졌을 때, 오름차순으로 정렬하는 프로그램
import sys
# 첫째 줄에 수의 개수 N
N = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(N)]
array.sort()
for i in array:
    print(i)