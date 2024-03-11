num_list = [2, 3, 4, 5]


def solution(num_list):
    a = 1
    b = 0
    if len(num_list) <= 10:
        for i in num_list:
            a = a * i
        return a
    else:
        for i in num_list:
            b += i
        return b


a = solution(num_list)
print(a)

# 다른 사람 풀이


def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))

# from math import prod


def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else prod(num_list)
