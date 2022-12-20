#상자를 높은 곳에서 낮은 곳으로 옮기는 방식
#평탄화 잡업을 하면 최고 높이와 최저 높이차 1
for tc in range(1,11):
    dump_num = int(input())
    heigh = list(map(int,input().split()))

    max_heigh = 0
    min_heigh = 0
    result = -1
    # 덤프 횟수가 남아도 평탕화가 끝나면 끝
    while True:
        # for i in range(len(heigh)-1,0,-1):
        #     for j in range(0,i):
        #         if heigh[j] > heigh[j+1]:
        #             heigh[j], heigh[j+1] = heigh[j+1], heigh[j]
        heigh.sort()
        if dump_num == 0:
            result = (heigh[-1] - heigh[0])
            break

        if (heigh[-1] - heigh[0]) <= 1:
            result = (heigh[-1] - heigh[0])
            break
        else:
            dump_num -= 1
            heigh[0] += 1
            heigh[-1] -= 1

        
    print(f'#{tc} {result}')



