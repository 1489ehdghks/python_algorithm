arr = [1, 2, 3, 100, 99, 98]


def solution(arr):
    a_list = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            a_list.append(int(i/2))
        elif i < 50 and i % 2 == 1:
            a_list.append(i*2)
        else:
            a_list.append(i)
    return a_list


print(solution(arr))
