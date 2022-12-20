import sys
sys.stdin = open('정식이의 은행업무.txt','r')
# 2진수, 3진수를 한 자리만 잘못 기억
# 두 수가 같은 수를 출력

# 2진수를 10진수로 바꾸는 함수
def change_bi(arr):
    result = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[len(arr)-i-1] == '1':
            result += 2**i
    return result
# 3진수를 10진수로 바꾸는 함수
def change_thi(arr):
    result = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[len(arr)-i-1] == '2':
            result += 3**i*2
        elif arr[len(arr)-i-1] == '1':
            result += 3 ** i
    return result

# 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    data = [list(input()) for _ in range(2)]
    result = []
    for i in range(2):
        # 2진수를 한 자리씩 바꾸면서 10진수 값을 넣는다.
        if not i%2:
            check = data[0][:]
            for j in range(len(data[i])):
                if check[j] == '0':
                    check[j] = '1'
                elif check[j] == '1':
                    check[j] = '0'
                result.append(change_bi(check))
                check = data[0][:]

        else:
            # 3진수의 값을 바꾸면서 10진수로 변환하고 result에 집어 넣는다.
            check = data[1][:]
            for j in range(len(data[i])):
                for k in range(3):
                    check[j] = f'{k}'
                    result.append(change_thi(check))
                    check = data[1][:]
    # 결과들 중 갯수가 2개이고 원래의 숫자와 값이 같지 않은 수를 출력
    for i in result:
        if i != change_bi(data[0]) and i != change_thi(data[1]) and result.count(i)==2:
            same_result = i
    print(f'#{tc} {same_result}')
