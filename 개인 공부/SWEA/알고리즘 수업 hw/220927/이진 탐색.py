import sys
sys.stdin = open('이진 탐색.txt','r')

# 정수 N개가 정렬한 상태로 리스트 A에 저장
# B에 저장된 M개의 정수가 A에 들어있는 수 인지 이진 탐색으로 확인

def search(N_lst,l,r,key,v):
    global cnt
    if l > r:
        return v
    else:
        middle = (r+l) // 2
        if key == N_lst[middle]:
            cnt += 1
            return
        if key < N_lst[middle]:
            return search(N_lst,l,middle-1,key,v+'1')
        elif key > N_lst[middle]:
            return search(N_lst,middle+1,r,key,v+'0')


# 첫 줄에 테스트케이스 T
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    N_lst = list(map(int,input().split()))
    M_lst = list(map(int,input().split()))
    l = 0
    r = N-1
    cnt = 0
    for i in M_lst:
        print(search(N_lst,l,r,i,''))
    print(f'#{tc} {cnt}')
