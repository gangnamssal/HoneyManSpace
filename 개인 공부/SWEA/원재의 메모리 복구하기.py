import sys
sys.stdin = open('원재의 메모리 복구하기.txt','r')

# 원래 상태가 주어질 때 초기화 상태에서 돌아가는데 몇 번 고쳐야 하는지
# bit를 고르면 그 뒤는 전부 같은 수로 바뀐다.

T = int(input())
for tc in range(1, T+1):
    # 결과로 나올 리스트
    n_lst = list(map(int, input()))
    # 처음 리스트
    arr = [0]*len(n_lst)
    # 결과 리스트 길이
    N = len(n_lst)
    # 첫 리스트 길이
    M = len(arr)
    i = 0
    cnt = 0
    while i <= N-1:
        if n_lst[i] != arr[i]:
            if n_lst[i] == 1:
                for x in range(i, len(arr)):
                    arr[x] = 1
                cnt += 1
                if arr == n_lst:
                    break
            else:
                for x in range(i, len(arr)):
                    arr[x] = 0
                cnt += 1
                if arr == n_lst:
                    break
        i += 1

    print(f'#{tc} {cnt}')

