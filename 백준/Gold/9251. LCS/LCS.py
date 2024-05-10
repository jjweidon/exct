str1 = list(input())
str2 = list(input())
N, M = len(str1), len(str2)
dp = [[0] * N for _ in range(M)]
if str1[0] == str2[0]:
    dp[0][0] = 1

for j in range(1, M):
    if str2[j] == str1[0] or dp[j-1][0]:
        dp[j][0] = 1

for i in range(1, N):
    if str1[i] == str2[0] or dp[0][i-1]:
        dp[0][i] = 1

for j in range(1, M):
    for i in range(1, N):
        dp[j][i] = dp[j-1][i-1] + 1 if str2[j] == str1[i] else max(dp[j][i-1], dp[j-1][i])
        
print(dp[M-1][N-1])