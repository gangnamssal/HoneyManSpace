# import sys
# N = int(sys.stdin.readline())
# start = 1
# numbers = 0
# while True:
#     # 숫자를 문자열로 바꿔서 각 자리를 더하여 비교
#     str_start = str(start)
#     result = start
#     for i in str_start:
#         result += int(i)
#
#     if start < N and result != N:
#         start += 1
#     elif result == N:
#         numbers = start
#         break
#     elif result > N and start > 10:
#         break
# print(numbers)
n = int(input())
result = 0

for i in range(1, n+1):
    nums = list(map(int, str(i)))
    cons = i + sum(nums)
    if cons == n:
        result = i
        break
print(result)
