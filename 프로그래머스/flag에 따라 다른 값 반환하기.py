a = -4
b = 7
flag = True


def solution(a, b, flag):
    if flag == True:
        return a+b
    else:
        return a-b


a = solution(a, b, flag)
print(a)


# 다른 사람 풀이

def solution(a, b, flag):
    if flag:
        return a+b
    return a-b
