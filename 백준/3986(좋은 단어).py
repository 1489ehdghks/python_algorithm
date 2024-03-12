n = int(input())
best_word = 0

for i in range(0, n):
    stack = []
    a = input()
    for j in a:
        if j == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()

            else:
                stack.append(j)

        elif j == 'B':
            if stack and stack[-1] == 'B':
                stack.pop()

            else:
                stack.append(j)

    if not stack:
        best_word += 1
print(best_word)
