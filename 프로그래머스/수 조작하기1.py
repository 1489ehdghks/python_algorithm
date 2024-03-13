n = 0
control = "wsdawsdassw"


def solution(n, control):
    for i in control:
        if i == 'w':
            n = n+1
        elif i == 's':
            n = n-1
        elif i == 'd':
            n = n+10
        elif i == 'a':
            n = n-10
        else:
            pass

    return n


a = solution(n, control)
print(a)


# 다른 사람 풀이
def solution(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


def solution(n, control):
    answer = n
    c = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    for i in control:
        answer += c[i]
    return answer
