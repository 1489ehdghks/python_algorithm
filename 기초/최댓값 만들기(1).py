numbers = [0, 31, 24, 10, 1, 9]


def solution(numbers):
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    return a*b


a = solution(numbers)
print(a)

# 다른사람 풀이


def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
