#선택정렬   O(n**2)
#------------------------------------------------------------------
def selection_sort(arr):
    print('Selection')
    for i in range(len(arr) - 1):
        min_idx = i                         #최소값 찾기-탐색 전에는 맨 앞의 값으로
        for j in range(i + 1, len(arr)):    #나머지 최소값 탐색
            if arr[j] < arr[min_idx]:
                min_idx = j                 #최소값을 찾으면 swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#삽입정렬    O(n**2)
#------------------------------------------------------------------
def insertion_sort_1(arr):
    print('Selection_1')
    for end in range(1, len(arr)):          #먼저 끝을 정의
        for i in range(end, 0, -1):         #정의된 끝에서부터 거꾸로 탐색
            if arr[i - 1] > arr[i]:         #작은 값 찾으면 swap
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr

#최적화 : 코드 간략화
def insertion_sort_2(arr):
    print('Selection_2')
    for end in range(1, len(arr)):          #먼저 끝을 정의
        to_insert = arr[end]                #arr[end] 값을 따로 저장하여 아래 while에서 조건으로 사용 
        while end > 0 and arr[end-1] > to_insert :
            arr[end] = arr[end-1]
            end -= 1
        arr[end] = to_insert
    return arr

#버블정렬   O(n**2)
#------------------------------------------------------------------
def bubble_sort_1(arr):
    print('Bubble_1')
    for i in range(len(arr)-1, 0 , -1) :    #뒤에서부터 정렬
        for j in range(i) :                 #양 옆의 값을 비교하여 swap
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#최적화 : swap 유무 확인하여 안했을 경우 바로 반복문을 탈출할 수 있는 방식으로 코드 동작을 줄임
def bubble_sort_2(arr) :
    print('Bubble_2')
    for i in range(len(arr)-1,0,-1) :
        swapped = False                     #swap 확인 변수
        for j in range(i) :
            if arr[j]>arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True              #swap 발생할 경우 True로
        if not swapped :                    #swap이 발생하지 않으면 반복문 탈출
            break
    return arr

#합병정렬   O(nlogn)
#------------------------------------------------------------------
def merge_sort_1(arr) :
    #탈출 조건
    if len(arr) < 2 :
        return arr

    #분할
    mid = len(arr)//2
    low_arr = merge_sort_1(arr[:mid])
    high_arr = merge_sort_1(arr[mid:])

    merged_arr = []     #합병할 리스트
    l, h = 0,0          #low_arr와 high_arr를 각각 돌 idx

    print('Merge_1')
    while l<len(low_arr) and h<len(high_arr) :      #모두 다 크기 확인을 할 때까지
        if low_arr[l] < high_arr[h] :               #작은 값을 먼저 merged_arr에 추가
            merged_arr.append(low_arr[l])
            l+=1
        else :
            merged_arr.append(high_arr[h])
            h+=1

    #정렬된 값들을 병합
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr

#최적화 : 매번 배열을 만드는 것보다 각 부분마다 idx를 지정
def merge_sort_2(arr):
    print('Merge_2')

    def sort(low, high):
        #탈출 조건
        if high - low < 2:
            return
       
        mid = (low + high) // 2     #분할
        sort(low, mid)              #앞 부분 배열 정렬
        sort(mid, high)             #뒷 부분 배열 정렬
        merge(low, mid, high)       #합병

        return arr

    def merge(low, mid, high):      #정렬하는 함수
        temp = []
        l, h = low, mid

        #low에 있는 값과 high에 있는 값 비교
        while l < mid and h < high:     #배열 끝까지 돌아가도록
            if arr[l] < arr[h]:         
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        
        #low, high에서 지정된 값을 각각 mid와 비교
        while l < mid:                  
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        
        #
        for i in range(low, high):
            arr[i] = temp[i - low]
        
        return temp

    return sort(0, len(arr))

#퀵정렬     O(n**2)
#------------------------------------------------------------------
def quick_sort_1(arr) :
    print('Quick_1')
    if len(arr) <= 1 :
        return arr
    pivot = arr[len(arr)//2]                        #피봇 정하기(마음대로)
    lesser_arr, equal_arr, greater_arr = [],[],[]   #피봇보다 작은 값 저장/같은 값 저장/ 큰 값 저장

    for num in arr :        #값 비교해서 각 배열에 값 넣기 
        if num < pivot :
            lesser_arr.append(num)
        elif num > pivot :
            greater_arr.append(num)
        else :
            equal_arr.append(num)

    # 정렬된 배열 합치기+다시 lesser_arr과 greater_arr에서 다시 피봇잡고 정렬
    return quick_sort_1(lesser_arr)+equal_arr+quick_sort_1(greater_arr)

#최적화 : 매번 배열을 만드는 것보다 각 부분마다 idx를 지정
def quick_sort_2(arr) :
    print('Quick_2')
    def sort(low, high) :
        if high <= low :                #탈출조건
            return
        
        mid = partition(low, high)      #피봇을 기준으로 분할
        sort(low, mid-1)                #피봇보다 작은 값들 정렬
        sort(mid, high)                 #피봇보다 큰 값들 정렬

        return arr

    def partition(low, high) :
        pivot = arr[(low+high)//2]      #피봇 선택(마음대로)

        #값 비교해서 배열에 넣기
        while low <= high :
            while arr[low] < pivot :
                low += 1
            while arr[high] > pivot :
                high -= 1
            if low <= high :    #swap
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low+1, high-1

        return low
    
    return sort(0, len(arr)-1)


print(selection_sort([7, 4, 6, 5, 2]))
print(insertion_sort_1([7, 4, 6, 5, 2]))
print(insertion_sort_2([7, 4, 6, 5, 2]))
print(bubble_sort_1([7, 4, 6, 5, 2]))
print(bubble_sort_2([2, 4, 5, 6, 7]))
print(merge_sort_1([2, 4, 3, 9, 5, 11, 6, 7]))
print(merge_sort_2([2, 4, 3, 9, 5, 11, 6, 7]))
print(quick_sort_1([2, 4, 3, 9, 5, 11, 6, 7]))
print(quick_sort_2([2, 4, 3, 9, 5, 11, 6, 7]))