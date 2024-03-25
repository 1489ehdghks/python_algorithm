my_string = "hello"
num1 = 1
num2 = 2


def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    x = ''
    for i in my_string:
        x += i

    return x


print(solution(my_string, num1, num2))


# 다른 사람 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)
