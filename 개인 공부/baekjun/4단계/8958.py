import sys
# 테스트 케이스 개수
N = int(sys.stdin.readline())
sum = 0 #수들의 합
cnt = 0 #O의 갯수를 카운트 하는 변수
for i in range(N):  
    lst = sys.stdin.readline()
    for j in lst:  # 문자열을 하나씩 검사
        if j == 'O': # O가 나오면
            cnt += 1  # 카운트를 1개 증가하고
            sum += cnt # 카운트를 더한다.
        else:
            cnt = 0 # X가 나오면 카운트를 초기화한다.
    print(sum)
    sum = 0