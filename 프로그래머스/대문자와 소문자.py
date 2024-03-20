my_string = "cccCCC"


def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer


print(solution(my_string))


# 다른 사람 풀이

def solution(my_string):
    return my_string.swapcase()
