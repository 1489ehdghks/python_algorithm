s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]


def solution(s1, s2):
    x = []
    for i in s1:
        if i in s2:
            x.append(i)
    return len(x)


a = solution(s1, s2)
print(a)

# 다른 풀이


def solution(s1, s2):
    return len(set(s1) & set(s2))
