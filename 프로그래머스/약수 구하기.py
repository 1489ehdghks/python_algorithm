n = 29


def solution(n):
    x = []
    for i in range(1, n+1):
        if n % i == 0:
            x.append(i)
    return x


print(solution(n))
