n = 15


def solution(n):
    if n % 7 > 0:
        return n // 7+1
    return n // 7


a = solution(n)
print(a)

# 다른 사람의 풀이


def solution(n):
    return (n - 1) // 7 + 1
