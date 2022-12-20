# 숫자를 문자열로 나타내는 행성이 있다.
import sys
sys.stdin = open('GNS_test_input.txt','r')
# 첫 줄에 테스트 케이스의 개수가 주어진다.
T = int(input())

for tc in range(1,T+1):
    # #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스틑 케이스의 길이가 주어진다.
    C, N = map(str,input().split())
    # 테스트 케이스가 주어진다.
    TC = input()
    char = []
    num_arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    # 문자를 숫자 문자로 바꿈
    for i in range(len(num_arr)):
        TC = TC.replace(num_arr[i],f'{i}')
    # 숫자를 비교해서 문자로 다시 변경하고 새로운 리스트에 저장
    for i in range(len(num_arr)):
        for j in TC:
            if f'{i}' == j:
                char.append(num_arr[i])
    # 리스트를 합쳐서 출력
    char = ' '.join(char)
    print(f'#{tc}')
    print(f'{char}') 
