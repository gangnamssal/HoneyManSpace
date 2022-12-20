import sys
sys.stdin = open('수영장.txt','r')
def dfs(n):
    global sum
    if n == 12:
        result.append(sum)
        return
    for i in range(3):
        if i == 0:
            sum += schedule[n]*day
            dfs(n+1)
            sum -= schedule[n]*day
        elif i == 1:
            sum += month
            dfs(n+1)
            sum -= month
        elif i == 2 and n <= 9:
            sum += t_month
            dfs(n+3)
            sum -= t_month



T = int(input())
for tc in range(1,T+1):
    day,month,t_month,year = map(int,input().split())
    schedule = list(map(int,input().split()))
    result = [year]
    sum = 0
    dfs(0)
    print(f'#{tc} {min(result)}')
