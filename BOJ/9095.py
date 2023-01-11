import sys
input = sys.stdin.readline

f = [1] * 11
for i in range(1, 11):
    f[i] = f[i-1] * i

dp = [0] * 11

T = int(input())
for _ in range(T):
    n = int(input())
    if not dp[n]:
        cnt = 0
        tmp3 = n // 3
        for i in range(tmp3 + 1):
            index = n - (3 * i)           
            tmp2 = index // 2
            for j in range(tmp2 + 1):
                tmp1 = index - (2 * j)
                cnt += f[i + j + tmp1] // (f[i] * f[j] * f[tmp1])
        dp[n] = cnt

    print(dp[n])