def solution(num1, num2):
    return divmod(num1, num2)[0]


# 다른사람 풀이


solution = int.__floordiv__
# operator.__ifloordiv__(a, b)
# a = ifloordiv(a, b)는 a //= b와 동등합니다.


def solution(num1, num2):
    answer = num1 / num2
    return int(answer)


def solution(num1, num2):
    return num1 // num2


def solution(x, y): return x//y

# lambda 매개변수 : 표현식
# >>> def hap(x, y):
# ...   return x + y
# ...
# >>> hap(10, 20)
# 30

# 이것을 람다 형식으로는 어떻게 표현할까요?

# >>> (lambda x,y: x + y)(10, 20)
# 30
