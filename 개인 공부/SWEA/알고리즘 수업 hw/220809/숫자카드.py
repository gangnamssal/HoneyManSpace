# 0~9까지 숫자가 적힌 N장의 카드
# 가장 많은 카드가 적힌 숫자와 카드가 몇 장인지 출력
# 같을 때는 숫자가 큰 수를 출력

#테스트 케이스 개수
T = int(input())

for tc in range(1,T+1):
    # 숫자 길이
    N = int(input())
    # 숫자열
    N_num = input()
    counts = [0]*10
    max_num = 0
    max_index = 0
    # counts에 숫자의 갯수를 저장
    for i in range(len(N_num)):
        counts[int(N_num[i])] += 1
        if max_num < counts[int(N_num[i])]:
            max_num = counts[int(N_num[i])]
    # 인덱스를 출력하는데 가장 큰 인덱스 출력
    for i in range(len(counts)):
        if counts[i] == max_num:
            if max_index < i:
                max_index = i
    print(f'#{tc} {max_index} {max_num}')
    
    

