import sys
input = sys.stdin.readline

N = int(input())
cards = [0]
cards += list((map(int, input().split())))
dp = cards

for i in range(2, N + 1):
    for j in range(1, (i // 2) + 1):
        tmp = cards[j] + dp[i - j]
        if tmp > dp[i]:
            dp[i] = tmp

print(dp[N])