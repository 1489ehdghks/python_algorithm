my_string = "jaron"


def solution(my_string):
    return ''.join(reversed(my_string))


a = solution(my_string)
print(a)

# 다른 사람의 풀이


def solution(my_string):
    return my_string[::-1]
