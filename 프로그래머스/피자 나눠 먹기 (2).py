n = 6


def solution(n):
    p = 1
    while (p*6) % n != 0:
        p += 1
    return p


print(solution(n))
