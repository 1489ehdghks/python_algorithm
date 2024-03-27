num = 29183
k = 7


def solution(num, k):
    answer = list(map(int, str(num)))
    result = 0
    for index, i in enumerate(answer, 1):
        if i == k and result == 0:
            result = index
    if k not in answer:
        result = -1

    return result


print(solution(num, k))
