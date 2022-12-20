# 번호에 적힌 숫자는 같은 조

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x,y):
    p[find_set(y)] = find_set(x)

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    # M 쌍의 번호
    num = list(map(int,input().split()))
    p=[_ for _ in range(N+1)]
    for i in range(M):
        union(num[2*i],num[2*i+1])
    result = []
    for i in range(1,N+1):
        if find_set(i) in result:
            pass
        else:
            result.append(find_set(i))
    print(f'#{tc} {len(result)}')
