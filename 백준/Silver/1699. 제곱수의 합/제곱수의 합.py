N = int(input())
dp = [float('inf') for i in range(N+1)]
dp[0] = 0

for j in range(1, N+1):
    for i in range(int(j ** (0.5)), 0, -1):
        dp[j] = min(dp[j], dp[j - (i ** 2)] + 1)

print(dp[-1])