
def solution(array, n):
    result = 0
    for i in array:
        if i == n:
            result += 1
    return result


# 다른 사람 풀이
def solution(array, n):
    return array.count(n)
# string.count(self, x, __start, __end) 함수
# count의 특징
# 1. 대소문자를 구분합니다.
# 2. 찾을 x 에 문자 한개를 넣어도 가능하고 문자열을 넣어도 가능합니다.
# 3. __start, __end에 아무것도 넣지 않으면 문자열 처음부터 끝까지 탐색합니다.
# 4. 찾을 x의 범위는 __start <= x < __end 입니다. __start도 포함 __end 는 안 포함.


def solution(array, n):
    return sum(1 for x in array if x == n)
