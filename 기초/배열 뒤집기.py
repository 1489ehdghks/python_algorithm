num_list = [1, 2, 3, 4, 5]


def solution(num_list):
    return list(reversed(num_list))


a = solution(num_list)
print(a)

# 다른 사람의 풀이


def solution(num_list):
    return num_list[::-1]


def solution(num_list):
    num_list.reverse()
    return num_list


def solution(num_list):
    answer = num_list
    answer.reverse()
    return answer
