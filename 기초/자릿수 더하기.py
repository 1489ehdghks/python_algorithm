n = 1234


def solution(n):
    num = 0
    for i in str(n):
        num += int(i)
    return num


a = solution(n)
print(a)

# 다른 사람 풀이


def solution(n):
    return sum(int(i) for i in str(n))


def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n //= 10
    return answer


def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer
