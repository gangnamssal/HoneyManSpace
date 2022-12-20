# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return
def solution(n):
    sum = 0
    for i in range(0,n+1,2):
        sum += i
    return sum