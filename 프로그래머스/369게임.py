
order = 29423


def solution(order):
    answer = list(str(order))
    clap = 0
    for i in answer:
        print(i)
        if i == '3' or i == '6' or i == '9':
            clap += 1
    return clap


print(solution(order))
