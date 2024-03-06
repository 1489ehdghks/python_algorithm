slice = 7
n = 10


def solution(slice, n):

    if n % slice > 0:
        return n//slice+1
    return n//slice


a = solution(slice, n)
print(a)

# 다른 사람 풀이


def solution(slice, n):
    return ((n - 1) // slice) + 1


def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)
