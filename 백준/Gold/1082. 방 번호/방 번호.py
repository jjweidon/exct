N = int(input())
P = list(map(int, input().split()))
M = int(input())

nums = [(i, P[i]) for i in range(N)]
nums.sort(key=lambda x: (x[1], -x[0]))
dp = [0] * (M+1)
# 초기화
for i in range(N):
    for j in range(i + 1):
        if nums[i][1] > M:
            continue
        dp[nums[i][1]] = max(nums[i][0], dp[nums[i][1] - nums[i - j][1]] * 10 + nums[i-j][0])

for m in range(M+1):
    for n in range(N):
        if m - nums[n][1] < 0:
            continue
        dp[m] = max(dp[m], dp[m-1], dp[m - nums[n][1]] * 10 + nums[n][0])

print(dp[M])