import sys
input = sys.stdin.readline

def fibonacci(n):
    if dp[n][2]:
        return dp[n][0], dp[n][1]

    elif n == 0:
        dp[n][0] += 1
    elif n == 1:
        dp[n][1] += 1
    else:
        recur1 = fibonacci(n-1)
        recur2 = fibonacci(n-2)
        dp[n][0] = recur1[0] + recur2[0]
        dp[n][1] = recur1[1] + recur2[1]
    dp[n][2] = 1
    return dp[n][0], dp[n][1]

T = int(input())
dp = [([0] * 3) for _ in range(41)]
for _ in range(T):
    N = int(input())
    rs = fibonacci(N)
    print(rs[0], rs[1])