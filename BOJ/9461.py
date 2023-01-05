"""
1. 아이디어
- 1 1 1 2 2 초기값
- P(N) = P(N-1) + P(N-5)
2. 시간복잡도
- O(N) 가능
3. 자료구조
- P: int[]
"""

import sys
input = sys.stdin.readline

P = [0] * 101
P[1], P[2], P[3], P[4], P[5] = 1, 1, 1, 2, 2

def dp(N):
    if P[N-1] == 0 or P[N-5] == 0:
        dp(N-1)
    P[N] = P[N-1] + P[N-5]
    return

T = int(input())
for _ in range(T):
    N = int(input())
    if not P[N]:
        dp(N)
    print(P[N])