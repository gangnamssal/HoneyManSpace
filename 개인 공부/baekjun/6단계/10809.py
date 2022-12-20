# 소문자로 이뤄진 단어 S
# 알파벳에 대하여 있으면 처음 등장하는 위치를
# 없으면 -1을 출력
import sys
# 첫 줄에 단어 S
S = sys.stdin.readline().rstrip('\n')
# 빈 문자열에 결과를 저장
result = str()
# 아스키 코드 소문자의 숫자 범위
for i in range(97,123):
    if chr(i) not in S:  # 숫자를 아스키 코드로 변환한 것이 문자열에 없으면
        result += str(-1)+' ' 
    else:  # 있으면 index값을 받아 온다.
        result += str(S.index(chr(i))) + ' '
print(result)