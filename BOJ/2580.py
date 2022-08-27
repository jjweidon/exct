# PyPy3: Wrong
import sys
input = sys.stdin.readline

sudoku = [[0] * 9 for _ in range(9)] # 9*9 스도쿠 판 (입력받을)
zero = [] # 비어있는 칸(0) x, y 좌표를 담을 리스트

# 스도쿠 판 입력 및 0을 가지고 있는 좌표 zero에 담기
for i in range(9):
    sudoku[i] = list(map(int, input().split()))
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i, j)) # 0이 있는 좌표 zero에 저장

# 열, 행, 박스 탐색 함수를 통해 해당 숫자가 해당 범위에 있으면 False, 겹치지 않는 숫자면 True를 return

# 열 탐색 함수
def checkRow(x, num):
    for i in range(9):
        if sudoku[x][i] == num:
            return False
    return True

# 행 탐색 함수
def checkCol(y, num):
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True

# 3*3박스 탐색
def checkBox(x, y, num):
    # 좌표를 포함하는 3*3 박스에 해당 숫자가 있는 지 확인
    x //= 3
    y //= 3
    for i in range(x*3, (x+1)*3):
        for j in range(y*3, (y+1)*3):
            if num == sudoku[i][j]:
                return False
    return True

def dfs(idx):
    if idx == len(zero):
        # 최종 스도쿠 판을 출력
        for i in range(9):
            print(' '.join(map(str, sudoku[i])))
        return
    
    x = zero[idx][0] # zero의 해당 인덱스 x좌표값
    y = zero[idx][1] # zero의 해당 인덱스 y좌표값

    for i in range(1, 10):
        if checkRow(x, i):
            if checkCol(y, i):
                if checkBox(x, y, i):
                    sudoku[x][y] = i # 조건에 맞으면 0이 있던 자리에 해당 숫자 입력
                    dfs(idx + 1) # 다음 노드(다음 zero 인덱스)로 이동
                    sudoku[x][y] = 0 # ***백트랙킹: dfs가 끝나면 원상태로***

dfs(0) # zero의 0번째 좌표부터 dfs 시작