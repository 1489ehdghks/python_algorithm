my_string = "abcdef"
letter = "f"


def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer


a = solution(my_string, letter)
print(a)


# 다른 사람의 풀이
def solution(my_string, letter):
    return my_string.replace(letter, '')


def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer
