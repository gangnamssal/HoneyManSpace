# N*N 배열
# 한줄에 하나씩 N개의 숫자를 골라 합이 최소가 되도록 함
# 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
import sys
sys.stdin = open('lst_sum.txt', 'r')

def min_num(start):
    least = 11
    idx = -1
    global result
    if start == N:
        return result
    for i in range(N):
        if check[i] == 1:
            continue
        if least > num_arr[start][i]:
            least = num_arr[start][i]
            idx = i
    check[idx] += 1
    result += least
    min_num(start+1)
    return result

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # 숫자 N
    N = int(input())
    # 자연수 배열
    num_arr = [list(map(int,input().split())) for _ in range(N)]
    check = [0]*N
    result = 0
    print(f'#{tc} {min_num(0)}')

#-----------------------------------------------------------------#


def backtrack(row, n, now_sum, visited):
    global min_sum  # 최소합을 전역변수로 선언
    if row == n:  # i가 배열의 수와 일치하면
        # 현재 합과 (지금까지)최소합 값을 비교
        if now_sum < min_sum:
            min_sum = now_sum  # 현재합이 더 작으면 대체
    elif now_sum > min_sum:
        return  # 현재 부분합이 더 크면 탐색 중지 (Pruning)
    else:
        for col in range(n):
            if not visited[col]:  # 방문 전인 컬럼
                visited[col] = 1  # 방문처리
                # 다음 row로 넘어가고, now_sum에 값을 더해주고, visited 갱신
                backtrack(row + 1, n, now_sum + num[row][col], visited)
                visited[col] = 0  # 함수 적용 후 초기화 (재검색 할 수 있도록)


T = int(input())
for tc in range(T):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 100  # 값을 대체해주기 임의의 큰 수 대입
    visited = [0] * n

    backtrack(0, n, 0, visited)  # 함수시작
    print(f'#{tc + 1} {min_sum}')