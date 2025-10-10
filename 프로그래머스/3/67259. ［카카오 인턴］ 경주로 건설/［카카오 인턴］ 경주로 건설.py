from collections import deque

def solution(board):
    N = len(board)
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    
    q = deque([])
    for d in range(4):
        visited[0][0][d] = 0
        q.append((0, 0, d, 0))
    
    while q:
        cy, cx, cd, cost = q.popleft()
        if cy == N-1 and cx == N-1:
            continue
        
        for nd in range(4):
            ny = cy + dy[nd]
            nx = cx + dx[nd]
            if ny in (-1, N) or nx in (-1, N): continue
            if board[ny][nx]: continue
            ncost = cost + 100 if cd == nd else cost + 600
            if visited[ny][nx][nd] <= ncost: continue
            visited[ny][nx][nd] = ncost
            q.append((ny, nx, nd, ncost))
    
    return min(visited[N-1][N-1])
                    