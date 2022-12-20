# 0<= N < 1 십진수를 이진 수로 변경
# 12자리 이내에 이진수로 표현할 수 있으면 출력
# 아니면 overflow를 출력

# 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    N = input()
    # .에 인덱스를 계산
    K = N.index('.')
    result = ''
    while True:
        # .의 인덱스 계산
        K = N.index('.')
        # 소수만 본다
        number = N[K + 1:]
        # 소수를 만든다
        new_number = float('0' + '.' + number)
        next_number = new_number * 2
        N = str(next_number)
        # 소수점 앞자리 저장
        result += N[0]
        if N == '1.0':
            break
        elif len(result) > 12:
            result = 'overflow'
            break
    print(f'#{tc} {result}')