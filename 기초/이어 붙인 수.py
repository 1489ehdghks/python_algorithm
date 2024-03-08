num_list = [3, 4, 5, 2, 1]


def solution(num_list):
    x = ''
    y = ''
    for i in num_list:
        if i % 2 == 1:
            x += str(i)
        else:
            y += str(i)
    z = int(x)+int(y)
    return z


a = solution(num_list)
print(a)
