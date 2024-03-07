n = int(input())
try_number = 0
for i in range(1, n+1):
    text = input()
    try_number += 1
    x = 0
    if text == text[::-1]:
        x = 1
    pass

    print(f"#{try_number}", x)
