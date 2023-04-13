# 부분집합 binary count
# arr = [1,5,3,4,3,2,3]
# for i in range(1<<7):
#     for j in range(8):
#         if i & (1<<j):
#             print(arr[j],end=' ')
#     print()
#--------------------------------------#

# 부분집합 재귀
def solve(start):
    if start == n:
        for i in range(n):
            if result[i]:
                print(arr[i], end=' ')
        print()
        return
    else:
        for i in range(2):
            result[start] = i
            solve(start+1)
arr = [3,6,7,1,5,4]
n = len(arr)
result = [0]*n
solve(0)
