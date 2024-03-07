my_string = "bus"


def solution(my_string):
    a = my_string.replace('a', '').replace('e', '').replace(
        'i', '').replace('o', '').replace('u', '')
    return a


a = solution(my_string)

print(a)

# 다른 사람 풀이


def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string


def solution(my_string):
    answer = ''

    for c in my_string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            continue
        answer += c

    return answer
