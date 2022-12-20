import sys
sys.stdin = open('calculation.txt','r')
# 연산자는 + * 두 종류
# 숫자는 0~9의 정수만 주어짐

# 후위 표기식으로 바꾸는 함수를 만든다.
def CHANGE(arr):
    # 우선 순위를 나타냄
    token = {'+' : 1 , '*' : 2}
    # 토큰을 스택에 저장
    stack = []
    # 후위 계산식을 저장하는 변수
    new_arr = ''
    for i in arr:
        if i == '*' or i == '+':
            # 스택이 비었고 순위가 더 크다면 스택에 저장
            if (not stack) or (token[stack[-1]] < token[i]):
                stack.append(i)
                # 저장된 토큰이 크다면 꺼내면서 후위 계산식 문자열에 저장
            elif token[stack[-1]] >= token[i]:
                while stack:
                    if token[stack[-1]] < token[i]:
                        break
                    new_arr += stack.pop()
                stack.append(i)
        # 숫자가 나오면 스택에 저장하지 않고 문자열에 저장
        else:
            new_arr += i
    # 스택에 남은 토큰을 꺼내서 저장
    else:
        for i in range(len(stack)):
            new_arr += stack.pop()
    return  new_arr

# 후위 계산식을 계산하는 함수
def calculation(new_arr):
    stack = []
    result = 0
    for i in range(len(new_arr)):
        if new_arr[i] == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif new_arr[i] == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        else:
            stack.append(new_arr[i])
    return stack

for tc in range(1, 11):
    # 테스트 케이스의 길이가 주어진다.
    N = int(input())
    arr = input()
    new_arr = CHANGE(arr)
    print(f'#{tc}',*calculation(new_arr))