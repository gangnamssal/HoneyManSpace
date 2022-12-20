# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력
# 첫 줄에 테스트 케이스의 수 T가 주어짐
T = int(input())
for i in range(1, T+1):
    # 각 케이스의 첫 줄에 양수의 개수 N이 주어짐
    N = int(input())
    # 다음 줄에 N개의 양수 a가 주어진다.
    a = list(map(int,input().split()))
    max_num = -1
    min_num = 1000001
    for j in range(len(a)): # 최댓값 최솟값 구하기
        if max_num < a[j]:
            max_num = a[j]
        if min_num > a[j]:
            min_num = a[j]
    print(f'#{i} {max_num - min_num}')