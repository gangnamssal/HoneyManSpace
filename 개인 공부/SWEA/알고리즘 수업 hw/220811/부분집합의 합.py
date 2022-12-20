# 1부터 12까지의 숫자를 원소로 가지는 집합 A
# A의 부분 집합 중 N개의 원소를 갖고
# 원소의 합이 K인 부분집합의 개수를 출력
# 첫 줄에 테스트 케이스 개수 T
T = int(input())
for tc in range(1,T+1):
    a = 0  # 부분 집합 합을 저장하는 변수
    b = 0  # 부분 집합의 갯수를 저장하는 변수
    cnt = 0 # K와 합이 같은 부분집합의 갯수를 저장하는 변수
    N, K = map(int,input().split()) 
    for i in range(1<<12):
        b = 0   # 초기화
        a = 0
        for j in range(12):
            if i & (1<<j):
                a += j+1  # 부분집합의 합을 구한다.
                b += 1    # 부분집합의 원소 갯수를 구한다.
        if b == N:  # 원소 갯수가 N개이고
            if a == K:  # 합이 K이면
                cnt += 1  # 카운트를 1 증가
    print(f'#{tc} {cnt}')