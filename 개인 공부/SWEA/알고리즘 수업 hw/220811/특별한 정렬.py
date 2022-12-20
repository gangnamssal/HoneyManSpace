# N개의 정수가 주어지면 큰수와 작은 수를 번갈아서 출력
# 첫 줄에 테스트 케이스가 주어진다.
import sys
sys.stdin = open('spe.txt','r')

T = int(input())
for tc in range(1,T+1):
    # 정수의 개수 N개
    N = int(input())
    # 정수 ai
    ai = list(map(int,input().split()))
    
    arr = []
    num = len(ai)
    arr_str = str()
    while True:
        max_num = 0
        min_num = 101
        index = 0
        # 최댓값을 선택
        for i in range(len(ai)):
            if max_num < ai[i]:
                max_num = ai[i]
                index = i
        # ai에서 최댓값의 뽑아냄
        if len(ai) == 1:
            arr.append(ai[0])
            break
        elif len(arr) == 10:
            break
        else:
            ai.pop(index)
            arr.append(max_num)
        # 최솟값을 선택
        for i in range(len(ai)):
            if min_num > ai[i]:
                min_num = ai[i]
                index = i
        # 최솟값을 뽑아냄
        if len(ai) == 1:
            arr.append(ai[0])
            break
        elif len(arr) == 10:
            break
        else:
            ai.pop(index)
            arr.append(min_num)
    for i in arr:
        arr_str += str(i) + ' '
    print(f'#{tc} {arr_str}')
