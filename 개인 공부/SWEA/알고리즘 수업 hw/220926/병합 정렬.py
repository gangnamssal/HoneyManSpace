# 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크면 출력
# 분할 과정
def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    if low_arr[-1] > high_arr[-1]:
        cnt += 1
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    # 정수 N
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc} {merge_sort(ai)[N//2]} {cnt}')
