import sys
sys.stdin = open('calculation.txt','r')
def step1(inOrder):
    isp = {'+': 1, '*': 2, '(': 0}
    icp = {'+': 1, '*': 2, '(': 3}
    order = {'+': 1, '*': 2}
    ST = []
    postOrder = []
    for token in inOrder:
        if token.isdecimal():
            postOrder.append(token)
        else:
            # 왼쪽 괄호가 있는 경우
            # isp[ST[-1]] >= icp[token]
            # 스택에 있는 거랑 token이랑 우선순위를 생각
            while len(ST) > 0 and order[ST[-1]] >= order[token]:
                postOrder.append(ST.pop())
            ST.append(token)

    while ST:
        postOrder.append(ST.pop())

            # if len(ST) and order[ST[-1]] < order[token]:
            #     ST.append(token)
            # else:
            #     while len(ST) > 0 and order[ST[-1]] >= order[token]:
            #         postOrder.append(ST.pop())
            #     ST.append(token)
    return postOrder

def step2(postOrder):
    ST = []
    for token in postOrder:
        if token.isdecimal():
            ST.append(int(token))
        else:
            v1 = ST.pop()
            v2 = ST.pop()
            if token == '+':
                ST.append(v1+v2)
            else:
                ST.append(v1*v2)
    return ST[-1]


TC = 10
for tc in range(1, TC+1):
    N = int(input())
    inputS = input()

    postOrder = step1(inputS)
    result = step2(postOrder)
    print(f'#{tc} {result}')