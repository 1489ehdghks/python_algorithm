x = int(input())
a = 0
b = 0
for j in range(x):
    y = list(input())
    for i in y:
        if i == '(':
            a += 1
        elif i == ')':
            b += 1
        else:
            pass
    if a == b:
        print("YES")
        a = 0
        b = 0
    else:
        print("NO")
        a = 0
        b = 0
