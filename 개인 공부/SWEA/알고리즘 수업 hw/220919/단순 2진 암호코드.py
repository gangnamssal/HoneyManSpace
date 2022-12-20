import sys
sys.stdin = open('단순 2진 암호코드.txt','r')
# 암호코드는 8개의 숫자
# 올바른 암호코드 (홀수 자리의 합*3) + (짝수 자리의 합)이 10의 배수
# 스캐너는 암호코드 1개가 포함된 직사각형 배열을 읽는다.
# 암호코드 이외의 부분은 전부 0

# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 배열의 세로 크기 N, 배열의 가로 크기 M
    # 1<= N <=50, 56<=M<=100
    N, M = map(int,input().split())
    # N개의 줄에 걸쳐 직사각형 배열
    password_lst = [list(map(int,input())) for _ in range(N)]
    # 암호가 있는 행을 저장하는 변수
    row = 0
    # 1이 나오는 열을 찾는다.
    for i in range(N):
        for j in range(M):
            if password_lst[i][j]:
                row = i
                break
        if row:
            break
    # 리스트를 만들어 숫자들의 규칙을 저장
    num_lst = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],
               [0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

    # 맨 뒤의 1이 처음 나오는 열
    col = 0
    for i in range(M-1, -1,-1):
        if password_lst[row][i]:
            col = i
            break
    # 맨 뒤의 수가 1로 끝나기 때문에 뒤에서부터 탐색
    # 수를 저장하는 list
    lst = [0,0,0,0,0,0,0]
    # 7번 카운트 하는 변수
    cnt = 6
    # 수를 저장하는 리스트
    result_lst = []
    for i in range(col,-1,-1):
        lst[cnt] = password_lst[row][i]
        cnt -= 1
        # 수를 7개 확인하고 result_lst에 암호에 맞는 인덱스 값을 넣는다.
        if cnt == -1:
            result_lst.append(num_lst.index(lst))
            lst = [0,0,0,0,0,0,0]
            cnt = 6
            # 남은 수가 전부 0이면 그냥 나온다.
            if 1 not in password_lst[row][0:i+1]:
                break

    # result_lst의 길이
    num = len(result_lst)
    # 합
    sum_lst = 0
    for i in range(num-1,-1,-1):
        if not i%2:
            sum_lst += result_lst[i]
        else:
            sum_lst += result_lst[i]*3
    # 만약 합이 10의 배수라면 결과를 출력
    if not sum_lst % 10:
        print(f'#{tc} {sum(result_lst)}')
    else:
        print(f'#{tc} 0')



