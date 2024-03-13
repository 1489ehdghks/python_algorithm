num_list = [15, 98, 23, 2, 15]
n = 20


def solution(num_list, n):
    if n in num_list:
        return 1
    else:
        return 0


a = solution(num_list, n)
print(a)


# 다른 사람 풀이
def solution(num_list, n):
    return int(n in num_list)
