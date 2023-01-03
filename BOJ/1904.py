"""
1. 점화식
- tile(N): tile(N-1) + tile(N-2)
2. 시간복잡도
- O(N)
3. 자료구조
- tile(N)
"""

import sys
input = sys.stdin.readline

N = int(input())

tile = [0] * (N + 1)

tile[1] = 1
tile[2] = 2

for i in range(3, N + 1):
    tile[i] = tile[i - 1] + tile[i - 2]
    if tile[i] >= 15746: tile[i] = tile[i] % 15746

print(tile[N])