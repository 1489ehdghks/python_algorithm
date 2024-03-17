num_list = [2, 1, 6]
n = 1


def solution(num_list, n):
    n_list = []
    for i in range(0, n):
        n_list.append(num_list[i])
    return n_list


print(solution(num_list, n))


# 다른 사람 풀이
def solution(num_list, n):
    return num_list[:n]
