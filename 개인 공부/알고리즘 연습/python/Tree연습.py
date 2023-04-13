# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# V = int(input())
# arr = list(map(int, input().split()))
# H = 4
# 방법 1
# def preorder(n):
#     if n >= 2**(H+1) or tree[n] == 0:
#         return
#     preorder(n*2)
#     preorder(n*2+1)
#     print(tree[n])
#
# tree = [0] * (2**(H+1))
# tree[1] = arr[0]

# 배열 구하기 1
# for i in range(V-1):
#     parent = tree.index(arr[i*2])
#     if tree[parent*2]:
#         tree[parent*2+1] = arr[2*i+1]
#     else:
#         tree[parent*2] = arr[2*i+1]


# 배열 구하기 2
# for i in range(0, 2*V-2, 2):
#     parent = tree.index(arr[i])
#     if tree[parent*2]:
#         tree[parent*2+1] = arr[i+1]
#     else:
#         tree[parent*2] = arr[i+1]

# preorder(1)

#----------------------------------------------#
# 방법 2
# def preorder(n):
#     if n:
#         print(n)
#         preorder(ch1[n])
#         preorder(ch2[n])
#
# def find_root(V):
#     for i in range(1, V+1):
#         if not par[i]:
#             return i
#
#
# # 부모 노드를 인덱스로 자식을 나눔
# ch1 = [0]*(V+1)
# ch2 = [0]*(V+1)
# # 자식 노드를 인덱스로 부모를 나눔
# par = [0]*(V+1)
#
# for i in range(0,len(arr),2):
#     p,c = arr[i], arr[i+1]
#     if not ch1[p]:
#         ch1[p] = c
#     else:
#         ch2[p] = c
#     par[c] = p
#
# root = find_root(V)
# preorder(root)
#---------------------------------------#
# 연습문제
tree = [0,'A','B','C','D','E','F']
size = len(tree)-1
def pre(n):
    if n <= size or not n:
        print(tree[n])
        pre(2*n)
        pre(2*n+1)
pre(1)