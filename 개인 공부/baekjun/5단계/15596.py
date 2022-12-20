# a : 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
# 리턴값 : a에 포함되어 있는 정수 n개의 합

def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans
