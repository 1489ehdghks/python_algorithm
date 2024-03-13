str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"


def solution(str1, str2):

    if str2 in str1:
        return 1
    else:
        return 2


a = solution(str1, str2)
print(a)


# 다른 사람의 풀이

def solution(str1, str2):
    return 1 if str2 in str1 else 2


def solution(str1, str2):
    return 1 + int(str2 not in str1)
