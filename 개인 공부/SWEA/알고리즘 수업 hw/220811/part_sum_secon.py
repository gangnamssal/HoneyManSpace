# 재귀를 활용한 부분 집합
arr = [1,2,3,4,5]
N = 5
# idx 에 해당하는 요소의 부분집합 포함 여부 결정
selected = [0]*N
def ps(idx):
    if idx == N: # 재귀 호출 하지 않음
        # print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i],end=',')
        print()
        return
    # 부분 집합에 포함
    selected[idx] = 1
    ps(idx+1)
    # 부분 집합에 포함시키지 않음
    selected[idx] = 0
    ps(idx+1)

ps(0)
