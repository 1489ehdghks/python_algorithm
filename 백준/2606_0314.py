N = int(input())
M = int(input())

c_list = [[]for i in range(N)]

for j in range(M):
    com1, com2 = map(int, input().split(' '))
    if com2 not in c_list[com1-1]:
        c_list[com1-1].append(com2)

    if com1 not in c_list[com2-1]:
        c_list[com2-1].append(com1)

print(c_list)
