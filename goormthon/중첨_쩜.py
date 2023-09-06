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