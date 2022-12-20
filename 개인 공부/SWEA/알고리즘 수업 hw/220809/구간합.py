# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차를 출력

# 첫 줄에 테스트 케이스 개수 T
T = int(input())
for tc in range(1,T+1):
    # 정수의 개수 N, 구간의 개수 M
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    sum_list = []
    max_num = 0
    min_num = 1000000


    # 최댓값을 구함
    for i in range(N-M+1):
        sum = 0
        for j in a[i:i+M]:
            sum += j
        sum_list.append(sum)
    
    for i in sum_list:
        if max_num < i:
            max_num = i
        
    for i in sum_list:
        if min_num > i:
            min_num = i

    print(f'#{tc} {max_num - min_num}')

