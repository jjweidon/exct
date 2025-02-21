N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
dp = [[0] * (101) for _ in range(N + 1)]

for j in range(1, N+1):
    for i in range(1, 101):
        if i < L[j]:
            dp[j][i] = dp[j-1][i]
        else:
            dp[j][i] = max(dp[j-1][i], dp[j-1][i-L[j]] + J[j])

print(dp[N][99])