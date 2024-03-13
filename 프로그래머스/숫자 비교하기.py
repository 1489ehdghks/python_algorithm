def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1


# 다른 사람풀이
def solution(num1, num2):
    return 1 if num1 == num2 else -1


def solution(num1, num2):
    answer = -1
    if num1 == num2:
        answer = 1
    return answer


def solution(num1, num2):
    return -1 if num1 != num2 else 1


def solution(num1, num2):
    return ((num1 == num2)-0.5)*2