# N 명의 학생이 N장의 카드를 나눠 갖는다.
# 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자
# 같은 카드면 번호가 작은 쪽이 승리
import sys
sys.stdin = open('card.txt','r')
# 첫 줄에 테스트 케이스 개수
def game(start, end):
    if start == end:
        return start
    a = game(start,(start+end)//2)
    b = game((start+end)//2+1,end)
    return rsp(a, b)

def rsp(x, y):
    if numbers[x] == numbers[y]:
        return x
    elif numbers[x] - numbers[y] == 1 or numbers[x] - numbers[y] == -2:
        return x
    return y

T = int(input())
for tc in range(1, T+1):
    # 인원수 N
    N = int(input())
    # N명이 고른 카드가 번호순으로 주어짐
    numbers = list(map(int, input().split()))
    print(f'#{tc} {game(0,N-1)+1}')

