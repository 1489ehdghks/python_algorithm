dot = [-5, 12]


def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] > 0 and dot[1] < 0:
        return 4
    else:
        return 3


a = solution(dot)
print(a)
