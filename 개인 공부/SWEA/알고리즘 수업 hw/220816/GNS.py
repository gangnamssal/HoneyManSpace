# 교수님 풀이

# 문자열 크기 비교로는 정렬 불가능
# 각 문자열의 크기를 비교할 수 있는 방안이 팔요하다.
# 각 문자열의 value를 가지고 있는 dict를 이용해서 크기 비교를 가능
# 정렬하는 함수

def GNS_sort(arr):
    GNS_Value = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    # 버블 정렬을 활용하여 정렬하기
    # 요소 2개 비교해서 큰 값 뒤로 보내기
    # (큰 원소 뒤로 보내기 작업) * N 번 수행
    for j in range(N-1):
        # 가장 앞쪽 원소부터 제일 뒤 원소까지 2개씩 비교해서 큰 값 뒤로 보내기
        for i in range(N-1-j):
            if GNS_Value[arr[i]] > GNS_Value[arr[i+1]]: # 앞 쪽 요소가 뒤쪽 요소보다 더 크면 자리 바꾸기
                arr[i], arr[i+1] = arr[i+1],arr[i]


T = int(input())
for _ in range(1,T+1):
    tc, N = input().split()
    N = int(N)
    # GNS 숫자 배열 입력받기
    arr = input().split()
    GNS_sort(arr)
    print(f'{tc}')
    print(*arr)



# 카운팅 정렬 활용
def GNS_sort2(arr):
    GNS_value = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    # 카운팅 정렬
    # 1. 각 요소가 몇 번 나왔는지 숫자 세기
    # 2. 누적합 구하기(요소 자리 구하기)
    # 3. 요소들을 위치 보고 복사하면 된다. 
    counts = [0] * 10
    sorted_arr = ['']*N
    # 1.
    for i in range(N):
        index = GNS_value[arr[i]]
        counts[index] += 1
    for i in range(1,N):
        counts[i] += counts[i-1]
    # 새로운 배열에 요소가 들어갈 위치에 값을 복사
    for i in range(N):
        # arr[i] 요소가 들어갈 자리(counts[GNS_value[arr[i]]])에다가 넣어주기
        counts[GNS_value[arr[i]]] -= 1
        sorted_arr[counts[GNS_value[arr[i]]]] = arr[i]
    return sorted_arr
        
