array = [1, 1,1,1, 2, 3, 4, 5]

def solution(array, n):
    result = 0
    for i in array:
        if i == n:
            result += 1
    return result


a= solution(array,1)
print(a)