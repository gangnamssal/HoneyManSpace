# N!을 출력
N = int(input())
result = 1
while N > 0:
    result *= N
    N -= 1
print(result)