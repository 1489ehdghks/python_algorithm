n = 64
k = 6


def solution(n, k):
    return n*12000 + k*2000 - (n//10)*2000


a = solution(n, k)
print(a)
