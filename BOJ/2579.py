import sys
input = sys.stdin.readline

N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [0] * N

dp[0] = stair[0]
if N >= 2:
    dp[1] = stair[1] + stair[0]
    if N >= 3:
        dp[2] = stair[2] + max(stair[0], stair[1])

for i in range(3, N):
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

print(dp[N - 1])