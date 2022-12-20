import sys
sys.stdin = open('Forth.txt','r')
# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # 연산 코드가 주어진다.
    CODE = input().split()
    N = len(CODE)
    # 숫자를 쌓는 스택
    token = {'+':1,'-':1,'*':2,'/':2}
    stack = []
    num_cnt = 0
    for i in range(N):
        if CODE[i] == '.':
            if len(stack) != 1:
                print(f'#{tc} error')
                break
            print(f'#{tc}', *stack)
        elif CODE[i] in '+*/-':
            if len(stack) <= 1:
                print(f'#{tc} error')
                break
            if CODE[i] == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif CODE[i] == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif CODE[i] == '/':
                stack.append(int(1/(int(stack.pop()) / int(stack.pop()))))
            elif CODE[i] == '-':
                stack.append(-(int(stack.pop()) - int(stack.pop())))
        else:
            stack.append(CODE[i])
