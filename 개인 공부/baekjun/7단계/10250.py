# 정문에서 가장 짧은 거리의 방을 선호
# w개의 방이 있는 H층
# 엘리베이터는 가장 왼쪽
# 정문은 1층 엘리베이터 앞에 있음
# 방 번호 Y는 층 수 X는 방 번호

# 테스트 테이터 T
T = int(input())
for tc in range(1, T+1):
    # H 층수, W 방수, N 몇 번째 손님
    H, W, N = map(int,input().split())
    # H * W의 2차원 배열을 생성
    arr = [[0]*(W+1) for _ in range(H+1)]
    cnt = 0
    # 6번 행이 1번방
    # 6번 행부터 탐색
    for j in range(1,W+1):
        for i in range(H,0,-1):
            arr[i][j] = 1
            cnt += 1
            # cnt가 손님 수랑 같으면 나옴
            if cnt == N:
                break
        if cnt == N:
                break
    # 반대로 되어 있으므로 출력할 때의 형태도 달라진다.
    if j < 10:
        print(f'{(H+1)-i}0{j}')
    else:
        print(f'{(H+1)-i}{j}')
            