import sys
# 2차원 평면 위의 점 N개
# x좌표를 증가하는 순으로, y좌표가 같으면 s좌며가 증가하는 순으로 정렬

# 점의 개수 N(1이상 100000이하)
N = int(sys.stdin.readline().strip('\n'))
# +x좌표 리스트에 y좌표를 저장하는 빈 리스트
data_plus = [[] for _ in range(100001)]
# -x좌표 리스트에 y좌표를 저장하는 빈 리스트
data_minus = [[] for _ in range(100001)]
# i번 점의 위치 xi와 yi
for i in range(N):
    xi, yi = map(int,sys.stdin.readline().strip('\n').split())
    if yi >= 0:
        data_plus[yi].append(xi)
    else:
        data_minus[-yi].append(xi)
# y좌표가 (-) 값인 리스트부터 출력
for i in range(100000,-1,-1):
    if data_minus[i]:
        data_minus[i].sort()
        for j in data_minus[i]:
            print(j, -i)
# 그 다음 y좌표가 (+) 값인 리스트 출력
for i in range(100001):
    if data_plus[i]:
        data_plus[i].sort()
        for j in data_plus[i]:
            print(j, i)
