# T=int(input())
# for tc in range(1,T+1):
#     dcost,mcost,tmcost,ycost = map(int,input().split())
#     plan=[0]+list(map(int,input().split()))
#     cost=[0]*13
#     tm=0
#     for i in range(1,13):
#         cost[i]=min(dcost*plan[i],mcost)+cost[i-1]
#         if i>=3: #3개월
#             cost[i]=min(cost[i],tmcost+cost[i-3])
#         if i==12:
#             cost[i]=min(cost[i],ycost)
#     print(f'#{tc} {cost[-1]}')

import sys
sys.stdin = open('수영장.txt','r')
t = int(input())
for tc in range(1, t + 1):
    cost = list(map(int, input().split()))
    months = list(map(int, input().split()))
    cost_daily = []
    cnt = 0
    ans = [cost[3]]

    def dfs(n):
        global cnt

        if n == 12:
            ans.append(cnt)
            return

        for i in range(3):
            if i == 0:
                cnt += cost[0] * months[n]
                dfs(n + 1)
                cnt -= cost[0] * months[n]
            elif i == 1:
                cnt += cost[1]
                dfs(n + 1)
                cnt -= cost[1]
            elif i == 2 and n <= 9:
                cnt += cost[2]
                dfs(n + 3)
                cnt -= cost[2]

    dfs(0)
    print(ans)
    print(f'#{tc} {min(ans)}')