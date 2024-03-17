T = int(input())


def preorder(n):
    global result
    if n:  # n이 0이여야 true
        result += 1
        preorder(ch1[n])
        preorder(ch2[n])


for test_case in range(1, T+1):
    E, N = map(int, input().split())
    inputlist = list(map(int, input().split()))

    result = 0
    # 노드의 갯수는 E+1, 0번째 리스트 요소를 안사용할 예정(+1).
    ch1 = [0]*(E+2)
    ch2 = [0]*[E+2]

    for i in range(0, len(inputlist), 2):
        parent, child = inputlist[i], inputlist[i+1]

        if ch1[parent] == 0:
            ch1[parent] = child
        elif ch2[parent] == 0:
            ch2[parent] = child
