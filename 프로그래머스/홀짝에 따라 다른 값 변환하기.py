n = 10


def solution(n):
    total_홀수 = 0
    total_짝수 = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            total_홀수 += i
        else:
            total_짝수 = total_짝수 + i**2
    if n % 2 == 1:
        return total_홀수
    else:
        return total_짝수


print(solution(n))


# 다른 사람 풀이
def solution(n):
    answer = 0
    if n % 2:
        for i in range(1, n+1, 2):
            answer += i
    else:
        for i in range(2, n+1, 2):
            answer += i**2
    return answer
