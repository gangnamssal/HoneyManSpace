# 정수가 들어 있는 배열 num_list
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return

def solution(num_list):
    N = len(num_list)
    result = [0] * N
    for i in range(N-1,-1,-1):
        result[N-i-1] = num_list[i]
    return result


