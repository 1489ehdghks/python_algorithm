n = 144


def solution(n):
    x = n**(1/2)
    if x == int(x):
        return 1
    return 2


a = solution(n)
print(a)
