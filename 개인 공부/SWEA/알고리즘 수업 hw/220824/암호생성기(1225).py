import sys
sys.stdin = open('password_cre.txt','r')
# 8개의 숫자를 입력 받음
# n번째 수는 n만큼 감소하고 뒤로 보내짐
# 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되고 종료
# 주어진 수는 integer 범위를 넘지 않음
# 마지막 배열은 모두 한자리 수로 구성

# 큐를 이용하여 암호를 확인
def Q(N_lst):
    cnt = 1
    result = 0
    while not result:
        # 5회를 반복하면 1 싸이클
        while cnt <= 5:
            queue = [0] * 8
            # 첫 번째 자리를 제외하고 큐에 저장
            for i in range(1, 8):
                queue[i-1] = N_lst[i]
            # 첫 번째 자리가 0보다 작아지면 종료
            if N_lst[0]-cnt <= 0:
                queue[-1] = 0
                result = 1
                return queue
            # 아니면 cnt를 빼고 마지막 자리에 저장
            queue[-1] = (N_lst[0]-cnt)
            N_lst = queue
            cnt += 1
        cnt = 1


# 첫 줄에 테스트 케이스 번호
for tc in range(1,11):
    T = int(input())
    N_lst = list(map(int,input().split()))
    print(f'#{tc}', *Q(N_lst))