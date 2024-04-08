num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2


def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        answer.append(num_list[n*i: n*(i+1)])

    return answer


print(solution(num_list, n))
