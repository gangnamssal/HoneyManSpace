# 자기 점수 중 최댓값을 M
# 모든 점수를 점수/M*100
# 과목의 갯수 N개
import sys
N = int(sys.stdin.readline())  # 과목 수를 입력 받음
lst = list(map(int,sys.stdin.readline().rstrip('\n').split())) # 과목의 점수를 리스트로 만듬
sum = 0   #합을 0으로 초기화
for i in lst:
    sum += ((int(i)/int(max(lst)))*100) # 새로운 과목 점수를 계산
print(sum/N)    # 새로운 과목 평균을 구함


