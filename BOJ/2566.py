import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

max = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if max < arr[i][j]:
            max = arr[i][j]
            row = i
            col = j

print(max)
print(row+1, col+1)