# 크로아티아 알파벳의 갯수를 찾는다
# 첫줄에 최대 100글자의 단어가 주어진다.
arr_dict = {'c=':'č','c-':'ć','dz=':'dž','d-':'đ',
            'lj':'lj','nj':'nj','s=':'š','z=':'ž'}
arr = input()
cnt = 0
# 딕셔너리의 키 값이 문자열에 포함이 되면
for i in arr_dict.keys():
    if i in arr:
        # 같은 크로아티아 알파벳이 존재하면
        if arr.count(i) > 1:
            cnt += arr.count(i)
        else:
            cnt += 1
        arr = arr.replace(i,',')
# 나머지 알파벳의 갯수를 측정
for i in arr:
    if i == ',':
        continue
    else:
        cnt += 1
print(cnt)