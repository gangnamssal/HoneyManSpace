import sys
# 10개의 수를 입력 받는다
num = [] # 빈 리스트를 만든다.
for i in range(10):
    N = int(sys.stdin.readline()) # 수를 10번 받는다
    num.append(N%42)  # 받은 수를 42로 나눈 나머지를 저장한다.
num = list(set(num)) # 중복된 수를 없애고 
print(len(num)) # 원소의 갯수를 출력한다.