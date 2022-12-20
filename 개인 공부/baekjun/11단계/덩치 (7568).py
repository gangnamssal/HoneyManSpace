N = int(input())
inputarr = []
arr = [[]]
result = [0]*N
cnt = 0
for i in range(N):
    x, y = map(int,input().split())
    inputarr.append([x,y])
    for j in range(len(arr)):
        if arr[j]:
            for k in range(len(arr[j])):
                if arr[j][k][0] < x and arr[j][k][1] < y:
                    arr.insert(j,[[x,y]])
                    cnt += 1
                    break
                elif arr[j][k][0] > x and arr[j][k][1] > y:
                    break
                else:
                    arr[j].append([x,y])
                    cnt += 1
                    break
        else:
            arr[j].append([x,y])
            cnt += 1
else:
    if cnt != N:
        arr.insert(N-1,[[x,y]])



