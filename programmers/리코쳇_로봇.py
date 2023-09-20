from collections import deque

def solution(board):
    lst = [[] for _ in range(len(board))]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    s_y, s_x = 0, 0
    e_y, e_x = 0, 0
    for j, line in enumerate(board):
        for i, ele in enumerate(board[j]):
            lst[j].append(ele)
            if ele == 'R':
                s_y, s_x = j, i
            elif ele == 'G':
                e_y, e_x = j, i
    
    q = deque([(s_y, s_x)])
    visited[s_y][s_x] = True
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    step = 0
    
    while q:
        step += 1
        for _ in range(len(q)):
            ey, ex = q.popleft()
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if ny in (-1, len(board)) or nx in (-1, len(board[0])) or board[ny][nx] == 'D':
                    continue
                while not (ny+dy[k]  in (-1, len(board)) or nx+dx[k] in (-1, len(board[0])) or board[ny+dy[k]][nx+dx[k]] == 'D'):
                    ny += dy[k]
                    nx += dx[k]
                
                if ny == e_y and nx == e_x:
                    return step
                
                if not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
    
    return -1


# 정해 코드

def solution(board):
    que = []
    for x, row in enumerate(board):
        for y, each in enumerate(row):
            if board[x][y] == 'R':
                que.append((x, y, 0))
    visited = set()
    while que:
        x, y, length = que.pop(0)
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return length
        visited.add((x, y))
        for diff_x, diff_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x + diff_x, now_y + diff_y
                if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != 'D':
                    now_x, now_y = next_x, next_y
                    continue
                que.append((now_x, now_y, length + 1))
                break
    return -1