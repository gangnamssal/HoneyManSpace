# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때,
# 마지막 원소 다음으로 올 숫자를 return

def solution(common):
    check1 = common[1] - common[0]
    check2 = common[2] - common[1]
    if check1 == check2:
        return common[-1] + check1
    else:
        return common[-1]*(check2//check1)
