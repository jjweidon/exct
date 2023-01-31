import sys
input = sys.stdin.readline

K = int(input())
total = []
for _ in range(K):
    price = int(input())
    if price == 0:
        total.pop()
    else:
        total.append(price)
print(sum(total))