# 조카는 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서
# 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다.
# 문자열 배열 babbling이 매개변수로 주어질 때,
# 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return
def solution(babbling):
    possible_word = ["aya", "ye", "woo", "ma"]
    result = 0
    for i in babbling:
        compare_word = ''
        compare_lst = []
        for j in i:
            compare_word += j
            if compare_word in possible_word and (not compare_lst or compare_word != compare_lst[-1]):
                compare_lst.append(compare_word)
                compare_word = ''
        else:
            if not compare_word:

                result += 1
    return result

