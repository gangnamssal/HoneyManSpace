# d(n) = n과 n의 각 자리수를 더하는 함수
# d(75) = 75 + 7 + 5 = 87
# 생성자가 없는 숫자를 셀프 넘버
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 출력
def self_num():
    num_list = []
    num = 1
    self_number = str()
    while num < 10000:  # d(n)의 수를 구하여 빈 리스트에 저장
        if num < 10:
            num_list.append(num + num%10)
            num += 1
        elif num < 100:
            num_list.append(num+num%10+num//10)
            num += 1
        elif num < 1000:
            num_list.append(num+num%10+(num//10)%10+(num//10)//10)
            num += 1
        else:
            num_list.append(num+num%10+(num//10)%10+(num//100)%10+(num//100)//10)
            num += 1
    for i in range(1,10001): # 셀프넘버를 구함
        if i not in num_list:
            self_number += str(i) + '\n'
    return self_number

print(self_num())


