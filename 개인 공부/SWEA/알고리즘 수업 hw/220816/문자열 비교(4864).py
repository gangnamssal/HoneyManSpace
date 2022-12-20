# 문자열 1과 2가 주어짐
# 문자의 일치하는 부분이 존재하면 1, 아니면 0
# 첫 줄에 테스트 T
import sys
sys.stdin = open('4864.txt','r')
T = int(input())
for _ in range(1,T+1):
    str1 = input()
    str2 = input()
    for i in range(len(str2)):
        if str2[i] == str1[0] and str2[i:i+len(str1)] == str1:
            result = 1
            break
        else:
            result = 0
    print(f'#{_} {result}')
