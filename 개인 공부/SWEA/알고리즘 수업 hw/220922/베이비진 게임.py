import sys
sys.stdin = open('베이비진 게임.txt','r')

# 0~9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 고름
# 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triple
# 교대로 한 장씩 카드를 가져감, 먼저 run이나 triple이 되는 사람이 승자
# 무승부는 0

# 테스트케이스 T
T = int(input())
for tc in range(1,T+1):
    data = list(map(int,input().split()))
    player1 = [0]*10
    player1_run = []
    player2 = [0]*10
    player2_run = []
    num_dic = {
        0:'012',
        1:'123',
        2:'234',
        3:'345',
        4:'456',
        5:'567',
        6:'678',
        7:'789'
    }
    result = 0
    for i in range(len(data)):
        # 수를 하나씩 가져간다
        if not i%2:
            player1[data[i]] += 1
            player1_run.append(str(data[i]))
            player1_run = list(set(player1_run))
            player1_run.sort()
            check_run1 = ''.join(player1_run)
            if 3 in player1:
                result = 1
                break
            else:
                for i in range(8):
                    if num_dic[i] in check_run1:
                        result = 1
                        break
                if result:
                    break
        else:
            player2[data[i]] += 1
            player2_run.append(str(data[i]))
            player2_run = list(set(player2_run))
            player2_run.sort()
            check_run2 = ''.join(player2_run)
            if 3 in player2:
                result = 2
                break
            else:
                for i in range(8):
                    if num_dic[i] in check_run2:
                        result = 2
                        break
                if result:
                    break
    print(f'#{tc} {result}')
