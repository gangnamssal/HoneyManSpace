A, B = map(int,input().split()) # 현재 시간
C = int(input()) # 예상 시간

A = A + (C // 60) # 예상 시간을 계산
B = B + (C % 60)
if B >= 60: # 60분이 넘는 상황
    A = A + 1
    B = B - 60
    if A > 23: # 23시가 넘는 상황
        A = A - 24
if A > 23: # A가 24시가 넘을 경우
    A = A - 24
print(str(A) + ' ' + str(B))