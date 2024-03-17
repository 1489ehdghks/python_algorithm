numbers = [34, 5, 71, 29, 100, 34]
n = 123


def solution(numbers, n):
    total=0
    for i in numbers:
        total +=i
        if total > n:
            return total


print(solution(numbers, n))
