import sys
sys.stdin = open('4873.txt','r')
# 반복문자를 지운다.
# 첫 줄에 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    strs = list(input())
    # 문자열 검사 횟수
    i = 0
    while i < len(strs)-1:
        # 앞과 뒤가 같으면 둘다 제거
        if strs[i] == strs[i+1]:
            strs.pop(i)
            strs.pop(i)
            # 다시 처음부터 검사
            i = 0
        i += 1
    print(strs)