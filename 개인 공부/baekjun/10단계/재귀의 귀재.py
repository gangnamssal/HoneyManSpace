# 주어진 함수를 활용하여 재귀 횟수를 구하면 된다.
# 재귀를 할 때 마다 cnt를 1씩 증가하는게 만들어서 출력한다.
def recursion(s, l, r,cnt):
    global num
    if l >= r:
        num = cnt
        return 1
    elif s[l] != s[r]:
        num = cnt
        return 0
    else: return recursion(s, l+1, r-1,cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)

N = int(input())
num = 0
for i in range(N):
    arr = input()
    print(isPalindrome(arr),num+1)