# N은 홀수
'''
1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최반값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
import sys
N = int(sys.stdin.readline())   # 입력 받기
data = [int(sys.stdin.readline()) for _ in range(N)]    # N줄의 데이터
data.sort()                     # 받은 데이터를 오름차순으로 정렬
result = {}
for i in data:                  # 받은 데이터를 바탕으로 나온 수의 갯수를 딕셔너리로 만든다.
    if result.get(i):           # i 값이 있다면 1 증가시킨다.
        result[i] += 1
    else:                       # 만약 딕셔너리에 i 값이 없다면 생성
        result[i] = 1
print(round(sum(data)/N))       # 산술평균
print(data[N//2])               # 중앙값
if len(data)==1:                # 데이터 값이 1개라면 그냥 출력
    print(data[0])
    # 데이터 딕셔너리를 내림차순으로 정렬 후 같은 갯수가 없으면 앞의 값을 출력
elif sorted(result.items(), key=lambda x:x[1],reverse=True)[0][1] > sorted(result.items(), key=lambda x:x[1],reverse=True)[1][1]:
    print(sorted(result.items(), key=lambda x:x[1],reverse=True)[0][0])
else:   # 같은 갯수가 있으면 뒤의 값을 출력
    print(sorted(result.items(), key=lambda x:x[1],reverse=True)[1][0])
print(data[-1] - data[0])   # 범위