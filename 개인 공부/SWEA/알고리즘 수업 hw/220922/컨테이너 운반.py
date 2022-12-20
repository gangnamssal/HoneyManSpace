import sys
sys.stdin = open('컨테이너 운반.txt','r')

# N개의 컨테이너를 M대의 트럭으로 운반
# 트럭당 한 개의 컨테이너를 운반할 수 있음, 적재량을 초과하면 운반 x
# M대의 트럭이 편도로 한번만 이동

# 테스트케이스
T = int(input())
for tc in range(1,T+1):
    # 컨테이너 수 N, 트럭 수 M
    N, M = map(int,input().split())
    # N개의 화물의 무게
    Wi = list(map(int,input().split()))
    # M개 트럭의 적재용량
    ti = list(map(int,input().split()))

    # 화물의 무게를 정렬
    Wi.sort(reverse=True)
    # 트럭의 적재 용량을 정렬
    ti.sort(reverse=True)
    # 화물의 무게를 나타냄
    weith = 0
    # 옮긴 총 무게를 나타내는 변수
    sum_weith = 0
    # 옮긴 횟수를 나타냄
    cnt = 0
    while True:
        # 가장 큰 무게가 적재 용량보다 작거나 같으면
        # 옮겼다는 의미, 트럭에서 1개를 뺀다.
        if Wi[weith] <= ti[0]:
            sum_weith += Wi[weith]
            ti.pop(0)
        weith += 1
        cnt += 1
        # 만약 하나도 못옮겼거나 화물이 남으면 반복문 종료
        if cnt >= M or weith >= N:
            break
    print(f'#{tc} {sum_weith}')
