import sys
# 좌표가 주어지고
# 주어진 좌표 중 현재 좌표보다 작은 좌표의 개수가 압축 좌표가 된다.

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
# set을 이용해서 중복 데이터를 없앤다.
set_data = list(set(data))
set_data.sort()
result = {}
# 숫자의 인덱스 값을 딕셔너리에 같이 저장한다.
for i in range(len(set_data)):
    result[set_data[i]] = i
# 입력 숫자에 맞는 딕셔너리 값을 출력한다.
for i in data:
    print(result[i],end=' ')





