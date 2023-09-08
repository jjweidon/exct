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