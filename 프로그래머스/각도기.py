def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    return 4


# 다른 사람 풀이

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer


def solution(angle):
    if angle <= 90:
        return 1 if angle < 90 else 2
    else:
        return 3 if angle < 180 else 4


def solution(angle):
    angles = {180: 4, 91: 3, 90: 2, 0: 1}
    for base, result in angles.items():
        if angle >= base:
            return result


def solution(angle):
    return 2 if angle == 90 else 1 if angle < 90 else 4 if angle == 180 else 3
