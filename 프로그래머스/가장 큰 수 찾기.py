array = [1, 8, 3]


def solution(array):
    max = 0
    idx = 0
    for index, i in enumerate(array):
        if i > max:
            max = i
            idx = index

    return [max, idx]


print(solution(array))


# 다른풀이
def solution(array):
    val = max(array)
    return [val, array.index(val)]
