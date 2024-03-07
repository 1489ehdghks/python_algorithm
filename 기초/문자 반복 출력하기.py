my_string = "hello"
n = 3


def solution(my_string, n):

    x = ''
    for i in my_string:

        a = i*n
        x += a
    return x


a = solution(my_string, n)
print(a)

# 다른 사람 풀이


def solution(my_string, n):
    return ''.join(i*n for i in my_string)
