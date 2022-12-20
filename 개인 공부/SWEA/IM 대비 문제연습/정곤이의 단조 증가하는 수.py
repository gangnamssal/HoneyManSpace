import sys
sys.stdin = open('정곤이의 단조 증가하는 수.txt','r')

# 각 숫자의 자릿수가 단순하게 증가하는 수
# 양의 정수 N개가 주어진다.
# 정수 N개 중 2개를 곱해서 단조 증가하는 수를 구하고 최댓값을 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = []
    max_num = 0
    # 곱셈을 리스트에 저장
    for i in range(N-1):
        for j in range(i+1, N):
            result.append(str(arr[i]*arr[j]))

    for i in range(len(result)):
        for j in range(len(result[i])-1):
            if int(result[i][j]) > int(result[i][j+1]):
                break
        else:
            if max_num < int(result[i]):
                max_num = int(result[i])
    if max_num == 0:
        max_num = -1
    print(f'#{tc} {max_num}')


