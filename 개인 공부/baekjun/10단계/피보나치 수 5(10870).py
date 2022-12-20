# 피보나치의 수를 출력
N = int(input())
data = [0,1]
cnt = 0
if N == 0:
    print('0')
else:
    while cnt < N-1:
        data.append(data[-1]+data[-2])
        cnt += 1
    print(data[-1])