n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
start, end = 0, n-1
cnt = 0

while start < end:
    add = a[start] + a[end]
    if add == x:
        cnt += 1
        start += 1
        end -= 1
        continue
    if add < x:
        start += 1
        continue
    if add > x:
        end -= 1
        continue

print(cnt)