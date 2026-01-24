import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0] * (N+1)
tree = [0] * (N+1)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= i & -i
    return result

def update(i, DIFF):
    while i <= N:
        tree[i] += DIFF
        i += i & -i

def interval_sum(s, e):
    return prefix_sum(e) - prefix_sum(s-1)

for i in range(1, N+1):
    arr[i] = int(input())
    update(i, arr[i])

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1: # update
        DIFF = c - arr[b]
        arr[b] = c
        update(b, DIFF)

    if a == 2: # interval_sum
        print(interval_sum(b, c))