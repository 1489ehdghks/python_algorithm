cipher = "dfjardstddetckdaccccdegk"
code = 4


def solution(cipher, code):
    answer = ''
    for i in range(code, len(cipher)+1):
        if i % code == 0:
            answer += cipher[i-1]

    return answer


print(solution(cipher, code))


# 다른 사람 풀이

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
