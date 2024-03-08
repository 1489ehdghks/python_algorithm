num = 34
n = 3


def solution(num, n):
    if num % n == 0:
        return 1
    return 0


a = solution(num, n)
print(a)


# 다른 사람풀이

def solution(num, n):
    return int(num % n == 0)
