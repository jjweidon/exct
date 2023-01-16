"""
1. 아이디어
- 밑에서부터 최대합이 되는 값을 누적하여 더하며 올라간다
2. 시간복잡도
- 4000만 이하 : 500^2 = 250000 O(N^2) 가능
3. 자료구조
- tri[n]: int
"""

import sys
input = sys.stdin.readline

n = int(input())
tri = [0] * n

for i in range(n):
    tri[n - i - 1] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(n - i):
        tri[i][j] = max(tri[i-1][j], tri[i-1][j+1]) + tri[i][j]

print(tri[n-1][0])