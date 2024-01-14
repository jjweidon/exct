def solution(x, y, n):
    dp = [0 for _ in range(y+1)]

    for num in range(x+1, y+1):
        temp = []
        if num - n >= x and dp[num - n] != -1:
            temp.append(dp[num - n]+1)
        if num % 2 == 0 and num // 2 >= x and dp[num // 2] != -1:
            temp.append(dp[num // 2]+1)
        if num % 3 == 0 and num // 3 >= x and dp[num // 3] != -1:
            temp.append(dp[num // 3]+1)
        
        if temp:
            dp[num] = min(temp)
        else:
            dp[num] = -1
    
    return dp[y]