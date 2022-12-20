import sys
sys.stdin = open('문제 제목 붙이기.txt','r')
# 제목의 가장 앞 글자에 대문자 A~Z가 순서대로 등장
# 중간에 하나라도 안들어가면 제목 중단
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    arr.sort()
    alpha = ['']*25
    second_alpha = ['A']
    cnt = 1
    for i in range(1, 26):
        alpha[i-1] = chr(i+65)
    if arr[0][0] != 'A':
        cnt = 0
        print(f'#{tc} {cnt}')
        continue
    for i in range(0, len(arr)):
        if arr[i][0] not in second_alpha and arr[i][0] == alpha[0]:
            cnt += 1
            second_alpha.append(alpha.pop(0))
    print(f'#{tc} {cnt}')