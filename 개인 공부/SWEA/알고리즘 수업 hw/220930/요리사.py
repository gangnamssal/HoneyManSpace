# import sys
# sys.stdin = open('요리사.txt','r')
# N개의 식재료가 있다.
# N/2개씩 나누어 두 개의 요리를 한다.
# A음식과 B음식 맛의 차이가 최소가 되도록 재료를 배분
# 식재로 i,j는 시너지 Sij가 발생
# 음식의 맛은 시너지들의 합

# 식재료의 수 N은 4이상 16이하의 짝수
# 시너지 Sij는 1이상 20000이하의 정수
def nCr(n, ans, r):
    if n == len(arr):
        if len(ans) == r:
            temp = [i for i in ans]
            A = 0
            for i in range(len(temp)):
                for j in range(i,len(temp)):
                    A += Sij[temp[i]][temp[j]] + Sij[temp[j]][temp[i]]
            comb.append(A)
        return
    ans.append(arr[n])
    nCr(n + 1, ans, r)
    ans.pop()
    nCr(n + 1, ans, r)

# 테스트 케이스 T
T = int(input())
for tc in range(1,T+1):
    # 식재료의 수 N
    N = int(input())
    Sij = [list(map(int,input().split())) for _ in range(N)]
    arr = [_ for _ in range(0,N)]
    comb = []
    nCr(0,[],N/2)
    minV = 0xffffff
    for i in range(len(comb)):
        value = abs(comb[i]-comb[len(comb)-1-i])
        if minV > value:
            minV = value
    print(f'#{tc} {minV}')
