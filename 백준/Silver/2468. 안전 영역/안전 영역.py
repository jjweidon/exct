from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
rs = 0

for h in range(101):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    def bfs(y, x):
        q = deque([(y, x)])
        while q:
            ey, ex = q.popleft()
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if ny in (-1, N) or nx in (-1, N) or visited[ny][nx]:
                    continue
                if maps[ny][nx] <= h:
                    continue
                q.append((ny, nx))
                visited[ny][nx] = True

    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                continue
            if maps[y][x] <= h:
                continue
            bfs(y, x)
            cnt += 1
    rs = max(cnt, rs)

print(rs)