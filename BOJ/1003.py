"""
1. 아이디어
- dp로 1부터 N까지 각 1과 0 수를 저장하고 중복돼서 나오면 그 값을 더한다.
2. 시간복잡도
- 500만 이하
- O(N)?
3. 자료구조
- T: int
- dp: int[41][3]: y는 인덱스(0~40) x는 0: 0횟수 1: 1횟수 2: 값 저장되어 있는지
"""

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