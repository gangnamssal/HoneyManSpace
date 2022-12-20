# N명의 학생들 중 점수가 가장 높은 k명이 상을 받는다.
# 이때 커트라인이 몇 점인지

N, k = map(int,input().split())
x = list(map(int,input().split()))
# 수를 정렬한다
x.sort(reverse=True)
# 인덱스의 표현이니 k-1번째의 수를 출력하면 된다.
print(x[k-1])