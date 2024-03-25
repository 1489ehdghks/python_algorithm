my_string = "hi12392"


def solution(my_string):
    answer = list(my_string)
    answer.sort()
    x = []
    for i in answer:
        if (i.isdigit()):
            x.append(int(i))

    return x


print(solution(my_string))
