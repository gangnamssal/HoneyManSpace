#정수가 담긴 리스트 num_list가 주어질 때,
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return
def solution(num_list):
    result = [0,0]
    for i in num_list:
        if i%2:
            result[1] += 1
        else:
            result[0] += 1
    return result