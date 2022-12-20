# 첫 줄에 테스트 케이스가 주어진다.
import sys
sys.stdin = open('4869.txt', 'r')
# 가로 * 세로, 10*20과 20*20이 있음
# 세로는 20으로 정해짐
# N에 따라서 크기가 달라짐
T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = [1, 2, 5, 11]
    if N//10 < 4:
        i = N//10 -1
        print(f'#{_} {arr[i]}')
        continue
    else:
        while len(arr) < N/10:
            result = 0
            result = arr[-1]*arr[0] + arr[-2]*arr[1]
            arr.append(result)
    print(f'#{_} {arr[-1]}')


