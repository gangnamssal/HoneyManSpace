# 알파벳 대소문자로 된 단어에서 가장 많이 사용된 알파벳을 구함

# 첫째 줄에 알파벳 대소문자로 이뤄진 단어가 주어짐
import sys
from unittest import result
# 단어를 입력 받음 # 단어를 전부 소문자로 바꿈
words = sys.stdin.readline().rstrip('\n').lower()
words_dict = {}
max_num = 0
# 딕셔너리에 알파벳 키와 갯수 벨류를 받음
for i in words:
    if words_dict.get(i):
        words_dict[i] += 1
    else:
        words_dict[i] = 1
# 벨류값이 가장 큰 것을 result에 저장
for i in words_dict:
    if max_num < words_dict.get(i):
        max_num = words_dict.get(i)
        result = i.upper() # 결과를 대문자로 출력
words_dict.pop(result.lower()) # 내부에 같은 수의 알파벳이 존재할 수 있으므로 result를 제거하고 비교
for i in words_dict: # 만약 같은 수의 알파벳이 추가로 있으면 ?를 출력
    if max_num == words_dict.get(i):
        result = '?'
print(result)

# 시간 초과난 코드
# 단어들의 갯수가 가장 큰 값을 max_num에 저장
# max_num = 0
# cnt = 0
# result = str()
# for i in range(len(words)):
#     if max_num < words.count(words[i]):
#         max_num = words.count(words[i])
#         result = words[i].upper()
# for i in range(len(words)):
#     if words.count(words[i]) == max_num:
#         cnt += 1
# if (cnt / max_num) >= 2:
#     result = '?'
# print(result)
    