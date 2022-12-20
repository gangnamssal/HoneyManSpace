# # 총 10개의 테스트 케이스가 존재
# for i in range(1, 11):
#     sum = 0
#     # 첫 줄에는 테스트 케이스 길이가 주어진다.
#     N = int(input())

#     # 다음 줄에는 테스트 케이스가 주어진다.
#     test_case = list(map(int, input().split()))

#     for num in range(2, N-2): # 첫 2개랑 마지막 2개는 빼고
#         # 앞에 2 수와 뒤에 2수가 작고 4개의 수의 최댓값을 빼서 더함
#         if (test_case[num-2] < test_case[num]) and (test_case[num-1] < test_case[num]) and (test_case[num+1] < test_case[num]) and (test_case[num+2] < test_case[num]):
#             max_num = max(test_case[num-1], test_case[num-2], test_case[num+2], test_case[num+1])
#             sum += (test_case[num] - max_num)

#     print(f'#{i} {sum}')

# nomax
# 총 10개의 테스트 케이스가 존재

for i in range(1, 11):
    sum = 0
    # 첫 줄에는 테스트 케이스 길이가 주어진다.
    N = int(input())

    # 다음 줄에는 테스트 케이스가 주어진다.
    test_case = list(map(int, input().split()))

    for num in range(2, N-2): # 첫 2개랑 마지막 2개는 빼고
        # 앞에 2 수와 뒤에 2수가 작고 4개의 수의 최댓값을 빼서 더함
        if (test_case[num-2] < test_case[num]) and (test_case[num-1] < test_case[num]) and (test_case[num+1] < test_case[num]) and (test_case[num+2] < test_case[num]):
            max_num = test_case[num-2]
            for j in test_case[num-1:num+3]:
                if j == test_case[num]:
                    continue
                elif max_num < j:
                    max_num = j
            sum += test_case[num] - max_num

    print(f'#{i} {sum}')