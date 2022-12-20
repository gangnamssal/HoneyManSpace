import sys
sys.stdin = open('1945.txt','r')
# 첫 줄에는 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N > 1:
        if not N % 2:
            N /= 2
            a += 1
            continue
        if not N % 3:
            N /= 3
            b += 1
            continue
        if not N % 5:
            N /= 5
            c += 1
            continue
        if not N % 7:
            N /= 7
            d += 1
            continue
        if not N % 11:
            N /= 11
            e += 1
            continue
    print(f'#{tc} {a} {b} {c} {d} {e}')