n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    left, bottom = map(int, input().split())
    for i in range(left, left+10):
        for j in range(bottom, bottom+10):
            paper[i][j] = 1

area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

print(area)


n = int(input())

covered_area = set()

for _ in range(n):
    left, bottom = map(int, input().split())
    for i in range(left, left+10):
        for j in range(bottom, bottom+10):
            covered_area.add((i, j))

print(len(covered_area))
