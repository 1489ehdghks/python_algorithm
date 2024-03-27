from collections import deque

numbers = [1, 2, 3]
direction = "right"


def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    elif direction == 'left':
        numbers.rotate(-1)

    return list(numbers)


print(solution(numbers, direction))


# deque(덱)은 앞 뒤로 요소를 추가하고 삭제할 수 있는 자료구조
# rotate(1)는 제일 뒤에 있던게 제일 앞으로 이동합니다.
# popleft()는 제일 끝 요소가 아니라 제일 앞의 요소가 삭제가 됨
