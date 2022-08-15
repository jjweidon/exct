N = int(input()) #입력

# 퀸이 놓여질 수 있는 경우의 수를 출력할 결과 변수
result = 0
# N개의 열 생성
row = [0] * N

def check(x):
    for i in range(x):
        # 같은 행에 퀸이 놓여져 있거나 or 좌우 대각선 위로 퀸이 놓여져 있는경우 False 반환
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    # 앞에 놓여진 퀸과 겹치지 않으면 True 반환
    return True

def dfs(num):
    # dfs가 N만큼 진행돼 퀸이 N만큼 놓이면 result를 1증가, dfs 종료
    if num == N:
        global result
        result += 1
        return
    # num 열의 각 행을 check하며 적합한 위치에 퀸을 놓고 다음 열로 dfs를 진행해야 함
    for i in range(N):
        row[num] = i
        if check(num):
            # check에서 True를 반환하면 다음 열로 dfs 진행
            dfs(num+1)

# dfs(0)으로 0번째 열부터 탐색 시작
dfs(0)
print(result) # 결과 출력