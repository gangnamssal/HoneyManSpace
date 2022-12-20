# 첫 줄에 테스트 케이스 개수 T
import sys
sys.stdin = open('4864.txt','r')

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    result = {}
    max_num = 0
    for i in str2:
        if result.get(i):
            result[i] += 1
        else:
            result[i] = 1
    for i in str1:
        if max_num < result[i]:
            max_num = result[i]
    print(f'#{tc} {max_num}')