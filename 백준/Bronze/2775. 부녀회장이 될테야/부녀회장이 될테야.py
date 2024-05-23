dp = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    dp[0][i] = i
for j in range(1, 15):
    dp[j][1] = dp[j-1][1]
    for i in range(2, 15):
        dp[j][i] = dp[j][i-1] + dp[j-1][i]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])