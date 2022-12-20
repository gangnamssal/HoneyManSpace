import sys
sys.stdin = open('5432.txt','r')
# 밑의 쇠막대기가 더 길다
# 끝점이 겹치도록 놓지는 않는다.
# 레이저는 적어도 하나 존재한다
# 레이저는 쇠막대기의 양 끝점과 겹치지 않는다.
# 레이저는 (), 쇠막대기의 왼쪽 끝은 : (, 오른쪽 끝은 : )
T = int(input())
for tc in range(1, T+1):
    arr = input()
    # 막대기를 저장하는 변수
    stack = []
    # 레이저 개수를 저장
    # 막대기 숫자를 저장
    result = 0
    for i in range(len(arr)-1):
        if arr[i] == '(' and arr[i+1] != ')':
            stack.append(arr[i])
        elif arr[i] == '(' and arr[i+1] == ')':
            result += len(stack)
            if not stack:
                cnt = 0
        if arr[i] == ')' and arr[i-1] != '(':
            result += 1
            stack.pop()
    else:
        if stack[0] == '(' and arr[-1] == ')':
            result += 1

    print(f'#{tc} {result}')
