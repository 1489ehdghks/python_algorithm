numbers = [1, 2, 3, 4, 5]


def solution(numbers):
    x = []
    for i in numbers:
        x.append(i*2)
    return x


a = solution(numbers)
print(a)

# 다른 사람 문제 풀이


def solution(numbers):
    return [num*2 for num in numbers]
