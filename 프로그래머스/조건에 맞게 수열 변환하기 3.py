arr = [1, 2, 3, 100, 99, 98]
k = 3


def solution(arr, k):
    if k % 2 == 1:
        return [x * k for x in arr]
    else:
        return [x + k for x in arr]


print(solution(arr, k))
