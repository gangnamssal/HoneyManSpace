# 어떤 양의 정수 X의 각 자리가 등차수열 그 수를 한수
# 등차수열은 연속된 두 개의 수의 차이가 일정
# N에서 한수 개수를 출력

N = int(input()) # 입력은 받음

def hansu(Num):  # 한수의 갯수를 출력하는 함수
    result = 0  # 출력
    cnt = 0    # 갯수를 새는 변수
    if Num < 100:  # 100 미만의 수는 자기 자신이 한수의 갯수
        result = Num + cnt
    else:
        for i in range(100,Num+1):  # 100 이상의 수는 각 자리의 차가 같으면 cnt를 증가
            if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2])-int(str(i)[1]):
                cnt += 1
        result = cnt + 99  # 100보다 큰 수는 cnt에 99를 더해 결과를 출력
    return result
print(hansu(N))