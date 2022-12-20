# 단어가 연속해서 존재하면 그룹 단어
# 첫째 줄에 단어의 개수 N이 들어옴
from unittest import result


N = int(input())
# 단어가 N번 나온다.
words = [input() for _ in range(N)]
cnt = 0
# 단어를 하나씩 검사
for i in range(len(words)):
    result = 0
    for j in range(1,len(words[i])):
        # 만약 앞의 단어와 뒤의 단어가 다르다면
        if words[i][j] != words[i][j-1]: 
            # 그 단어가 뒤에 나오면 result를 -1로 바꾸고
            if words[i][:j].find(words[i][j]) != -1:
                result = -1
    # -1이 아닌 단어들 갯수만 샌다
    if result != -1:
        cnt += 1
print(cnt)