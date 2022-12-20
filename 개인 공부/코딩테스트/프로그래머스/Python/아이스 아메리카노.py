# 아이스 아메리카노는 한잔에 5,500원입니다.
# 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때,
# 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수
# 남는 돈을 순서대로 담은 배열을 return

def solution(money):
    result = [0]*2
    result[0] = money // 5500
    result[1] = money - (5500*result[0])
    return result