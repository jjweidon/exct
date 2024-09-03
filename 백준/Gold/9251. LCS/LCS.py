str1 = input()
str2 = input()

dp = [[0] * len(str1) for _ in range(len(str2))]

# 초기화
if str1[0] == str2[0]:
    dp[0][0] = 1

for i in range(1, len(str1)):
    if dp[0][i-1] or str1[i] == str2[0]:
        dp[0][i] = 1

for j in range(1, len(str2)):
    if dp[j-1][0] or str2[j] == str1[0]:
        dp[j][0] = 1

# dp 테이블 채우기
for j in range(1, len(str2)):
    for i in range(1, len(str1)):
        if str1[i] == str2[j]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

print(dp[-1][-1])