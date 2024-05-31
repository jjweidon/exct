N, M = map(int, input().split())
A = list(map(int, input().split()))
maxx = sum(A)
dp = [False] * (maxx+1)
cnt = 0

presum = [0] * (N+1)
for i in range(1, N+1):
    presum[i] = presum[i-1] + A[i-1]
    dp[presum[i]] = True

for i in range(N+1):
    index = presum[i] + M
    if index > maxx:
        break
    if dp[index]:
        cnt += 1

print(cnt)