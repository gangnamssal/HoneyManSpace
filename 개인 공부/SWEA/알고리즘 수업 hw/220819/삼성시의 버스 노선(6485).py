import sys
sys.stdin = open('6485.txt', 'r')
# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    #  버스 노선 개수
    N = int(input())
    # A이상 B이하인 모든 정류장만을 다니는 버스 노선
    nosion = [list(map(int, input().split())) for _ in range(N)]
    # 버스 정류장의 개수
    P = int(input())
    # C번 버스
    C = [int(input()) for _ in range(P)]
    result = [0] * 5001
    for i in range(len(C)):
        for j in range(N):
            if nosion[j][0] <= C[i] <= nosion[j][1]:
                result[i] += 1
    print(f'#{tc}', *result[:P])
