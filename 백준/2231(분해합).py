a = int(input())


def asdf(n):
    for i in range(1, n):
        sum1 = sum(map(int, str((i))))
        sum2 = i + sum1
        if sum2 == n:
            return i
    return 0


x = asdf(a)
print(x)
