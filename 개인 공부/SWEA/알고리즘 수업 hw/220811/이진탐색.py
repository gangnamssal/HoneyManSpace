# A와 B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면
# 이진 탐색 만으로 지정된 페이지를 먼저 펼치는 사람이 이김
# 첫 줄에 테스트 케이스 갯수 T
from unittest import result


T = int(input())
for tc in range(1,T+1):
    # 전체 쪽 수 P, A, B가 찾을 쪽수
    P, A, B = map(int,input().split())
    P_B = P
    i_A = 1
    i_B = 1
    cnt_A = 0
    cnt_B = 0
    while True:
        # A가 먼저 탐색
        middle_A = (i_A + P) // 2
        if middle_A == A:
            pass
        elif middle_A < A:
            i_A = middle_A
        elif middle_A > A:
            P = middle_A
        # A 탐색이 끝나면 카운트 1 증가
        cnt_A += 1
        middle_B = (i_B + P_B) // 2
        if middle_B == B:
            pass
        elif middle_B < B:
            i_B = middle_B
        elif middle_B > B:
            P_B = middle_B
        # B 탐색이 끝나면 카운트 1 증가
        cnt_B += 1
        # A랑 B가 동시에 끝나는 경우
        if (middle_B == B) & (middle_A == A) & (cnt_A == cnt_B):
            result = 0
            break
        elif (middle_B == B) & (middle_A != A):
            result = 'B'
            break
        elif (middle_B != B) & (middle_A == A):
            result = 'A'
            break
    print(f'#{tc} {result}')
            