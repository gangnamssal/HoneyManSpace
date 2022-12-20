import sys
sys.stdin = open('사칙연산.txt','r')
# 10개의 테스트 케이스
for tc in range(1,11):
# 첫 줄에는 정점의 개수 N
    N = int(input())
# 그 다음 N 줄에 정점의 정보
# 정점이 정수면 정점 번호와 양의 정수
# 연산자이면 정점 번호, 연산자, 왼쪽, 오른쪽 자식의 정점 번호
# 정점 번호는 1부터 N까지의 정수, 루트 정점의 번호는 항상 1
    arr = [list(input().split()) for _ in range(N)]
    lst = [0]
    perent = [0]*(N+1)
    # 정점 번호별로 값을 새리스트에 저장
    for i in range(N):
        lst.append(arr[i][1])
        if len(arr[i]) == 4:
            # 자식 - 부모를 연결하는 리스트
            perent[int(arr[i][2])] = int(arr[i][0])
            perent[int(arr[i][3])] = int(arr[i][0])
    # 계산을 위한 변수
    cal = 0
    # 자식에게 연결된 부모를 계산하는 과정
    for j in range(N,2,-2):
        if lst[perent[j]] == '-':
            cal = float(lst[j-1]) - float(lst[j])
            lst[perent[j]] = cal
        elif lst[perent[j]] == '+':
            cal = float(lst[j-1]) + float(lst[j])
            lst[perent[j]] = cal
        elif lst[perent[j]] == '*':
            cal = float(lst[j-1]) * float(lst[j])
            lst[perent[j]] = cal
        elif lst[perent[j]] == '/':
            cal = float(lst[j-1]) / float(lst[j])
            lst[perent[j]] = cal
    print(f'#{tc} {int(cal)}')