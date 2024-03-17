n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]


def solution(n, numlist):
    n_list = []
    for i in numlist:
        if i % n == 0:
            n_list.append(i)
    return n_list


print(solution(n, numlist))


# 다른 사람 풀이
def solution(n, numlist):
    answer = [i for i in numlist if i % n == 0]
    return answer
