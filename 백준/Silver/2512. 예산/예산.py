N = int(input())
yesans = list(map(int, input().split()))
total = int(input())

s = 0
e = max(yesans)

while s <= e:
    mid = (s + e) // 2
    summary = 0
    for yesan in yesans:
        summary += yesan if yesan < mid else mid
    if summary <= total:
        s = mid + 1
    else:
        e = mid - 1

print(e)