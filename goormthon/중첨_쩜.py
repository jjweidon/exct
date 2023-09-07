import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pan = [[[0, 0] for _ in range(N)] for _ in range(N)] # [세로선 수, 가로선 수]

for _ in range(M):
    y, x, d = input().split()
    y, x = map(int, [y, x])
    if d == 'U':
        for j in range(y):
            pan[j][x-1][0] += 1
    if d == 'D':
        for j in range(y-1, N):
            pan[j][x-1][0] += 1
    if d == 'L':
        for i in range(x):
            pan[y-1][i][1] += 1
    if d == 'R':
        for i in range(x-1, N):
            pan[y-1][i][1] += 1

rs = 0
for j in range(N):
    for i in range(N):
        rs += pan[j][i][0] * pan[j][i][1]

print(rs)


# 정해 코드

N, M = map(int, input().split())
arr = [[[0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
	y, x, d = input().split()
	y = int(y) - 1
	x = int(x) - 1

	if d == "R":
		for j in range(x, N):
			arr[y][j][1] += 1
	elif d == "L":
		for j in range(x + 1):
			arr[y][j][1] += 1
	elif d == "U":
		for i in range(y + 1):
			arr[i][x][0] += 1
	elif d == "D":
		for i in range(y, N):
			arr[i][x][0] += 1

result = 0

for i in range(N):
	for j in range(N):
		result += arr[i][j][0] * arr[i][j][1]
	
print(result)