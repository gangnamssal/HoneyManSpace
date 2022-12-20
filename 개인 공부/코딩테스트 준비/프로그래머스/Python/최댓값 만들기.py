# 정수 배열 numbers가 매개변수
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return

def solution(numbers):
    return dfs(0,numbers,1)

def dfs(n,numbers,result):
    global maxV
    if n == 2 and result > maxV:
        maxV = result
        return
    for i in range(len(numbers)):
        if i not in visited and numbers[i]:
            visited.append(i)
            dfs(n+1, numbers, result*numbers[i])
            visited.pop()
    return maxV

visited = []
maxV = 0
