소중한메모지 = [0, 1]


def fib(n):
    if n < len(소중한메모지):
        return 소중한메모지[n]

    소중한메모지.append(fib(n-1))
