A, B, C = map(int,input().split()) # 세가지 수를 입력 받는다.
num_list = [A, B, C] # 세 가지 수를 리스트로 만듦
sum = 0 # 합을 초기화
for i in num_list:
    if num_list.count(i) == 3: # 리스트 내에 같은 원소가 3개인 경우
        sum = 10000 + i*1000    # sum을 출력하고 나온다.
        break
    elif num_list.count(i) == 2: # 리스트 내에 같은 원소가 2개인 경우
        sum = 1000 + i * 100   # sum을 출력하고 나온다.
        break
    elif num_list.count(i) == 1: # 위의 2 경우가 아닌 경우 sum을 출력한다.
        sum = max(num_list)*100
print(sum)
