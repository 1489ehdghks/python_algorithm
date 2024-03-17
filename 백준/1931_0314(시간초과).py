N = int(input())
meetings = []


def sort(x):
    return x[1], x[0]


for i in range(0, N):
    s_time, e_time = map(int, input().split(" "))
    meetings.append((s_time, e_time))
    meetings.sort(key=sort)

time = 0
answer = 0
for j in meetings:
    if time <= j[0]:
        print("time00", time)
        print("j00", j[0])
        time = j[1]
        print("j11", j)
        print("time11:", time)
        answer += 1
print(meetings)
print(answer)

# 시간 초과.
