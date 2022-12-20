H, M = map(int,input().split()) # 시간을 받음

if 45 <= M < 60:  # 분이 45분 이상
    M = M - 45
    print(str(H) + ' ' + str(M))
elif 45 > M and H != 0: # 시간이 0시가 아니고 분이 45분보다 작으면
    M = 60 - (45-M)
    H = H - 1
    print(str(H) + ' ' + str(M))
else:  # 시간이 0시고 분이 45분 이하이면
    M = 60 - (45-M)
    H = 23
    print(str(H) + ' ' + str(M))