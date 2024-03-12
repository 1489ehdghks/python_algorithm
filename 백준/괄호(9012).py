n = int(input())


for i in range(0, n):
    stack = []
    a = input()

    for j in a:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack and stack[-1] == '(':
                stack.pop()
                print("stack",stack)
            else:
                print("NO")
                break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")


