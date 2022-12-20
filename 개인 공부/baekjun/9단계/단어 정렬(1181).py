import sys
# 알파벳 소문자로 이루어진 N개의 단어를 정렬
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

N = int(sys.stdin.readline())
# 문자열의 최대 길이가 50이라 50번까지 리스트를 만듬
words = [[] for _ in range(51)]
for i in range(N):
    word = sys.stdin.readline().rstrip('\n')
    # 문자열 길이에 해당하는 리스트에 문자열을 저장
    if word not in words[len(word)]:
        words[len(word)].append(word)

for i in words:
    if i:
        # 저장된 문자열을 정렬하여 출력
        i.sort()
        for j in i:
            print(j)
