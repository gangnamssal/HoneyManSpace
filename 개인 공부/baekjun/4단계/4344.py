# 테스트 케이스 개수 C
# 학생수 N, N명의 점수
# 소수점 넷쩨 자리에서 반올림
import sys
C = int(sys.stdin.readline()) # 테스트 케이스 개수
sum = 0
avr = 0
num_list = []
for i in range(C):
    N = list(map(int,sys.stdin.readline().rstrip('\n').split())) # 점수를 리스트로 만듬
    for j in range(1,len(N)): # 점수의 합을 구함
        sum += N[j]
    avr = float(sum / N[0]) # 평균을 구함
    for j in N[1:]:
        if j > avr: # 평균보다 높으면 저장
            num_list.append(j)
    print('%.3f'%(len(num_list)/N[0]*100))
    sum = 0
    avr = 0
    num_list = []
