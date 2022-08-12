import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dtbojob = list(set([input().rstrip() for i in range(N)]) & set([input().rstrip() for i in range(M)]))
dtbojob.sort()

print(len(dtbojob))
for x in dtbojob:
    print(x)