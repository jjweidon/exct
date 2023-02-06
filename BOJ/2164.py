from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cards = deque()
cards.extend([i + 1 for i in range(N)])

for i in range(2 * (N - 1)):
    if i % 2 == 0:
        cards.popleft()
    else:
        cards.append(cards.popleft())

print(cards[0])