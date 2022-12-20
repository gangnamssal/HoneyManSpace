# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램
# 첫째 줄에 수의 개수 N
# 둘째 줄부터 N개의 줄에는 수
# 이 수는 절댓값이 1000보다 작거나 같은 정수, 중복 x

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
for i in arr:
    print(i)