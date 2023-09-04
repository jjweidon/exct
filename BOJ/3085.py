N = int(input())
candy = [[''] * N for _ in range(N)]
for j in range(N):
    temp = input()
    for i in range(N):
        candy[j][i] = temp[i]

def chk():
    cnt = 0

    # 가로 체크
    for j in range(N):
        temp = 1
        for i in range(1, N):
            if candy[j][i] == candy[j][i-1]:
                temp += 1
            else:
                temp = 1
            cnt = max(cnt, temp)
    
    # 세로 체크
    for i in range(N):
        temp = 1
        for j in range(1, N):
            if candy[j][i] == candy[j-1][i]:
                temp += 1
            else:
                cnt = max(cnt, temp)
            cnt = max(cnt, temp)

    return cnt

rs = 0
dy = [1, 0]
dx = [0, 1]

for j in range(N):
    for i in range(N):
        for k in range(2):
            ny = j + dy[k]
            nx = i + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if candy[j][i] != candy[ny][nx]:
                    candy[j][i], candy[ny][nx] = candy[ny][nx], candy[j][i]
                    rs = max(rs, chk())
                    candy[j][i], candy[ny][nx] = candy[ny][nx], candy[j][i]

print(rs)