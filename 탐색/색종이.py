# 색종이의 수 입력받기
n = int(input())

# 도화지를 나타내는 100x100 크기의 이차원 리스트 초기화 (0: 흰색, 1: 검은색)
paper = [[0 for _ in range(100)] for _ in range(100)]

# 색종이를 붙인 영역을 1로 표시
for _ in range(n):
    left, bottom = map(int, input().split())  # 색종이의 왼쪽 및 아래쪽 변과의 거리
    # 해당 영역에 색종이 붙이기
    for i in range(left, left+10):
        for j in range(bottom, bottom+10):
            paper[i][j] = 1

# 붙은 색종이의 총 넓이 계산
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
