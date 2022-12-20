import sys
sum = 0  # 합을 0으로 초기화
sum_case = str()  # 결과를 출력하는 문자열 함수
while True:
    A, B = map(int,sys.stdin.readline().split()) # A와 B를 받음
    if A == 0 and B == 0:  # 반복문을 빠저나오는 조건
        break
    sum = A + B
    sum_case += str(sum)+'\n' 
print(sum_case)

        