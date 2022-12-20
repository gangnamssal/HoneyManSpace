# 수가 10보다 작다면 앞에 0을 붙여 두 자리로 만들고 각 자리를 더함
# 수의 가장 오른쪽 수와 구한 합의 가장 오른쪽 자리를 이어 붙여 새로운 수를 만듬
import sys
N = sys.stdin.readline() # 첫 번째 숫자를 입력 받음
num = N[:]         # 얕은 복사로 같은 수를 다른 주소로 복사
sum = 0      # N의 두 수를 더하는 함수
cnt = 1      # 카운터 하는 변수
if 0 <= int(N) < 10:  # N이 10 미만의 경우
    N = str(0)+N

while True:
    sum = int(N[0])+int(N[1]) # sum을 구함
    if int(str(int(N)%10)+str(sum%10)) == int(num): #sum이 첫 수와 같음 나옴
        break 
    else:
        N = str(int(N)%10) + str(sum%10) #아니면 N을 교체함
        cnt += 1                            # 카운터를 1 증가

print(cnt)