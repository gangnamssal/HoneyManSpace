import sys
sys.stdin = open('전자키드.txt','r')
def solve(start,v,cnt):
    global minV
    if cnt == N and not check[-1] and minV > v:
        minV = v
        return
    else:
        # v값이 최소값보다 커지는 순간 다시 돌아감
        if v > minV:
            return
        # 첫 번째 행부터 검사
        for i in range(N):
            # 만약 값이 0이 아니고 방문한 적이 없으면
            if data[start][i] and i not in check:
                # 방문 체크
                check.append(i)
                # 다음 행으로 넘어감
                solve(i,v+data[start][i],cnt+1)
                # 방문한 것을 초기화
                check.pop()

# 각 구역을 한 번씩만 방문하고 돌아왔을 때 배터리 사용량의 최소를 구함
# 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    # 최솟값을 구하는 변수
    minV = 999999
    # 방문한 적이 있는지 확인하는 리스트
    check = []
    solve(0,0,0)
    print(f'#{tc} {minV}')
