start_num = 3
end_num = 10


def solution(start_num, end_num):
    a = []
    for i in range(start_num, end_num+1):
        a.append(i)
    return a


print(solution(start_num, end_num))


# 다른 사람 풀이
def solution(start, end):
    return list(range(start, end + 1))
