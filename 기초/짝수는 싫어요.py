n = 10


def solution(n):
    a = []

    for i in range(1, n+1):
        if i % 2 == 1:
            a.append(i)

    return a


a = solution(n)
print(a)


# 다른 사람 풀이

def solution(n):
    return [i for i in range(1, n+1, 2)]


def solution(n):
    return list(range(1, n+1, 2))
