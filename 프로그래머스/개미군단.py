hp = 23


def solution(hp):
    ants = [5, 3, 1]
    result = 0
    for i in ants:
        (a, b) = divmod(hp, i)
        result += a
        hp = b
    return result


print(solution(hp))
