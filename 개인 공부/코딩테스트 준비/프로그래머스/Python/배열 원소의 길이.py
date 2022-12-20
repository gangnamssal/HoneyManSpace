# 문자열 배열 strlist
# strlist 각 원소의 길이를 담은 배열을 retrun
def solution(strlist):
    N = len(strlist)
    result = [0]*N
    for i in range(N):
        result[i] = len(strlist[i])
    return result