num_list = [5, 7, 8, 3]


def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a = a * i
        b = b + i
    print(a, b**2)
    if a < b**2:
        return 1
    else:
        return 0


a = solution(num_list)
print(a)

# 다른 사람 풀이


def solution(num_list):
    s = sum(num_list)**2
    m = eval('*'.join([str(n) for n in num_list]))
    return 1 if s > m else 0


def solution(num_list):
    a = 1
    b = 0
    for x in num_list:
        a *= x
        b += x
    if a < b*b:
        return 1
    return 0
