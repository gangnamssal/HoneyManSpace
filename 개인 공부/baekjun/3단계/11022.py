import sys
T = int(sys.stdin.readline()) # 테스트 갯수를 입력함
for i in range(1,T+1):  # 테스트 갯수만큼 수를 입력 받고 합을 출력
    A, B = map(int,sys.stdin.readline().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')