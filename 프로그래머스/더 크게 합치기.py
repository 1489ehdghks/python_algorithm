a = 9
b = 91


def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    if ab > ba:
        return ab
    elif ab == ba:
        return ab
    else:
        return ba


print(solution(a, b))


# 다른 사람 풀이

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
