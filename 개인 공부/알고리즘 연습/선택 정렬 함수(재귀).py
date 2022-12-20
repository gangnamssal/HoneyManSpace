# 선택 정렬 함수를 재귀로 표현
def select_sort(num):
    minV = num
    if num == N-1:
        return
    else:
        # 현재 자리와 뒷자리를 비교해서
        # 현재 자리가 크면 바꾼다.
        for i in range(num+1,N):
            if arr[minV] > arr[i]:
                minV = i
        arr[num],arr[minV] = arr[minV],arr[num]
        select_sort(num+1)

arr = [8,4,5,3,1,2,9,3]
N = len(arr)
select_sort(0)
print(arr)

