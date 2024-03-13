high_number = 0
x = 1
y = 1

for i in range(1, 10):
    input_list = list(map(int, input().split()))
    for j, num in enumerate(input_list, 1):
        if high_number < num:
            high_number = num
            x = i
            y = j
print(high_number)
print(i, j)
