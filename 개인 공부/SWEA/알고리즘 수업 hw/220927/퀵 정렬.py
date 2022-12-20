import sys
sys.stdin = open('퀵 정렬.txt','r')
# 퀵 정렬을 수행하는 함수
def partition(l,r):
    pivot = ai[l]
    i, j = l, r
    while i <= j:
        while i <= j and ai[i] <= pivot:
            i += 1
        while i <= j and ai[j] > pivot:
            j -= 1
        if i < j:
            ai[i],ai[j] = ai[j], ai[i]
    ai[l],ai[j] = ai[j], ai[l]
    return j

def quick_sort(l,r):
    if l < r:
        p_idx = partition(l,r)
        quick_sort(l,p_idx-1)
        quick_sort(p_idx+1,r)

# 첫 줄에 테스트케이스 T
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # N개의 정수 ai
    ai = list(map(int,input().split()))
    quick_sort(0,N-1)
    print(f'#{tc} {ai[N // 2]}')
