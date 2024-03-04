def solution(n):
    a = range(0, n+1, 2)
    return sum(a)

# 다른 사람 풀이


def solution(n):
    return sum([i for i in range(2, n + 1, 2)])


def solution(n):
    return 2*(n//2)*((n//2)+1)/2


def solution(n):
    return sum(range(0, n+1, 2))


def solution(n):
    return sum(filter(lambda v: v % 2 == 0, [_ for _ in range(n+1)]))


def solution(n):
    answer = 0
    return sum(i for i in range(1, n+1) if i % 2 == 0)


def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer
