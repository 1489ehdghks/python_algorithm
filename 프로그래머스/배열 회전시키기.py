numbers = [1, 2, 3]
direction = "right"


def solution(numbers, direction):
    x = []
    if direction == 'right':
        numbers = numbers[-1]
    elif direction == 'left':
        numbers = numbers[-1]
