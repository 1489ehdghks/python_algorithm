money = 15000


def solution(money, x=0):
    if money >= 5500:
        return solution(money - 5500, x + 1)
    else:
        return [x, money]


a = solution(money)
print(a)

# 다른사람 풀이


def solution(money):

    answer = [money // 5500, money % 5500]
    return answer


def solution(money):
    return divmod(money, 5500)


def solution(money):
    cup = money//5500
    change = money % 5500
    return [cup, change]
