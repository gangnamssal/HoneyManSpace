# 배열 array와 정수 n이 매개변수로 주어질 때,
# array에 n이 몇 개 있는 지를 return

def solution(array, n):
    result = {}
    for i in array:
        if result.get(i):
            result[i] += 1
        else:
            result[i] = 1
    return result.get(n)