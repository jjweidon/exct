def solution(board):
    cnt = [0, 0, 0, 0] # cnt_o, cnt_x, line_o, line_x
    
    def chk_cnt(j, i, o, x):
        if board[j][i] == 'O':
            o += 1
        if board[j][i] == 'X':
            x += 1
        return o, x
    
    def chk_line(o, x):
        if o == 3:
            cnt[2] += 1
        if x == 3:
            cnt[3] += 1
        return
    
    # 가로 3줄 체크 + OX 개수 체크
    for j in range(3):
        o, x = 0, 0 
        for i in range(3):
            if board[j][i] == 'O':
                cnt[0] += 1
            if board[j][i] == 'X':
                cnt[1] += 1
            o, x = chk_cnt(j, i, o, x)
        chk_line(o, x)

    # 세로 3줄 체크    
    for i in range(3):
        o, x = 0, 0 
        for j in range(3):
            o, x = chk_cnt(j, i, o, x)
        chk_line(o, x)
            
    # 대각선 /
    o, x = 0, 0     
    for i in range(3):
        o, x = chk_cnt(i, 2 - i, o, x)
    chk_line(o, x)
        
    # 대각선 \
    o, x = 0, 0    
    for i in range(3):
        o, x = chk_cnt(i, i, o, x)
    chk_line(o, x)

    # o개수 - x개수가 0이나 1이 아닐 때
    if cnt[0] - cnt[1] not in (0, 1):
        return 0
    
    # o 2라인일 때 그 개수가 5개가 아닐 때
    if cnt[2] == 2 and cnt[0] != 5:
        return 0
    
    # o 1라인일 때 x가 o랑 같거나 더 많을 때
    if cnt[2] == 1 and cnt[0] <= cnt[1]:
            return 0
    
    # x 1라인일 때 둘이 개수 다를 때
    if cnt[3] == 1 and cnt[0] != cnt[1]:
            return 0
    
    return 1


# 정해 코드

def check_win(player, board):
    # Check rows
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0

    elif (check_win('O', board) and num_x != num_o - 1) or (check_win('X', board) and num_x != num_o):
        return 0

    return 1