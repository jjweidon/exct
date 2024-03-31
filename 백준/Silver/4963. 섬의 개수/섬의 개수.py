from collections import deque

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    jido = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False if jido[j][i] else True for i in range(w)] for j in range(h)]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    dx = [0, 0, 1, -1, -1, 1, -1, 1]
    cnt = 0

    def bfs(y, x):
        q = deque([(y, x)])
        visited[y][x] = True
        while q:
            ey, ex = q.popleft()
            for k in range(8):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if ny in (-1, h) or nx in (-1, w) or visited[ny][nx]:
                    continue
                q.append((ny, nx))
                visited[ny][nx] = True

    for j in range(h):
        for i in range(w):
            if visited[j][i]:
                continue
            bfs(j, i)
            cnt += 1
    
    print(cnt)