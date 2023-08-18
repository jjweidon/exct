N = int(input())
k = list(map(int, input().split()))
rs = k[0]
btn = False

for i in range(1, N):
    rs += k[i]
    if not btn:
        if k[i] < k[i-1]:
            btn = True
    if btn:
        if k[i] > k[i-1]:
            rs = 0
            break

print(rs)


# 정해 코드

N = int(input())
arr = list(map(int, input().split()))

MAX = max(arr)
maxIndex = arr.index(MAX)

left = arr[:maxIndex]
right = arr[maxIndex:]

left.sort()
right.sort(reverse=True)

sortedArr = left + right

for i in range(N):
	if arr[i] != sortedArr[i]:
		print(0)
		break
else:
	print(sum(arr))