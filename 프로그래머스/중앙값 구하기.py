array = [9, -1, 0]


def solution(array):
    a = sorted(array)
    b = int(len(array)/2)
    c = a[b]
    return c


a = solution(array)
print(a)

# 다른 사람 풀이


def solution(array):
    return sorted(array)[len(array) // 2]
