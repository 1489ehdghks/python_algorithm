rny_string = "masterpiece"


def solution(rny_string):
    return rny_string.replace('m', 'rn')


a = solution(rny_string)
print(a)

# 다른 사람풀이


def solution(rny_string):
    answer = []
    for x in rny_string:
        if x == 'm':
            answer.append('rn')
        else:
            answer.append(x)
    return ''.join(answer)
