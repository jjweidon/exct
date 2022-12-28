import sys
input = sys.stdin.readline

paper = [[False for _ in range(100)] for _ in range(100)]

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = True

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]: cnt += 1
print(cnt)