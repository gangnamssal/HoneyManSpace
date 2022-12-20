# 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때,
# n명의 사람이 최소 한 조각 이상 피자를 먹으려면
# 최소 몇 판의 피자를 시켜야 하는지를 return
def solution(n):
    if n % 7:
        return n // 7 + 1
    else:
        return n // 7
print(solution(7))