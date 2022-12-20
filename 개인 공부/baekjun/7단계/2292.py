# 첫 줄에는 방 번호가 주어진다.
N = int(input())
cnt = 1
start = 1
while True:
    # N이 1이면 그대로 출력
    if N:
        break
    # N이 벌집 테두리 내에 있으면
    if start + 6*cnt >= N:
        cnt += 1
        break
    else:
        # N이 테두리 내에 없으면
        start += 6*cnt
        cnt += 1

print(cnt)