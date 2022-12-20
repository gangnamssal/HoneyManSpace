# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return

sum = 0
def solution(n):
    global sum
    if n // 10 == 0:
        sum += n
        return sum
    else:
        n = str(n)
        sum += int(n) % 10
        new_n = int(n) // 10
        solution(new_n)
        return sum

