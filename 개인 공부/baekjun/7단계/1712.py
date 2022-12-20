# 고정비 A, 가변비B, 가격C
# 손익 분기점을 계산

# 첫 줄에 A, B, C가 주어진다.
import sys
A, B, C = map(int,sys.stdin.readline().rstrip('\n').split())
i = 0
D = C - B
# 가변비가 가격보다 높으면 -1을 반환
if D <= 0:
    i = -1
    # 가격과 가변비를 뺀 이익이 고정비를 넘어서는 갯수를 반환
else:
    i = (A // D) + 1
print(i)