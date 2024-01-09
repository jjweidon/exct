import sys
sys.setrecursionlimit(100000)

def solution(n, k, enemy):
    N = len(enemy)
    dp = [[0] * (k+1) for _ in range(N)]
    visited = [[False] * (k+1) for _ in range(N)]
    dp[0][0] = enemy[0]
    for j in range(1, N):
        dp[j][0] = dp[j-1][0] + enemy[j]
        visited[j][0] = True
    for i in range(k+1):
        visited[0][i] = True
    
    def dfs(j, i):
        if not visited[j][i]:
            dp[j][i] = min(dfs(j-1, i-1), dfs(j-1, i) + enemy[j])
            visited[j][i] = True
        return dp[j][i]
    
    for j in range(1, N):
        dp[j][k] = dfs(j, k)
        if dp[j][k] == n:
            return j+1
        elif dp[j][k] > n:
            return j
    return N