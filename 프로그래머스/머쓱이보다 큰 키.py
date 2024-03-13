array = [149, 180, 192, 170]


def solution(array, height):
    x = 0
    for i in array:
        if i > height:
            x += 1

    return x


a = solution(array, 167)
print(a)

# 다른 사람 풀이


def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)


def solution(array, height):
    return sum(1 for a in array if a > height)


def solution(array, height):
    return len([i for i in array if i > height])
