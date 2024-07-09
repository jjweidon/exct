import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1]
    if arr: arr = arr.split(',')
    deq = deque(arr)
    rvs = False

    for rd in p:
        if rd == 'R':
            if rvs:
                rvs = False
            else:
                rvs = True
        
        else:
            if not deq:
                print("error")
                break

            if rvs:
                deq.pop()
            else:
                deq.popleft()

    else:
        if rvs:
            deq.reverse()
        print(f"[{','.join(map(str, deq))}]")