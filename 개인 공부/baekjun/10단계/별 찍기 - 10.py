# N은 3의 거듭 제곱
N = int(input())
stars = [['*']*N for _ in range(N)]
s = 0   # 인덱스 스텝을 나타낸다.
# 별이 찍히는 패턴을 반복문으로 나타냈다.
while s <= N // 3:
    for i in range(3**s,N,3**(s+1)):
        for j in range(3**s,N,3**(s+1)):
            for k in range(3**s):
                for q in range(3**s):
                    stars[i+k][j+q] = ''
    s += 1
# 리스트로 만들어진 문자들을 하나로 합쳐서 출력하는 반복문
for i in stars:
    for j in i:
        if j == '*':
            print(j,end='')
        elif not j:
            print(end=' ')
    print()





