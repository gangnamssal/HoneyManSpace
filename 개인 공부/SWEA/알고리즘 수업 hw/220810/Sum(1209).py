# 2차원 배열이 주어짐
# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구함
# 10개의 테스트 케이스
import sys
sys.stdin = open('sum_input.txt', 'r')
for tc in range(1, 11):
    N = int(input())
    # 2차원 배열을 받음
    arr = [list(map(int, input().split())) for _ in range(100)]
    num = len(arr)
    max_sum = 0
    # 행의 최댓값을 구함
    for i in range(num):
        sum_num = 0
        for j in range(num):
            sum_num += arr[i][j]
            if max_sum < sum_num:
                max_sum = sum_num
    # 행의 최댓값과 열의 최댓값을 구해서 비교
    for j in range(num):
        sum_num = 0
        for i in range(num):
            sum_num += arr[i][j]
            if max_sum < sum_num:
                max_sum = sum_num
    # 대각선 최댓값과 이전 최댓값을 비교
    sum_num = 0
    for i in range(num):
        sum_num += arr[i][i]
        if max_sum < sum_num:
            max_sum = sum_num
    sum_num_2 = 0
    for i in range(num):
        sum_num_2 += arr[i][num-i-1]
        if max_sum < sum_num_2:
            max_sum = sum_num_2
    print(f'#{tc} {max_sum}')

