import sys
sys.stdin = open('암호코드 스캔.txt','r')
# 암호코드 규칙
# 1. 8개의 숫자
# 2. 앞 7자리는 상품 고유의 번호, 마지막 자리는 검증 코드
# 3. (짝수자리 합)*3 + 홀수자리 합 + 검증코드 = 10의 배수가 되어야 한다.

# 스캐너 성능
# 1. 세로 2000, 가로 500 이하의 크기
# 2. 비정상적인 암호코드가 포함될 수 있다.
# 3. 배열은 16진수, 2진수로 변환하여 정보를 확인해야한다.
# 4. 정상적인 암호코드들을 판별한 뒤 숫자들의 합을 출력

# 규칙
# 1. 암호코드들이 붙어있는 경우는 없다.
# 2. 모든 암호코드는 8개의 숫자
# 3. 암호코드의 세로 길이는 5~100칸
# 4. 암호코드의 가로 길이는 두께에 따라 달라짐, 두께가 가장 가는 경우
#    숫자 하나가 차지하는 길이는 7칸
# 5. 숫자 밑의 수는 비율을 의미
# 6. 선이 굵어질 경우 56의 배수 길이를 갖는다.
change = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

numbers = {
    (3,2,1,1):0,
    (2,2,2,1):1,
    (2,1,2,2):2,
    (1,4,1,1):3,
    (1,1,3,2):4,
    (1,2,3,1):5,
    (1,1,1,4):6,
    (1,3,1,2):7,
    (1,2,1,3):8,
    (3,1,1,2):9,
}
T = int(input())
for tc in range(1,T+1):
    # N 세로, M 가로
    N, M = map(int,input().split())
    data = [input() for _ in range(N)]
    new_data = ['' for _ in range(N)]
    for i in range(len(data)):
        for j in data[i]:
            new_data[i] += change[j]
    result_sum = 0
    check = []
    for i in range(len(new_data)):
        result = []
        if '1' in new_data[i]:
            j = len(new_data[i]) - 1
            while j > 0:
                if new_data[i][j] == '1':
                    n1=n2=n3=n4=0
                    while new_data[i][j] == '1':
                        n4 += 1
                        j -= 1
                    while new_data[i][j] == '0':
                        n3 += 1
                        j -= 1
                    while new_data[i][j] == '1':
                        n2 += 1
                        j -= 1
                    min_num = min(n2,n3,n4)
                    n2 //= min_num
                    n3 //= min_num
                    n4 //= min_num
                    n1 = 7 - n2 - n3 - n4
                    j -= n1*min_num
                    if numbers.get((n1,n2,n3,n4)) == 0 or numbers.get((n1,n2,n3,n4)):
                        result.append(numbers.get((n1,n2,n3,n4)))
                    if len(result) == 8 and result not in check:
                        check.append(result)
                        odd_sum = result[0] + result[2] + result[4] + result[6]
                        even_sum = result[1] + result[3] + result[5] + result[7]
                        if not (odd_sum + even_sum * 3) % 10:
                            result_sum += odd_sum + even_sum
                        result = []
                else:
                    j -= 1

    print(result_sum)




