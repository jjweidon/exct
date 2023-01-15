"""
1. 아이디어
- 0 : r / 1 : g / 2 : b
- 각 인덱스 별로 이전까지의 최소 합을 저장한다: dp
2. 시간복잡도
- 0.5 * 2000만 = 천만 = 10^7: O(N) 이하
3. 자료구조
- house[N][3]: int
"""

import sys
input = sys.stdin.readline

N = int(input())

house = list(([0] * 3) for _ in range(N))
house[0] = list(map(int, input().split()))

for i in range(1, N):
    house[i] = list(map(int, input().split()))
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]

print(min(house[N-1]))