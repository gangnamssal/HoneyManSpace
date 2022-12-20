import sys
sys.stdin = open('4866.txt','r')

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))
    # ()를 저장
    stack = []
    # {}를 저장
    result = 1
    for i in arr:
        if '(' not in stack and i == ')':
            result = 0
            break
        if '{' not in stack and i == '}':
            result = 0
            break
        if i == '(' or i == '{':
            stack.append(i)
        if i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == ')' and stack[-1] != '(':
            result = 0
            break
        if i == '}' and stack[-1] == '{':
            stack.pop()
        elif i == '}' and stack[-1] != '{':
            result = 0
            break
    if stack:
        result = 0
    print(f'#{tc} {result}')