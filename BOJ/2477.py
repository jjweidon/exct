import sys
input = sys.stdin.readline

K = int(input())
ewsn = []
length = []
for i in range(6):
    a, b = map(int, input().split())
    ewsn.append(a)
    length.append(b)

size1 = 1
size2 = 1
for direction in range(1,5):
    if ewsn.count(direction) == 1:
        size1 *= length[ewsn.index(direction)]
        size2 *= length[(ewsn.index(direction)+3) % 6]

print(K * (size1 - size2))