# 나이가 증가하는 순으로 나이가 같으면 먼저 가입한 사람이
# 앞에 온다.
import sys
N = int(sys.stdin.readline())
# 나이를 인덱스로 받아 저장하는 리스트
data = [[] for _ in range(201)]
for i in range(N):
    age, name = input().split()
    data[int(age)].append([age, name])
# 입력 받은 데이터를 출력
for i in data:
    for j in i:
        print(*j)