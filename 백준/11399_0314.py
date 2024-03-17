N = int(input())
P = list(map(int, input().split()))
P.sort()

total_time = 0
accumulate_time = 0

for time in P:
    accumulate_time += time
    total_time += accumulate_time
    print("total_time", total_time)

print(total_time)
