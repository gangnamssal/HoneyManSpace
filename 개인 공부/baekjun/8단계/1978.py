# 주어진 수 N개 중에서 소수가 몇 개인지 출력

# 소수를 구하는 함수
def sosu(num):
    cnt = 0             # 소수를 저장하는 변수
    for i in num_lst:   # 받은 숫자들을 하나씩 검사
        result = -1     # 소수가 아니면 0을 출력함
        if i == 1:      # 1이 있으면 넘어감
            continue
        for j in range(2, i):   # 검사하는 수보다 작은 수를 하나씩 나눠서 검사
            if not i % j:       # 소수가 아니면 return을 0으로 하고 나온다
                result = 0
                break
        if result != 0:         # 소수가 아닌 수만 카운트
            cnt += 1
    return cnt

# 첫 줄에 수의 개수 N
N = int(input())
# 다음으로 N개의 수가 주어짐
num_lst = list(map(int, input().split()))
print(sosu(num_lst))