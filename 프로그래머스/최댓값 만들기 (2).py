numbers = [0, -31, 24, 10, 1, 9]


def solution(numbers):
    numbers = sorted(numbers)
    max = 0
    if numbers[0]*numbers[1] >= numbers[-1]*numbers[-2]:
        max += numbers[0]*numbers[1]
    else:
        max += numbers[-1]*numbers[-2]
    return (max)


print(solution(numbers))
