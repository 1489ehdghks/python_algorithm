my_string = "We are the world"


def solution(my_string):
    answer = list(my_string)
    a = ''
    for i in answer:
        if i not in a:
            a += i

    return a


print(solution(my_string))
