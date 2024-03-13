strlist = ["We", "are", "the", "world!"]


def solution(strlist):
    array = []
    for x in strlist:
        array.append(len(x))

    return array


a = solution(strlist)
print(a)

# 다른 사람의 풀이


def solution(strlist):
    answer = list(map(len, strlist))
    return answer


def solution(strlist):
    return [len(str) for str in strlist]
