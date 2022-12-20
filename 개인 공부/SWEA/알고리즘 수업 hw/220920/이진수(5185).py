import sys
sys.stdin = open('이진수(5185).txt','r')
# 16진수가 주어지면 2진수로 바꾸는 프로그램
# 앞자리 0도 반드시 출력

# 16진수를 2진수로 바꾸는 함수
def binary(num):
    if num < 2:
        return str(num%2)
    return str(binary(num//2)) + str(num%2)

# 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 자리수 N, N자리 16진수
    N, M = input().split()
    # 16진수 영어를 숫자로 매핑하는 딕셔너리
    M_dic = {'A':10,
             'B':11,
             'C':12,
             'D':13,
             'E':14,
             'F':15}
    # 결과 값
    result = ''
    for i in M:
        # 문자가 나오면 숫자로 바꿔서 변환
        if i in M_dic:
            i = M_dic[i]
        # 2진수로 바꾸고
        binary(int(i))
        # 만약 2진수의 길이가 4의 배수가 아니면 앞자리에 0을 채워 넣는다
        if len(binary(int(i))) % 4:
            result += (4-(len(binary(int(i))) % 4))*'0'+binary(int(i))
        else:
            result += binary(int(i))
    print(f'#{tc} {result}')