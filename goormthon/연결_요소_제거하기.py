import sys
from collections import deque
input = sys.stdin.readline

N, K, Q = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def bfs():
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([])
    for j in range(N):
        for i in range(N):
            if visited[j][i]:
                continue

            if arr[j][i] == '.':
                visited[j][i] = True
                continue

            q.append((j, i))
            visited[j][i] = True
            chk = []
            while q:
                ey, ex = q.popleft()
                chk.append((ey, ex))
                for k in range(4):
                    ny = ey + dy[k]
                    nx = ex + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if arr[ny][nx] == arr[ey][ex]:
                            q.append((ny, nx))
                            visited[ny][nx] = True
            
            if len(chk) >= K:
                for y, x in chk:
                    arr[y][x] = '.'

for _ in range(Q):
    y, x, d = input().split()
    y = int(y) -1
    x = int(x) - 1
    arr[y][x] = d
    bfs()

for row in arr:
    print(''.join(x for x in row))


# 정해 코드

def f(i, j, c):
	arr[i][j] = c
	stack = [(i, j)]
	visited = set()
	
	while stack:
		y, x = stack.pop()
		
		if (y, x) in visited:
			continue
		
		visited.add((y, x))
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or arr[ny][nx] != arr[y][x]:
				continue
			
			stack.append((ny, nx))
	
	if len(visited) >= K:
		for y, x in visited:
			arr[y][x] = "."

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, K, Q = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for _ in range(Q):
	i, j, c = input().split()
	f(int(i) - 1, int(j) - 1, c)

for i in arr:
	print(''.join(i))