import sys
input = sys.stdin.readline

def get_score(r, c):
    chk = [[0] * N for _ in range(N)]
    ny = r - 1
    nx = c - 1
    score = 0

    done = False
    while not done:
        count = int(board[ny][nx][:-1])
        command = board[ny][nx][-1]
        dy, dx = 0, 0
        if command == 'U':
            dy = -1
        elif command == 'D':
            dy = 1
        elif command == 'R':
            dx = 1
        elif command == 'L':
            dx = -1
        
        for _ in range(count):
            chk[ny][nx] = 1
            score += 1
            ny = (ny + dy + N) % N
            nx = (nx + dx + N) % N  
            if chk[ny][nx] == 1:
                done = True
                break
    
    return score

N = int(input())
goorm = list(map(int, input().split()))
player = list(map(int, input().split()))
board = [input().split() for _ in range(N)]

score_g = get_score(goorm[0], goorm[1])
score_p = get_score(player[0], player[1])

if score_g > score_p:
    print('goorm', score_g)
elif score_g < score_p:
    print('player', score_p)
