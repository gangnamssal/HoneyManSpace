# 문자열 my_string과 문자 letter이 매개변수
# my_string에서 letter를 제거한 문자열을 return

def solution(my_string, letter):
    result = ''
    for i in my_string:
        if i != letter:
            result += i
    return result

