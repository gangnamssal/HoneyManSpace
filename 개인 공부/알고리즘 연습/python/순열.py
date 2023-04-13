# 반복을 이용한 순열
# for i in range(1,4):
#     for j in range(1,4):
#         if i != j:
#             for k in range(1,4):
#                 if i!=k and j!=k:
#                     print(i,j,k)
#-------------------------------------#

# 재귀를 통한 순열 생성
# def solve(num):
#     if num == N:
#         print(p)
#         return
#     else:
#     # 첫 번째 자리를 정하고 자리를 바꾼다.
#     # 다시 돌아오면 원래 모양으로 돌아와야 한다.
#         for i in range(num,3):
#             p[num],p[i] = p[i],p[num]
#             solve(num+1)
#             p[num], p[i] = p[i], p[num]
# p = [1,2,3]
# N = len(p)
#
# solve(0)
#-------------------------------------------------------#

# 방문 표시를 한 재귀를 이용
# def solve(num,k):
#     if num == k:
#         print(result)
#         return
#     else:
#         for i in range(N):
#             if not u[i]:
#                 u[i] += 1
#                 result[num] = p[i]
#                 solve(num+1,k)
#                 u[i] -= 1
# p = [1,2,3,4,5,6,7,8,9,10]
# N = len(p)
# u = [0]*N
# result = [0]*3
# solve(0,3)
#------------------------------------#

