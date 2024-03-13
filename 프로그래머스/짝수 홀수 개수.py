num_list = [1, 2, 3, 4, 5]


def solution(num_list):
    list = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            list[0] += 1
        else:
            list[1] += 1
    return list


a = solution(num_list)
print(a)


# 다른 사람 풀이

def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1
    return answer
