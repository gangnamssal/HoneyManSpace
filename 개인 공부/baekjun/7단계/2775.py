# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터
# b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다
# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # 첫 줄에 정수 k, k층
    k = int(input())
    # 둘 째줄에 정수 n, n호
    n = int(input())
    # 0층을 미리 준비한다.
    room = [_ for _ in range(n+1)]
    # 다음 층을 계산할 리스트
    next_room = [0]*(n+1)
    # k-1번 층까지 구한다.
    floor = 0
    while floor < k:
        result = 0
        for i in range(1, len(room)):
            result += room[i]
            next_room[i] = result
        room = next_room
        floor += 1
    print(room[n])

