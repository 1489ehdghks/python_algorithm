def solution(num1, num2):
    return num1 % num2


# 다른 사람풀이

def solution(num1, num2):
    # return num1%num2
    while num1 >= num2:
        num1 -= num2
    return num1


def solution(num1, num2):
    return divmod(num1, num2)[1]

# divmod() : 나눗셈의 몫과 나머지를 (몫, 나머지) 형태로 반환함
