import sys
input = sys.stdin.readline

sudoku = [[0] * 9 for _ in range(9)] # 9*9 스도쿠 판 생성
zero = [] # 비어있는 칸 좌표를 담을 리스트

# 스도쿠 판 입력 및 0을 가지고 있는 좌표 zero에 담기
for i in range(9):
    sudoku[i] = list(map(int, input().split()))
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i, j))

# 열 탐색 함수
def checkRow(x, y):
    for i in range(1, 10):
        # 열에 1~9 중 없는 숫자가 있으면 checkCol로 좌표와 숫자를 보냄
        if i not in sudoku[x]:
            checkCol(x, y, i)
    return

# 행 탐색 함수
def checkCol(x, y, num):
    for i in range(9):
        # 행에 checkRow로부터 받은 숫자가 있으면 리턴
        if num == sudoku[i][y]:
            return
    # 행에 checkRow로부터 받은 숫자가 없으면 checkBox로 좌표와 숫자를 보냄
    checkBox(x, y, num)

# 3*3박스 탐색
def checkBox(x, y, num):
    # 좌표를 포함하는 3*3 박스에 checkCol로부터 받은 숫자가 있는 지 확인
    for i in range((x//3)*3, (x//3+1)*3):
        for j in range((y//3)*3, (y//3+1)*3):
            # 숫자가 있으면 리턴 (함수 종료)
            if num == sudoku[i][j]:
                return
    # 박스 안에 겹치는 숫자가 없으면 좌표에 그 숫자를 담고 다음 zero 좌표로 이동
    sudoku[x][y] = num
    return

# 0을 가지고 있는 좌표들을 checkRow로 하나씩 보냄
for x, y in zero:
    checkRow(x, y)

# 최종 스도쿠 판을 출력
for i in range(9):
    print(' '.join(map(str, sudoku[i])))