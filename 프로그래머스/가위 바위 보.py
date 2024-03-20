rsp = "205"


def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        elif i == "5":
            answer += "2"
    return answer


print(solution(rsp))


# 다른 사람 풀이

def solution(rsp):
    d = {'0': '5', '2': '0', '5': '2'}
    return ''.join(d[i] for i in rsp)
