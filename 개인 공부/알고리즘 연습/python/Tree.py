T = int(input())
arr = list(map(int,input().split()))
H = 4
tree = [0] * (2**(H+1))
tree[1] = 1
for i in range(T-1):
    parent = tree.index(arr[2*i])
    if tree[parent*2]:
        tree[parent*2+1] = arr[i*2+1]
    else:
        tree[parent*2] = arr[i*2+1]
print(tree)
