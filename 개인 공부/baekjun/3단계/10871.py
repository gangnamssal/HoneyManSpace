import sys
N, X = map(int,sys.stdin.readline().split()) # 정수 N과 정수X를 입력받음
A = sys.stdin.readline().rstrip('\n').split(' ') #문자열로 받은
lst = str()      # 빈 문자열을              #수열을 띄어쓰기를 기준으로 나눠 리스트로 만듬
for i in A:
    if int(i) < X:  # 수를 비교해서 X보다 작으면
        lst += i+' ' # 문자열에 추가
    else:
        continue
print(lst)




