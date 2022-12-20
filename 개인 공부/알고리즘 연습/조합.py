# 재귀를 이용한 조합 구현 1
# def comb(n,r):
#     if r == 0:
#         print(tr)
#     elif n < r:
#         return
#     else:
#         tr[r-1] = arr[n-1]
#         comb(n-1,r-1)
#         comb(n-1,r)
#
# arr = [1,2,3,4,5,6]
# n = len(arr)
# r = 3
# tr = [0]*r
# comb(n,r)
#-------------------------------#

# 재귀를 이용한 방법 2
def nCr(n,r,k):
    if r == 0:
        print(check)
        return
    for i in range(k,n-r+1):
        check[r - 1] = arr[i]
        nCr(n,r-1,i+1)

arr = [1,2,3,4,5,6]
n = len(arr)
r = 3
check = [0]*r
nCr(n,r,0)

#---------------------------------#
# 재귀를 이용한 중복 조합 구현
def nCr(n,r,k):
    global cnt
    if r == 0:
        result = check[:]
        result.sort()
        if result not in same:
            same.append(result)
            cnt += 1
            print(check)
        return
    for i in range(n):
        check[r - 1] = arr[i]
        nCr(n,r-1,i+1)

arr = [1,2,3,4,5,6]
n = len(arr)
r = 3
cnt = 0
same = []
check = [0]*r
nCr(n,r,0)
print(cnt)
#--------------------------------#

# 반복문을 이용한 조합 구현
# arr = [1,2,3,4,5,6]
# N = len(arr)
# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             print(arr[i],arr[j],arr[k])
