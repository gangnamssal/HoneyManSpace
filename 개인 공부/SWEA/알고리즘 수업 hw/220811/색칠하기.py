
import sys
sys.stdin = open('color_input.txt','r')
# 첫 줄에 테스트 케이스 T
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #색상 1, 2의 위치를 저장하는 리스트, 내부값은 셋이다.
    position = [set({}), set({})]
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        #x, y를 돌면서 set에 넣는다.
        for a in range(x1, x2+1):
            for b in range(y1, y2+1):
                position[color-1].add((a, b))
    #교집합을 이용하여 겹치는 부분만 꺼낸다.
    result = position[0] & position[1]
    #겹치는 만큼 출력
    print(f'#{tc} {len(result)}')

