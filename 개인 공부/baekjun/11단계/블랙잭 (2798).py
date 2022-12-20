# 주어진 카드로 M과 최대한 가깝게 만들 수 있는 수를 구함
def solve(n,sumV):
    # 3장을 골랐을 때 값을 저장
    if n == 3:
        result.append(sumV)
        return
    # 중간에 합이 M보다 커지면 돌아간다.
    if sumV > M:
        return
    for i in range(n,N):
        # 합이 M보다 작고 고르지 않은 카드이면 선택
        if sumV + arr[i] <= M and i not in visited:
            visited.append(i)
            solve(n+1,sumV+arr[i])
            visited.pop()


N, M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
visited = []
solve(0,0)
print(max(result))