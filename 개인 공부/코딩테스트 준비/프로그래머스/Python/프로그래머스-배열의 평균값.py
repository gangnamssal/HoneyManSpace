# 정수 배열 numbers
# numbers의 원소의 평균값을 return

def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)