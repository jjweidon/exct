from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cnt = 0

while True:
    visited = [[False] * N for _ in range(N)]
    def bfs(y, x):
        q = deque([(y, x)])
        visited[y][x] = True
        group = [(y, x)]
        while q:
            ey, ex = q.popleft()
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if ny in (-1, N) or nx in (-1, N) or visited[ny][nx]:
                    continue
                if not L <= abs(A[ey][ex] - A[ny][nx]) <= R:
                    continue
                group.append((ny, nx))
                q.append((ny, nx))
                visited[ny][nx] = True
        
        if len(group) == 1:
            return False

        popularity = 0
        for gy, gx in group:
            popularity += A[gy][gx]
        popularity //= len(group)
        for gy, gx in group:
            A[gy][gx] = popularity
        return True
    
    check = False
    for j in range(N):
        for i in range(N):
            if visited[j][i]:
                continue
            check |= bfs(j, i)
    if check:
        cnt += 1
    else:
        break

print(cnt)