a = 2
b = 91


def solution(a, b):
    x = int(str(a) + str(b))
    y = 2 * a * b
    return max(x, y)


zxcv = solution(a, b)
print(zxcv)


# 다른 사람 풀이
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
