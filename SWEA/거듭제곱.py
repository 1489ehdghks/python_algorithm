def Square(n, m):
    if m == 0:
        return 1
    return n * Square(n, m-1)


for i in range(1, 11):
    t = int(input())
    a, b = map(int, input().split())
    result = Square(a, b)
    print(f'#{t}', result)
