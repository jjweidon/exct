N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
check = list(map(int, input().split()))

def binarySearch(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in range(M):
    print(binarySearch(check[i], cards), end = " ")