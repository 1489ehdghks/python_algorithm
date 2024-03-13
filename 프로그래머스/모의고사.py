answers = [1, 3, 2, 4, 2]


def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    winner = [0, 0, 0]

    for index, i in enumerate(answers):
        if i == one[index % len(one)]:
            # print(f"one이 {index}번째 문제 맞힘")
            score[0] += 1

        if i == two[index % len(two)]:
            # print(f"two가 {index}번째 문제 맞힘")
            score[1] += 1

        if i == three[index % len(three)]:
            # print(f"three가 {index}번째 문제 맞힘")
            score[2] += 1

    max_score = max(score)

    for index, i in enumerate(score):
        if i == max_score:
            winner[index] += index+1
        else:
            winner[index] = None

    result_list = []
    for j in winner:
        if j is not None:
            result_list.append(j)

    return result_list


# 다른 사람 풀이
def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
