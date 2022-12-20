import sys
sys.stdin = open('패턴 마디의 길이.txt','r')

# 마디의 길이를 출력

T = int(input())
for tc in range(1, T+1):
    arr = input()
    word = f'{arr[0]}'
    for i in range(1,len(arr)-1):
        if arr[i] != word[0]:
            word += arr[i]
        elif arr[i] == word[0] and arr[i+1] != word[1]:
            word += arr[i]
        else:
            break
    print(f'#{tc} {len(word)}')
