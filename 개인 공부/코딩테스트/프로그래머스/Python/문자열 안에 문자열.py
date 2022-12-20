# 문자열 str1, str2가 매개변수
# str1 안에 str2가 있다면 1을 없다면 2를 return

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2