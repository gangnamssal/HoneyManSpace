# 문자열 S를 입력받음
# 각 문자를 R번 반복해 새 문자열 P를 만들어 출력

# 첫 줄에 테스트 케이스 개수 T
import sys
from unittest import result
T = int(sys.stdin.readline())
# 반복 횟수 R, 문자열 S
for tc in range(1,T+1):
    R, S= sys.stdin.readline().rstrip('\n').split()
    result = str() # 빈 문자열에 결과를 저장
    for i in S:
        result += i * int(R) #문자를 하나하나 반복해서 R번 출력
    print(result)