def solution(num1, num2):
    a = num1/num2
    b = int(a*1000)
    return b

# 다른 사람 풀이


def solution(num1, num2):
    return int(num1 / num2 * 1000)

# 지역변수를 사용하지 않는 이유
# 변수를 저장하기 위해선 비용이 듭니다. 비용이 늘면 시스템 성능의 저하가 올 수 있습니다.
# 또한 함수화 된 코드는 굳이 변수에 담지 않더라도 return 값으로 주면,
# 차후에 x = solution(someting) 같은 형태로 불러와서 사용이 가능하니, 재사용이 없는 함수 내 지역변수는 굳이 변수에 담지 않는 것을 추천합니다.


def solution(num1, num2):
    answer = (num1/num2)*1000
    return answer//1

# //는 몫


def solution(x, y): return 1000 * x // y
