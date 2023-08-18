N, K = map(int, input().split())
a = list(map(int, input().split()))

lst = [[a[i], 0] for i in range(N)]
lst.sort(key=lambda x : -x[0])

for i in range(N):
    temp = lst[i][0]
    while temp > 0:
        if temp % 2 == 1:
            lst[i][1] += 1
        temp //= 2

lst.sort(key=lambda x : -x[1])

print(lst[K-1][0])