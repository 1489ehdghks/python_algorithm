my_string = "aAb1B2cC34oOp"


def solution(my_string):
    name = list(my_string)
    x = 0
    for i in name:
        if i.isdigit():
            x += int(i)

    return x


a = solution(my_string)
print(a)


# 다른 사람 풀이

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())


def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass

    return answer
