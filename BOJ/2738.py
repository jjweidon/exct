import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_A = []
arr_B = []
for _ in range(N):
    arr_A.append(list(map(int, input().split())))
for _ in range(N):
    arr_B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(arr_A[i][j] + arr_B[i][j], end=" ")
    print("")