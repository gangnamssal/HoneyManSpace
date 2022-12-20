N = input() # input을 받는다.
if N.isalpha:  # 알파벳이 아니라면
    print(ord(N))  # 숫자를 문자로 변환
else:
    print(chr(N)) # 알파벳이라면 문자를 숫자로 변환