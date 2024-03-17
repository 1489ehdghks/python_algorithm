n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin_list.append(int(input()))
count = 0

for i in reversed(range(n)):
    if k == 0:
        break
    else:
        a, b = divmod(k, coin_list[i])
        k = b
        count += a


print(count)
