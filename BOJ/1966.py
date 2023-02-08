import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    imp = deque()
    imp.extend(list(map(int, input().split())))
    cnt = 0

    while 1:
        maxx = max(imp)

        if M == 0 and imp[0] == maxx:
            cnt += 1
            print(cnt)
            break

        elif M == 0 and not imp[0] == max:
            imp.append(imp.popleft())
            M = len(imp) - 1
        
        elif not M == 0 and imp[0] == maxx:
            imp.popleft()
            cnt += 1
            M -= 1
        
        else:
            imp.append(imp.popleft())
            M -= 1