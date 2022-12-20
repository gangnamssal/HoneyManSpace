# 1을 걸려면 총 2초가 필요
# 1보다 큰 수는 1초씩 더 걸림
# 첫 줄에는 알파벳이 대문자로 주어짐
char = input()
arr = [['A', 'B', 'C'],['D','E','F'],['G','H','I'],['J','K','L'],
        ['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
sum = 0
# 입력 받은 문자열이 배열안에 포함이 되어 있을때
for i in char:
    for j in range(len(arr)):
        if i in arr[j]:
            sum += j+3
print(sum)