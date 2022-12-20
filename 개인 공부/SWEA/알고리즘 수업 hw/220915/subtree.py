import sys
sys.stdin = open('subtree.txt','r')
# 첫 줄에 테스트 케이스
def preorder(N):
    global cnt
    if N:
        cnt += 1
        preorder(ch1[N])
        preorder(ch2[N])
    return cnt

T = int(input())
for tc in range(1,T+1):
    # 간선의 개수 E와 N
    E, N = map(int,input().split())
    # E개의 부모 자식 노드 번호 쌍
    node = list(map(int,input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    cnt = 0
    for i in range(0,E*2,2):
        p, c = node[i], node[i+1]
        if not ch1[p]:
            ch1[p] = c
        else:
            ch2[p] = c

    print(f'#{tc} {preorder(N)}')


