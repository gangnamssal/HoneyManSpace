import sys
N = int(sys.stdin.readline()) # N 개의 정수를 받는다.
lst = list(map(int,sys.stdin.readline().rstrip('\n').split())) # 문자열로 받은 N개의 정수를
print(min(lst),max(lst))                                        #int로 바꿔주고 list에 담는다.
#min값과 max값을 출력한다.