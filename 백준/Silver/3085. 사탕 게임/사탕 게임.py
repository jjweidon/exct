N = int(input())
board = [list(input()) for _ in range(N)]
dy = [0, 1]
dx = [1, 0]

def check():
    # 가로
    garo = 0
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[j][i] == board[j][i-1]:
                cnt += 1
            else:
                cnt = 1
            garo = max(garo, cnt)
    
    # 세로
    sero = 0
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            sero = max(sero, cnt)
    
    return max(garo, sero)

rs = 0
for j in range(N):
    for i in range(N):
        cy, cx = j, i
        for k in range(2):
            ny = cy + dy[k]
            nx = cx + dx[k]
            if ny >= N or nx >= N:
                continue
            board[cy][cx], board[ny][nx] = board[ny][nx], board[cy][cx]
            rs = max(rs, check())
            board[cy][cx], board[ny][nx] = board[ny][nx], board[cy][cx]

print(rs)