# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 방법 1
# def preorder(n):
#     if n >= 2**(H+1) or tree[n] == 0:
#         return
#     print(tree[n])
#     preorder(2*n)
#     preorder(2*n+1)
#
#
# V = int(input())
# arr = list(map(int,input().split()))
# H = 4
# tree = [0]*(2**(H+1))
# tree[1] = arr[0]
# for i in range(0,2*V-2,2):
#     parent = tree.index(arr[i])
#     if tree[parent*2]:
#         tree[parent*2+1] = arr[i+1]
#     else:
#         tree[parent*2] = arr[i+1]
#
# preorder(arr[0])

# 방법 2
# def find_root(V):
#     for i in range(1,V+1):
#         if not parent[i]:
#             return i
#
# def preorder(n):
#     if n:
#         print(n)
#         preorder(ch1[n])
#         preorder(ch2[n])
#
# V = int(input())
# arr = list(map(int,input().split()))
# H = 4
#
# ch1 = [0]*(V+1)
# ch2 = [0]*(V+1)
# parent = [0]*(V+1)
# for i in range(0,len(arr),2):
#     p, c = arr[i], arr[i+1]
#     if not ch1[p]:
#         ch1[p] = c
#     else:
#         ch2[p] = c
#     parent[c] = p
#
# root = find_root(V)
#
# preorder(root)

# 연습문제
# def pre(n):
#     if n <= size or not n:
#         print(tree[n])
#         pre(2*n)
#         pre(2*n+1)
#
# tree = [0,'A','B','C','D','E','F']
# size = len(tree)-1
#
# pre(1)

# 최대합
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p and heap[p] < heap[c]:
        heap[p],heap[c] = heap[c], heap[p]
        c = p
        p = c//2

# 삭제
def deq(n):
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = 2*p
        else:
            break
    return tmp
heap = [0]*100
last = 0