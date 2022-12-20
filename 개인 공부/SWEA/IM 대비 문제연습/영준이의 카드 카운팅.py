import sys
sys.stdin = open('영준이의 카드 카운팅.txt', 'r')

# 이미 겹치는 카드를 가지고 있다면 오류를 출력
T = int(input())
for tc in range(1,T+1):
    # 무늬 (S,D,H,C)+숫자
    arr = input()
    arr_dict = {'S':0,'D':1,'H':2,'C':3}
    arr_lst = [[] for _ in range(4)]
    for i in range(0, len(arr)-2, 3):
        if arr[i+1] != '0':
            if int(arr[i+1]+arr[i+2]) in arr_lst[arr_dict[arr[i]]]:
                print(f'#{tc} ERROR', end='')
                break
            arr_lst[arr_dict[arr[i]]].append(int(arr[i + 1] + arr[i + 2]))
        else:
            if int(arr[i+2]) in arr_lst[arr_dict[arr[i]]]:
                print(f'#{tc} ERROR', end='')
                break
            arr_lst[arr_dict[arr[i]]].append(int(arr[i + 2]))
    else:
        print(f'#{tc}', end=' ')
        for i in arr_lst:
            print(f'{13-len(i)}', end=' ')
    print()