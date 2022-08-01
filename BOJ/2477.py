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
for direction in range(1,5):
    if ewsn.count(direction) == 1:
        size1 *= length.pop(ewsn.index(direction))
        ewsn.pop(ewsn.index(direction))
size2 = length[1] * length[2]

print(K * (size1 - size2))