"""
R은 뒤집기
D는 앞에 버리기
"""

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

    for rd in p:
        if rd == 'R':
            deq.reverse()
        
        else:
            if deq:
                deq.popleft()
            else:
                print("error")
                break
    
    else:
        print(f"[{','.join(map(str, deq))}]")