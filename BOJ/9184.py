"""
1. 점화식
- -1 -1 -1 이면 종료
- 하나라도 0 이하면 1
- 하나라도 20 초과면 w(20,20,20)
- a < b < c: w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
- else: w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

2. 시간복잡도
- 20*20*20 = 8000 *2 = 16000

3. 자료구조
- w[a][b][c]
"""
import sys
input = sys.stdin.readline

w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for c in range(1, 21):
    for b in range(1, 21):
        for a in range(1, 21):
            if a < b < c:
                w[a][b][c] = w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
            else:
                w[a][b][c] = w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

def fnum(a, b ,c):
    if a <= 0 or b <= 0 or c <= 0:
        a, b, c = 0, 0, 0
    elif a > 20 or b > 20 or c > 20:
        a, b, c  = 20, 20, 20
    return a, b, c

while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    rs = fnum(a, b, c)

    print(f"w({a}, {b}, {c}) = {w[rs[0]][rs[1]][rs[2]]}")