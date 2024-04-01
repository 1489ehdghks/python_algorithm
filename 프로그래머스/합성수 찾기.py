n = 10


def solution(n):
    list = []
    answer = 0

    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                list.append(i)
        if list.count(i) >= 3:
            answer += 1

    return answer


print(solution(n))
