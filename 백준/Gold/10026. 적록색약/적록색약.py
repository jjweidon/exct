from collections import deque

N = int(input())
pixel = [[x for x in input()] for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def check(blind):
    cnt = 0
    visited = [[False] * N for _ in range(N)]

    def bfs(j, i):
        q = deque([(j, i)])
        while q:
            ey, ex = q.popleft()
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if ny in (-1, N) or nx in (-1, N) or visited[ny][nx]:
                    continue
                if pixel[ny][nx] != pixel[ey][ex] and (not blind or pixel[ny][nx] == 'B' or pixel[ey][ex] == 'B'):
                    continue
                q.append((ny, nx))
                visited[ny][nx] = True

    for j in range(N):
        for i in range(N):
            if visited[j][i]:
                continue
            bfs(j, i)
            cnt += 1
    return cnt

print(check(False), check(True))