# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# id_list = ["muzi", "frodo", "apeach", "neo"]
# k = 2
# def solution(id_list, report, k):
#     answer = []
#     answer_first = []
#     answer_second = []
#     answer_third = []
#     report = list(set(report))
#     for i in id_list:
#         for j in range(len(report)):
#             if i in report[j][:len(i)]:
#                 answer_first.append(report[j][len(i)+1:])
#     for h in id_list:
#         if answer_first.count(h) >= k:
#             answer_second.append(h)
#     for x in answer_second:
#         for y in range(len(report)):
#             if x in report[y][-len(x):]:
#                 answer_third.append(report[y][:-len(x)-1])
#     for n in id_list:
#         answer.append(answer_third.count(n))
#     return answer

# print(solution(id_list, report, k))



report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
id_list = ["muzi", "frodo", "apeach", "neo"]
k = 2
def solution(id_list, report, k):
    answer = []
    answer_first = []
    answer_third = []
    report = list(set(report))
    for i in id_list:
        for j in range(len(report)):
            if i in report[j][:len(i)]:
                answer_first.append(report[j][len(i)+1:])
    for h in id_list:
        if answer_first.count(h) >= k:
            for y in range(len(report)):
                if h in report[y][-len(h):]:
                    answer_third.append(report[y][:-len(h)-1])
    for n in id_list:
        answer.append(answer_third.count(n))
    return answer

print(solution(id_list, report, k))