import sys

while True:  # try-except 구문을 사용해 오류가 나면 나오게 한다.
    try: 
        A,B = map(int,sys.stdin.readline().split())
        print(A+B)
    except:
        break